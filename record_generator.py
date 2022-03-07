'''
by Muzaffer Kahraman 2022

This scirpt generates random set of name,surname and age at every min and writes them to the /record.txt as csv format.
Airflow container is supposed to fetch that file.
This script is just for the demo purpose.

'''

import random
import time


def randomrecord():

	names=("Liam","Olivia","Noah","Emma","Oliver","Ava","Elijah","Charlotte","William","Sophia","James","Amelia","Benjamin","Isabella","Lucas","Mia","Henry","Evelyn","Alexander","Harper")
	surnames=("Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin")

	name=random.choice(names)
	surname=random.choice(surnames)
	age=random.randint(18,22)
	record="{0},{1},{2} \n".format(name,surname,age)
	return(record)


if __name__ == "_main__":
	
	while True:
		f=open("/record.txt","w")
		f.write(randomrecord())
		f.close()
		time.sleep(60)

