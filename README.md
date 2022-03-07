This repo includes the docker container environment to test and experience the Airflow elementary steps

**To deploy**

1. https://github.com/muzafferkahraman/airflow_sandbox
2. cd airflow_sandbox
3. make all
4. check if all the containers are up and running 
		> docker ps
5. get the password for the airflow admin
>      docker exec -ti airflow_sandbox_airflow_1 cat /opt/airflow/standalone_admin_password.txt
6. Type <ip of the host>:8080 at  the browser's address bar


		
		

dag: bash_dag.py

This dag simply redirtects the output of "date" command to the /home/airflow/date.txt file
See how it's done, check  airflow_sandbox/dags/bash_dag.py

From the browser 

