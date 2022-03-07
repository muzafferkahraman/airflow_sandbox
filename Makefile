all: airflow mysql centos composeup start_airflow

airflow:
	docker build -t airflow -f Dockerfile_airflow .

mysql:
	docker build -t mysql -f Dockerfile_mysql .

centos:
	docker build -t centos -f Dockerfile_centos .

composeup:
	docker-compose up 

start_airflow:
	docker exec -ti airflow_sandbox_airflow_1 airflow db init
