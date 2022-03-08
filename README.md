This repo includes the docker container environment to try and experience the Airflow elementary steps

**To deploy**

1. git clone https://github.com/muzafferkahraman/airflow_sandbox.git
2. cd airflow_sandbox
3. make all
4. check if all the containers are up and running
>       docker ps
5. get the password for the airflow admin
>      docker exec -ti airflow_sandbox_airflow_1 cat /opt/airflow/standalone_admin_password.txt
6. Type <ip of the host>:8080 at  the browser's address bar, username=admin & password=(you got that at step 5)


7.        

![image info](./images/airflow_login_page.png)


 
	       
![image info](./images/airflow_main_page.png)

	
8. Login to the mysql container and check the table whethet it's populated

>        docker exec -ti airflow_sandbox_mysql_1 bash
>        mysql -u root -p
>        enter Muzo1! as password
>        use school;
>        select * from students;

mysql> select * from students;
+-----------+-----------+------+
| name      | surname   | age  |
+-----------+-----------+------+
| HENRY     | GONZALEZ  |   22 |
| LUCAS     | MOORE     |   20 |
| AVA       | SMITH     |   21 |
| CHARLOTTE | LOPEZ     |   18 |
| EVELYN    | WILSON    |   20 |
| JAMES     | HERNANDEZ |   21 |
| ELIJAH    | GARCIA    |   20 |
| OLIVIA    | JACKSON   |   22 |
| OLIVIA    | TAYLOR    |   20 |
| EVELYN    | WILLIAMS  |   22 |
| CHARLOTTE | THOMAS    |   18 |
| ISABELLA  | THOMAS    |   20 |
| OLIVIA    | ANDERSON  |   22 |
| LIAM      | GONZALEZ  |   19 |
| ISABELLA  | HERNANDEZ |   19 |
| LIAM      | MOORE     |   18 |
| ALEXANDER | WILSON    |   19 |
| ELIJAH    | ANDERSON  |   18 |
| EVELYN    | TAYLOR    |   22 |
| OLIVER    | RODRIGUEZ |   18 |
| SOPHIA    | MARTIN    |   18 |
| WILLIAM   | MARTINEZ  |   22 |
| BENJAMIN  | JOHNSON   |   21 |
| MIA       | HERNANDEZ |   18 |
| ELIJAH    | LOPEZ     |   20 |
+-----------+-----------+------+
25 rows in set (0.00 sec)

Notes: The test environment is composed of 3 containers: Centos, Airflow and Mysql
* 	Centos container runs a very simple api server that provides a csv format of a random name,surname and age, that's changed every minute
* 	Airflow container runs the dag (pipe_demo_dag.py)  that extracts the input by sending http GETs to the centos, transorms it (uppercase) then loads it to the Mysql container
*   Mysql  container stores the db table whose entries are set by the Airflow container, at the db school and table students
	
	





