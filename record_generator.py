'''
by Muzaffer Kahraman 2022
This scirpt generates random set of name,surname and age at every min and writes them to the /record.txt as csv format.
Airflow container is supposed to fetch that file.
This script is just for the demo purpose.
'''

import random
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime


def randomrecord():

	names=("Liam","Olivia","Noah","Emma","Oliver","Ava","Elijah","Charlotte","William","Sophia","James","Amelia","Benjamin","Isabella","Lucas","Mia","Henry","Evelyn","Alexander","Harper")
	surnames=("Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin")

	name=random.choice(names)
	surname=random.choice(surnames)
	age=random.randint(18,22)
	record="{0},{1},{2} \n".format(name,surname,age)
	return(record)



class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = randomrecord()
        self.wfile.write(bytes(message, "utf8"))





if __name__ == "__main__":

  with HTTPServer(('', 5000), handler) as server:
    server.serve_forever()
	
