from bottle import Bottle, request, template, redirect
import sqlite3
import time


# Temp database
sample_users = {
        'user1': 'pass123',
        'user2': 'pass123123',
        }


def signin():
    auth = authentication()
    time.sleep(3)

    if auth:
        redirect('/home')
    else:
        redirect('/')


def authentication():
    username = request.forms.get("username")
    password = request.forms.get("password")

    if username in sample_users:  # Checks if the username already exists
        return False

    else:
        sample_users[username] = password  # Adds new user to the database
        print("Succesfully added the %s to database" %
              (sample_users[username], ))
        return True
