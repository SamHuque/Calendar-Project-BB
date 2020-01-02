from flask import Flask
from flask import send_file
from flask import request
import os
import psycopg2
import datetime

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']

connection = psycopg2.connect(DATABASE_URL, sslmode="require")

# cur = connection.cursor()
# create_table = "CREATE TABLE users (uuid serial PRIMARY KEY, first_name varchar(255), last_name varchar(255))"
# create_events = "CREATE TABLE events (event_id serial PRIMARY KEY, event_name varchar(255), event_location varchar(255), event_type varchar(255), start_time timestamp)"
# join = "select event_name, event_location, event_type, start_time from events join users_events on users_events.event_id = events.event_id where user_id = 1"
# cur.execute(create_table)
# cur.close()
# connection.commit()


def make_ics(user, data):
    file = open(f"user{user}.ics", "w")
    file.write("BEGIN:VCALENDAR\n")
    file.write("VERSION:2.0\n")
    file.write("X-PUBLISHED-TTL:PT1M\n")
    file.write("PRODID:sample calndar server\n")
    for event in data:
        file.write("BEGIN:VEVENT\n")
        file.write(f"DTSTAMP:{datetime.datetime.now()}\n")
        time_start = event[4].isoformat()
        new_start = ""
        for char in time_start:
            if char != "-" and char != ":":
                new_start += char
        file.write(f"DTSTART:{new_start}\n")
        time_end = event[5].isoformat()
        new_end = ""
        for char in time_end:
            if char != "-" and char != ":":
                new_end += char
        file.write(f"DTEND:{new_end}\n")
        file.write(f"SUMMARY:{event[2]}\n")
        file.write(f"LOCATION:{event[3]}\n")
        file.write("SEQUENCE:0\n")
        file.write(f"UID:{event[0]}@samplecalendar\n")
        file.write("END:VEVENT\n")
    file.write("END:VCALENDAR\n")
    file.close()


@app.route("/")
def hello():
    if connection:
        print("CONNECTED TO THE DATABASE")
    return "Calendar Server Home Route. To get a calendar, enter /get-cal?api=api_key"


@app.route("/get-cal")
def test():
    parameter = request.args.get("api")
    sql_statement = f"select events.event_id, event_name, event_location, event_type, start_time, end_time, events.act from events join users_events on users_events.event_id = events.event_id where user_id = {parameter} and act = 1 or act = 2"
    cur = connection.cursor()
    cur.execute(sql_statement)
    data = cur.fetchall()
    cur.close()
    if os.path.exists(f"user{parameter}.ics"):
        os.remove(f"user{parameter}.ics")
        make_ics(parameter, data)
    else:
        make_ics(parameter, data)
    return send_file(f"user{parameter}.ics", mimetype="text/calendar", as_attachment=True)


port = int(os.environ.get("PORT", 5000))
# uncomment the above for heroku
# port = 3500
app.run(host='0.0.0.0', port=port)

# this must be run with python3 and not python
# ex: python3 script.pydig in menu
