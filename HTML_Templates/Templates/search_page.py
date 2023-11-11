


def return_template(search_results):

    search_template = """<!DOCTYPE html>
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

    html_part = """</head>
                        <body>
                        <div>
                        <form method="get" action="/">
                            <input type="submit" value="Go back home">
                        </form>

                        <form method="POST" action="/search">
                            <input type="text" name="search_box" placeholder="Search Topics...">
                                <button type="submit" name="search_button">Search</button>
                        </form>

                            <div class="container">
                                
                                <h2>Search Results</h2>
                                    <ul>
                                        {}
                                    </ul>
                            </div>
                        </body>
                        </html>""".format(''.join(search_results))
    search_template += html_part

    return search_template