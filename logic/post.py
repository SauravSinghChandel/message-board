from bottle import request, redirect
from storage import dataHandler as dH
from HTML_Templates.Templates import *
from logic import fetching
import datetime


dataHandler = dH.dataBaseHandler()

def make_post(session_data):
    date = str(datetime.datetime.now())
    username = session_data['user']
    content = request.forms.get('post')
    topic = request.forms.get('topic')
    message_id = username + date
    data = [date, username, topic, content, message_id]
    dataHandler.addMessage(data)
    redirect('/')
    
def display_posts() -> list[str]:
    res = []
    data = dataHandler.displayTableMessages()
    if len(data) != 0:
        for message in data:
            res.append(post_formatter(fetching.post_data_formatter(message)))
    
    return res

def post_formatter(data: dict) -> str:
    css = """
            <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Post</title>
    <style>
        /* Add some basic styling for better visualization */
        .post {
            border: 1px solid #ccc;
            padding: 10px;
            margin: 10px;
            max-width: 400px;
        }

        .user-topic-line {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }

        .topic-heading {
            display: inline-block;
            font-size: 1.2em;
        }

        .user-name {
            font-weight: bold;
            font-size: 0.8em;
        }

        .content-box {
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 10px;
        }

        .button-box {
            margin-top: 10px;
            display: flex;
            justify-content: space-between;
        }

        .like-button,
        .dislike-button {
            flex: 1;
        }

        .like-count,
        .dislike-count {
            text-align: center;
        }

        .rating-box {
            margin-top: 10px;
        }
    </style>
    </head>"""

    main_body = f"""
    <div class="post" id="{data['message_id']}">
        <!-- User name and Topic heading in the same line -->
        <div class="user-topic-line">
            <div class="topic-heading">
                <h2>{data['topic']}</h2>
            </div>
            <div class="user-name">
                <strong>{data['username']}</strong>
            </div>
        </div>

        <!-- Message content box -->
        <div class="content-box">
            <!-- Message content -->
            <p>{data['message']}</p>
        </div>

        <!-- Like and Dislike buttons box with counts -->
        <div class="button-box">
            <!-- Like button with count -->
            <div class="like-button">
                <form action="/like/{data['message_id']}" method="post" target="hidden_iframe">
                    <button type="submit">Like</button>
                </form>
                <iframe name="like_hidden_iframe" style="display:none;"></iframe>
                    <div class="like-count">{data['likeStat']}</div>
            </div>

            <!-- Dislike button with count -->
            <div class="dislike-button">
                <form action="/dislike/{data['message_id']}" method="post" target="hidden_iframe">
                <button type="submit">Dislike</button>
                </form>
                <iframe name="Dislike_hidden_iframe" style="display:none;"></iframe>
                <div class="dislike-count">{data['dislikeStat']}</div>
            </div>
        </div>

        <!-- Rating bars box -->
        <div class="rating-box">
            <div>
                <!-- Rating bars -->
                <form action="/structure/{data['message_id']}" method="post">
                <label for="structure">Structure: {data['structure']}</label>
                <input type="range" id="structure" name="structure" min="1" max="5">
                <button type="submit">Rate Structure</button>
                </form>
            </div>

            <div>
                <form action="/quality/{data['message_id']}" method="post">
                <label for="quality">Quality: {data['quality']}</label>
                <input type="range" id="quality" name="quality" min="1" max="5">
                <button type="submit">Rate Quality</button>
                </form>
            </div>
        </div>
    </div>

"""
    return main_body