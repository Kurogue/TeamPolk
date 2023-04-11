'''
This file is used to connect to the PostgreSQL database hosted on cloud provider, Google Cloud.
'''

import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

def connect():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )

    if(connection):
        print("Connection successful!")

    return connection
