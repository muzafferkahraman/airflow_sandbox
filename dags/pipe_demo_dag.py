'''
This DAG is developed to try and experience the airflow

E- extracts the data by sending REST APIs
T- tarnsforms basically by converting every string to uppercase
L- loads the final output to MYSQL

Author: Muzo Kahraman  "muzaffer.kahraman@outlook.com"
'''

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

def send_mysql(ti):
    record=ti.xcom_pull(key='mod_res', task_ids='change_case')
    connection = pymysql.connect(host='airflow_sandbox_mysql_1',user='root',password="Muzo1!",database='school',cursorclass=pymysql.cursors.DictCursor)
  
    with connection.cursor() as cursor:
       
        data=record.split(",")
        data[2]=int(data[2])
        data=tuple(data)
        sql="INSERT INTO `students` (`name`, `surname`,`age`) VALUES " + str(data)
        
        cursor.execute(sql)
        
        connection.commit()
        cursor.close()
        connection.close()

with DAG(
    dag_id='pipe_example',
    # schedule_interval=datetime.timedelta(minutes=1),
    schedule_interval='* * * * *',
    start_date=datetime.datetime(2022, 3, 6),
    catchup=False,
) as dag:

    t1 = PythonOperator(task_id='send_api', python_callable=send_api)
    t2 = PythonOperator(task_id='change_case', python_callable=change_case)
    t3 = PythonOperator(task_id='send_mysql', python_callable=send_mysql)

    t1 >> t2 >> t3


