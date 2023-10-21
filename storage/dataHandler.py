##Handles all the database operations
import sqlite3


conn = sqlite3.connect("APP.db")
c = conn.cursor()
c.execute(f"""CREATE TABLE IF NOT EXISTS users(
            user_ID int NOT NULL,
            userName varchar(255) NOT NULL,
            password varchar(255) NOT NULL,
            PRIMARY KEY(user_ID)
            )""")
c.execute(f"""CREATE TABLE IF NOT EXISTS messages(
            date varChar(255) NOT NULL,
            userName varchar(255) NOT NULL,
            message varchar(255) NOT NULL,
            message_ID int NOT NULL,
            FOREIGN KEY(userName) REFERENCES users(userName)
            )""")
conn.commit()
conn.close()


class dataBaseHandler:
    """
    Creates a dataBaseHandler Object that is used to manipulate the database
    """
    def __init__(self):
        self._userItems = []
        self._messageItems = []

    def __len__(self):
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        item = c.fetchall()
        conn.commit()
        conn.close()
        return len(item)

    def __iter__(self):
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        item = c.fetchall()
        conn.commit()
        conn.close()
        return iter(item)

    def addUser(self, new_item):
        """
        Adds a new user to the database
        :param new_item: Tuple in the format (user_ID, username, password)
        :return: none
        """
        self._userItems.append(new_item)
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute(f"INSERT INTO users VALUES (?,?,?)", (new_item[0], new_item[1], new_item[2]))
        conn.commit()
        conn.close()

    def lookUpUserID(self, key):
        """
        Looks up a specific record using user_ID
        :param key: user_ID
        :return: A tuple containing user record.
        """
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute(f"SELECT * from users WHERE user_ID = (?)", (key,))
        item = c.fetchall()
        conn.commit()
        conn.close()
        return item

    def lookUpUserName(self,userName):
        """
        Looks up a specific record using userName
        :param userName: The username
        :return: A tuple containing user record.
        """
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute(f"SELECT * from users WHERE userName = (?)", (userName,))
        item = c.fetchall()
        conn.commit()
        conn.close()
        return item

    def removeUser(self, key):
        """
        removes a user from the database
        :param key: user_ID
        :return: removed user record
        """
        try:
            conn = sqlite3.connect('APP.db')
            c = conn.cursor()
            c.execute(f"DELETE from users WHERE user_ID = (?)", (key,))
            item = c.fetchall()
            conn.commit()
            conn.close()
            return item
        except IndexError:
            print("Not present in Database.")

    def deleteTableUsers(self):
        """
        Delete the users table
        :return: null
        """
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("DROP TABLE users")
        conn.commit()
        conn.close()


    def __iter__(self):
        pass

    def displayTableUsers(self):
        """
        Displays all the user records
        :return: list of all the user records
        """
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        item = c.fetchall()
        conn.commit()
        conn.close()
        return item

    def addMessage(self, new_item):
        """
        Adds a new message to the table
        :param new_item: message information in the form of a tuple
        :return: null
        """
        self._messageItems.append(new_item)
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("INSERT INTO messages VALUES (?,?,?,?)", (new_item[0], new_item[1], new_item[2], new_item[3]))
        conn.commit()
        conn.close()

    def lookUpuserMessages(self, userName):
        """
        Looks up all the messages of a particular user
        :param userName: userName
        :return: List of all the messages
        """
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute(f"SELECT * from messages WHERE userName = (?)", (userName,))
        item = c.fetchall()
        conn.commit()
        conn.close()
        return item

    def lookUpSpecificMessage(self, userName, messageID):
        """
        Looks up a specific message of a user
        :param userName: userName
        :param messageID: Unique ID of the message
        :return: Returns the specific message
        """
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("SELECT * from messages WHERE userName = (?) AND message_ID = (?)", (userName, messageID))
        item = c.fetchall()
        conn.commit()
        conn.close()
        return item

    def deleteMessage(self, userName, messageID):
        """
        Deletes a message
        :param userName: userName
        :param messageID: Unique message ID
        :return: the deleted item
        """
        try:
            conn = sqlite3.connect('APP.db')
            c = conn.cursor()
            c.execute("DELETE from messages WHERE userName = (?) AND message_ID = (?)", (userName, messageID))
            item = c.fetchall()
            conn.commit()
            conn.close()
            return item
        except IndexError:
            print("Does not exist")

    def deleteTableMessages(self):
        """
        Delete the messages table
        :return: null
        """
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("DROP TABLE messages")
        conn.commit()
        conn.close()

    def displayTableMessages(self):
        """
        Displays all the messages
        :return: null
        """
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("SELECT * FROM messages")
        item = c.fetchall()
        conn.commit()
        conn.close()
        return item






