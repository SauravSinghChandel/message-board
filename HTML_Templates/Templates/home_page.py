from logic import post






def return_template(username):
    
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
        </style>"""
    
    recent_posts = post.display_posts()
    recent_posts = recent_posts[::-1]
    
    html_part = f"""</head>
                        <body>
                            
                            </div>
                            <div class="container">
                                <div id="search">
                                <form method="POST" action="/search">
                                    <input type="text" name="search_box" placeholder="Search Topics...">
                                        <button type="submit" name="search_button">Search</button>
                                </form>
                                <div id="user-info">
                                    {username}
                                    <form id="logout"  method="get" action="/logout">
                                    <input type="submit" value="Logout">
                                    </form>
                                </div>
                                <h2>Create a Post</h2>
                                <form id="post-form" method="post" action="/post">
                                    <textarea id="topic-box" name="topic" rows="1" cols="25" placeholder="Topic Name"></textarea>

                                    <textarea id="post-box" name="post" rows="4" cols="50" placeholder="What's on your mind?"></textarea>
                                    <br>
                                    <input type="submit" value="Post">
                                </form>
                                <h2>Recent Posts</h2>
                                    <ul>
                                        {''.join(recent_posts)}
                                    </ul>
                            </div>
                        </body>
                        </html>"""
    home_template += html_part

    return home_template