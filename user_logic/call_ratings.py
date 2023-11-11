import sqlite3

def get_ratings(database_path, user_ID=None, item_ID=None):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        if user_ID is not None:
            # Retrieve ratings for a specific user
            cursor.execute("SELECT item_ID, rating FROM user_ratings WHERE user_ID=?", (user_ID,))
        elif item_ID is not None:
            # Retrieve ratings for a specific item
            cursor.execute("SELECT user_ID, rating FROM user_ratings WHERE item_ID=?", (item_ID,))
        else:
            # Retrieve all ratings
            cursor.execute("SELECT user_ID, item_ID, rating FROM user_ratings")

        ratings = cursor.fetchall()
        conn.close()
        return ratings
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return None

# Example usages with a specified database file path:
database_file_path = 'your_database_file.db'
user_ratings = get_ratings(database_file_path, user_ID=1)
item_ratings = get_ratings(database_file_path, item_ID=1001)
all_ratings = get_ratings(database_file_path)
