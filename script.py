from flask import Flask
from flask import send_file
from ics import Calendar, Event
import os
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="789abcaaa",
    auth_plugin='mysql_native_password'
)

print(mydb)


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
