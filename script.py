from flask import Flask
from flask import send_file
from ics import Calendar, Event
import os
import psycopg2

app = Flask(__name__)

connection = psycopg2.connect(host="127.0.0.1",
                              port="5432",
                              database="calendar")
cur = connection.cursor()
create_table = "CREATE TABLE users (first_name varchar(255), last_name varchar(255))"
cur.execute(create_table)
cur.close()
connection.commit()


@app.route("/")
def hello():
    return "Hello, World"


@app.route("/get-cal")
def get_cal():
    c = Calendar()
    e = Event()
    e.name = "My cool event"
    e.begin = '2019-11-11 00:00:00'
    c.events.add(e)
    with open('my.ics', 'w') as my_file:
        my_file.writelines(c)
    return send_file("my.ics", mimetype="text/calendar", as_attachment=True)


# port = int(os.environ.get("PORT", 5000))
# uncomment the above for heroku
port = 3500
app.run(host='0.0.0.0', port=port)

# this must be run with python3 and not python
# ex: python3 script.pydig in menu
