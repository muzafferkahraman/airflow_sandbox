from datetime import datetime, timedelta# Airflow modules
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 3, 6),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
    'schedule_interval': '*/2 * * * *'
}

with DAG(    dag_id='test_dag2',
    default_args=default_args,
    schedule_interval=None,
    tags=['test_dag2'],
) as dag:    
    t1 = BashOperator(bash_command="touch ~/my_bash_file.txt", task_id="create_file")    
    t2 = BashOperator(bash_command="date >  ~/my_bash_file.txt", task_id="change_file_name")    
    # Configure T2 to be dependent on T1’s execution
    t1 >> t2
