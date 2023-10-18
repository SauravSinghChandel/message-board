home_template = """<!DOCTYPE html>
<html>
<head>
    <title>Post Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
            text-align: center;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }

        h2 {
            margin-bottom: 20px;
        }

        #post-form {
            margin-bottom: 20px;
        }

        #post-box {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        #user-info {
            text-align: right;
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 10px;
        }

        .post {
            text-align: left;
            border: 1px solid #ccc;
            border-radius: 3px;
            padding: 10px;
            margin-bottom: 15px;
        }

        .post-text {
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div id="user-info">
            User Name
        </div>
        <form method="post" action="/logout">
            <input type="submit" value="Log Out">
        </form>
        <h2>Create a Post</h2>
        <form id="post-form" method="post" action="/post">
            <textarea id="post-box" name="post" rows="4" cols="50" placeholder="What's on your mind?"></textarea>
            <br>
            <input type="submit" value="Post">
        </form>
        <h2>Recent Posts</h2>
        <div id="post-list">
            {% for post in posts %}
            <div class="post">
                <p class="post-text">{{ post }}</p>
            </div>
            {% end %}
        </div>
    </div>
</body>
</html>"""