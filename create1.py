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

cur.execute(create_users)
cur.close()
connection.commit()

cur.execute(create_events)
cur.close()
connection.commit()

cur.execute(create_users_events)
cur.close()
connection.commit()

print("Tables Created")
print("Adding Data...")

insert_user1 = "INSERT INTO users (uuid, first_name, last_name) VALUES (1, 'Owen', 'Outlook')"

insert_user2 = "INSERT INTO users (uuid, first_name, last_name) VALUES (2, 'Glenda', 'Google')"

cur.execute(insert_user1)
cur.close()
connection.commit()

cur.execute(insert_user2)
cur.close()
connection.commit()

print("Users Added")
