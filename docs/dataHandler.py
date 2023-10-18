##Handles all the database operations
import sqlite3


conn = sqlite3.connect("user.db")
c = conn.cursor()
c.execute(f"""CREATE TABLE IF NOT EXISTS users(
            user_ID int NOT NULL,
            username varchar(255) NOT NULL,
            password varchar(255) NOT NULL,
            PRIMARY KEY(user_ID)
            )""")
conn.commit()
conn.close()


class dataBaseHandler:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def add(self,new_item):
        self._items.append(new_item)
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute(f"INSERT INTO users VALUES (?,?,?)", (new_item[0], new_item[1], new_item[2]))
        conn.commit()
        conn.close()

    def lookUpUserID(self,key):
        """Return the matching item"""
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute(f"SELECT * from users WHERE user_ID = (?)", (key))
        item = c.fetchall()
        conn.commit()
        conn.close()
        return item

    def lookUpUserName(self,userName):
        """Return the matching item"""
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute(f"SELECT * from users WHERE username = (?)", (userName,))
        item = c.fetchall()
        conn.commit()
        conn.close()
        return item



    def remove(self, key):
        """Remove a record"""
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute(f"DELETE from users WHERE user_ID = (?)", (key))
        item = c.fetchall()
        conn.commit()
        conn.close()
        return item

    def deleteTable(self):
        """Delete the table"""
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("DROP TABLE users")
        conn.commit()
        conn.close()

    def __iter__(self):
        pass

    def display_table(self):
        """Display the table"""
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        item = c.fetchall()
        conn.commit()
        conn.close()
        return item







