import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
with DAG(
    dag_id='muzokahraman',
    # schedule_interval=datetime.timedelta(minutes=1),
    schedule_interval='* * * * *',
    start_date=datetime.datetime(2022, 3, 6),
    catchup=False,
    tags=['example2', 'example3'],
) as dag:
    t1 = BashOperator(bash_command="touch ~/my_bash_file.txt", task_id="create_file")
    t2 = BashOperator(bash_command="date >  ~/my_bash_file.txt", task_id="change_file_name")
    # Configure T2 to be dependent on T1’s execution
    t1 >> t2

