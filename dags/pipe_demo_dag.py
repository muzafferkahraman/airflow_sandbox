import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
import pymysql.cursors

def send_api(ti):
    res=requests.get("http://airflow_sandbox_centos_1:5000").text 
    ti.xcom_push(key='res', value=res)

def change_case(ti):
    mod_res=ti.xcom_pull(key='res', task_ids='send_api')
    mod_res=mod_res.upper()
    ti.xcom_push(key='mod_res', value=mod_res)

def display(ti):
    record=ti.xcom_pull(key='mod_res', task_ids='change_case')
    connection = pymysql.connect(host='airflow_sandbox_mysql_1',
                             user='root',
                             password='Muzo1!',
                             database='school',
                             cursorclass=pymysql.cursors.DictCursor)

    with connection:
      with connection.cursor() as cursor:
        sql = "INSERT INTO students (`name`, `surname`, `age`) VALUES (%s,%s, %d)"
        A=record.split(",")
        # cursor.execute(sql,(A[0],A[1],A[2]))
        cursor.execute(sql,('muzo','kahraman',49))
       

with DAG(
    dag_id='pipe_example',
    # schedule_interval=datetime.timedelta(minutes=1),
    schedule_interval='* * * * *',
    start_date=datetime.datetime(2022, 3, 6),
    catchup=False,
) as dag:



    t1 = PythonOperator(task_id='send_api', python_callable=send_api)
    t2 = PythonOperator(task_id='change_case', python_callable=change_case)
    t3 = PythonOperator(task_id='display', python_callable=display)
    t1 >> t2 >> t3


