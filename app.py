import json
from flask import Flask
import psycopg2
import os

app = Flask(__name__)
password = os.environ['POSTGRES_PASSWORD']

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/widgets')
def get_widgets():
    with psycopg2.connect(
        host="db",
        user="postgres",
        password=password,
        database="example"
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM widgets")
            
            row_headers=[x[0] for x in cursor.description]

            results = cursor.fetchall()
            json_data=[]
            for result in results:
                json_data.append(dict(zip(row_headers,result)))

    return json.dumps(json_data)

@app.route('/initdb')
def db_init():
    with psycopg2.connect(
        host="db",
        user="postgres",
        password=password,
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute("DROP DATABASE IF EXISTS example")
            cursor.execute("CREATE DATABASE example")

    with psycopg2.connect(
        host="db",
        user="postgres",
        password=password,
        database="example"
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS widgets")
            cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")

    return 'init database'

if __name__ == "__main__":
    app.run(host ='0.0.0.0')
