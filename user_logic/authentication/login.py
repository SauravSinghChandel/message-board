from bottle import Bottle, request, template, redirect
import sqlite3
import time


# Temp database
sample_users = {
        'user1': 'pass123',
        'user2': 'pass123123',
        }


def login():
    auth = authentication()
    time.sleep(3)

    if auth != 'Login failed!':
        redirect('/home')
    else:
        redirect('/')


def authentication():
    username = request.forms.get("username")
    password = request.forms.get("password")

    # Checks if the username and password match
    if username in sample_users and sample_users[username] == password:
        return f'Hello {username}, you have succesfully logged in!'
    else:
        return 'Login failed!'
