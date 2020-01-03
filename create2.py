from flask import Flask
from flask import send_file
from flask import request
import os
import psycopg2
import datetime

DATABASE_URL = os.environ['DATABASE_URL']

connection = psycopg2.connect(DATABASE_URL, sslmode="require")

print("Connected")
cur = connection.cursor()

create_users = "CREATE TABLE users (uuid serial PRIMARY KEY, first_name varchar(255), last_name varchar(255))"
create_events = "CREATE TABLE events (event_id serial PRIMARY KEY, event_name varchar(255), event_location varchar(255), event_type varchar(255), start_time timestamp, end_time timestamp, act integer)"
create_users_events = "CREATE TABLE users_events (id serial PRIMARY KEY, user_id integer, event_id integer)"

insert_user1 = "INSERT INTO users (uuid, first_name, last_name) VALUES (1, 'Owen', 'Outlook')"
insert_user2 = "INSERT INTO users (uuid, first_name, last_name) VALUES (2, 'Glenda', 'Google')"

insert_event1 = "INSERT INTO events (event_id, event_name, event_location, event_type, start_time, end_time, act) VALUES (1, 'Google Pixel Launch', 'Mountain View', 'Product Launch', '2020-01-26 15:00:00', '2020-01-26 16:00:00', 1);"
insert_event2 = "INSERT INTO events (event_id, event_name, event_location, event_type, start_time, end_time, act) VALUES (2, 'Facebook Messenger', 'Los Angelas', 'Product Update', '2020-01-27 16:00:00', '2020-01-27 17:00:00', 1);"
insert_event3 = "INSERT INTO events (event_id, event_name, event_location, event_type, start_time, end_time, act) VALUES (3, 'Morgan Stanley Earnings Call', 'New York', 'Earnings Call', '2020-01-20 12:00:00', '2020-01-20 14:00:00', 1);"
insert_event4 = "INSERT INTO events (event_id, event_name, event_location, event_type, start_time, end_time, act) VALUES (4, 'Lehman Brothers', 'Washington D.C', 'What', '2020-01-19 18:00:00', '2020-01-19 19:00:00', 1);"

insert_users_events1 = "INSERT INTO users_events (user_id, event_id) VALUES (1, 1)"
insert_users_events2 = "INSERT INTO users_events (user_id, event_id) VALUES (1, 2)"
insert_users_events3 = "INSERT INTO users_events (user_id, event_id) VALUES (2, 3)"
insert_users_events4 = "INSERT INTO users_events (user_id, event_id) VALUES (2, 4)"

cur.execute(create_users)
cur.close()
cur = connection.cursor()
cur.execute(create_events)
cur.close()
cur = connection.cursor()
cur.execute(create_users_events)
cur.close()
cur = connection.cursor()
cur.execute(insert_user1)
cur.close()
cur = connection.cursor()
cur.execute(insert_user2)
cur.close()

cur = connection.cursor()
cur.execute(insert_users_events1)
cur.close()
cur = connection.cursor()
cur.execute(insert_users_events2)
cur.close()
cur = connection.cursor()
cur.execute(insert_users_events3)
cur.close()
cur = connection.cursor()
cur.execute(insert_users_events4)
cur.close()

connection.commit()

print("Data Added")
