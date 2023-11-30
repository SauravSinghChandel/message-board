ch_password_template = """<!DOCTYPE html>
<html>
<head>
    <title>Change Password</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
        }

        .container {
            margin: 0 auto;
            padding: 20px;
            width: 300px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }

        h2 {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
        }

        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        input[type="submit"] {
            background-color: #007bff;
            color: #fff;
            padding: 10px 15px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Change Password</h2>
        <form method="post" action="/changePassword">
            <label for="password">Current Password:</label>
            <input type="password" id="old_password" name="old_password" required><br>

            <label for="password">New Password:</label>
            <input type="password" id="new_password" name="new_password" required><br>

            <label for="retype-password">Re-type Password:</label>
            <input type="password" id="retype_new_password" name="retype_new_password" required><br>

            <input type="submit" value="Confirm Changes">
        </form>
        <div>
        <input class="action-button" type="button" value="Cancel In" onclick="location.href='/';">
        </div>
    </div>
</body>
</html>"""

def return_template():
    return ch_password_template
