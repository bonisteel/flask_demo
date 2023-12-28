import os
from flask import Flask, render_template
from flask_mysqldb import MySQL
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv("DB_HOST")
app.config['MYSQL_USER'] = os.getenv("DB_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("DB_NAME")

mysql = MySQL(app) 

@app.route('/')
def index():
    cursor = mysql.connection.cursor()

    cursor.execute("SHOW TABLES LIKE 'persons'")
    result = cursor.fetchone()

    if not result:

        cursor.execute(''' CREATE TABLE persons (id INTEGER, firstname VARCHAR(20), lastname VARCHAR(20)) ''')
        cursor.execute(''' INSERT INTO persons VALUES(1, 'John', 'Doe') ''')
        cursor.execute(''' INSERT INTO persons VALUES(2, 'Milly', 'Winfrerey') ''')
        mysql.connection.commit()

    cursor.execute('SELECT * FROM persons')
    entry = cursor.fetchall()
    cursor.close()
    return render_template('index.html', entry=entry)
