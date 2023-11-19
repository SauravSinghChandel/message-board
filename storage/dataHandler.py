##Handles all the database operations
import sqlite3
import pickle

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
            topic varchar(255) NOT NULL,
            message varchar(255) NOT NULL,
            message_ID int NOT NULL,
            FOREIGN KEY(userName) REFERENCES users(userName)
            )""")
c.execute(f"""CREATE TABLE IF NOT EXISTS messageRatingData(
            userName varchar(255) NOT NULL,
            message_ID int NOT NULL,
            structure blob,
            quality blob,
            likeStat blob,
            dislikeStat blob,
            FOREIGN KEY(userName) REFERENCES users(userName)
            FOREIGN KEY(message_ID) REFERENCES messages(message_ID)
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

        c.execute(f"SELECT * from users WHERE user_ID = (?)", (key, ))

        item = c.fetchall()
        conn.commit()
        conn.close()
        return item

    def lookUpUserName(self, userName):
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
        c.execute("INSERT INTO messages VALUES (?,?,?,?,?)", (new_item[0], new_item[1], new_item[2], new_item[3], new_item[4]))
        #Adding initial ratings, like and dislike counts.
        #The rating system is assumed to be from 0 to 10, so averages are added.
        #Initial like and dislike counts are set to 0.
        StructurefileName = f"Structure{new_item[1]}{new_item[4]}.pkl"
        QualityfileName = f"Quality{new_item[1]}{new_item[4]}.pkl"
        LikeStatfileName = f"LikeStat{new_item[1]}{new_item[4]}.pkl"
        DislikeStatfileName = f"DislikeStat{new_item[1]}{new_item[4]}.pkl"

        StructureData = {}
        QualityData = {}
        LikeStatData = {}
        DislikeStatData = {}

        with open(StructurefileName, "wb") as file1:
            pickle.dump(StructureData, file1)
        with open(QualityfileName, "wb") as file2:
            pickle.dump(QualityData, file2)
        with open(LikeStatfileName, "wb") as file3:
            pickle.dump(LikeStatData, file3)
        with open(DislikeStatfileName, "wb") as file4:
            pickle.dump(DislikeStatData, file4)

        c.execute("INSERT INTO messageRatingData VALUES (?,?,?,?,?,?)",(new_item[1],new_item[4], StructurefileName, QualityfileName, LikeStatfileName, DislikeStatfileName))

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

    def lookUpSpecificSubstring(self, s):
        """
        Returns all the messages containing the specific substring
        :param s: The substring
        :return:
        """
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("SELECT * from messages")
        item = c.fetchall()
        conn.commit()
        conn.close()
        matches = []
        for i in item:
            index = i[3].lower().find(s.lower())
            if index != -1:
                matchItem = i
                matches.append(matchItem)
        return matches

    def updateMessageRating(self, userName, messageID, updaterUserName, structure=None, quality=None, likeStat=None, dislikeStat=None):
        """
        Updates the message ratings for an individual message
        :param userName: The username of the user who posted
        :param messageID: The unique message ID of the post
        :updaterUserName: The username of the user updating the rating
        :param structure: The rating for the structure
        :param quality: The rating for the quality
        :param likeStat: The like count
        :param dislikeStat: The dislike count
        :return:
        """
        inputData = (userName, messageID, structure, quality, likeStat, dislikeStat)
        StructurefileName = f"Structure{userName}{messageID}.pkl"
        QualityfileName = f"Quality{userName}{messageID}.pkl"
        LikeStatfileName = f"LikeStat{userName}{messageID}.pkl"
        DislikeStatfileName = f"DislikeStat{userName}{messageID}.pkl"

        StructureData = {}
        QualityData = {}
        LikeStatData = {}
        DislikeStatData = {}

        with open(StructurefileName, "rb") as file1:
            StructureData = pickle.load(file1)
        with open(QualityfileName, "rb") as file2:
            QualityData = pickle.load(file2)
        with open(LikeStatfileName, "rb") as file3:
            LikeStatData = pickle.load(file3)
        with open(DislikeStatfileName, "rb") as file4:
            DislikeStatData = pickle.load(file4)

        if updaterUserName not in StructureData and structure != None:
            StructureData[updaterUserName] = structure
            with open(StructurefileName, 'wb') as file1:
                pickle.dump(StructureData, file1)

        if updaterUserName not in QualityData and quality != None:
            QualityData[updaterUserName] = quality
            with open(QualityfileName, 'wb') as file2:
                pickle.dump(QualityData, file2)

        if updaterUserName not in LikeStatData and likeStat != None:
            LikeStatData[updaterUserName] = likeStat
            with open(LikeStatfileName, 'wb') as file3:
                pickle.dump(LikeStatData, file3)

        if updaterUserName not in DislikeStatData and dislikeStat != None:
            DislikeStatData[updaterUserName] = dislikeStat
            with open(DislikeStatfileName, 'wb') as file4:
                pickle.dump(DislikeStatData, file4)



        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("""UPDATE messageRatingData SET structure = (?), quality = (?), likeStat = (?), dislikeStat = (?) 
                  WHERE userName = (?) AND message_ID = (?)""", (StructurefileName, QualityfileName, LikeStatfileName, DislikeStatfileName, userName, messageID))
        conn.commit()
        conn.close()

    def getSpecificMessageRatings(self, userName, messageID):
        """
        Returns the ratings for a specific message
        :param userName: The username of the user
        :param messageID: The unique messageID
        :return:
        """
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("SELECT * from messageRatingData WHERE userName = (?) AND message_ID = (?)", (userName, messageID))
        item = c.fetchall()
        returnTuple = (item[0][2], item[0][3], item[0][4], item[0][5])
        StructureData = {}
        QualityData = {}
        LikeStatData = {}
        DislikeStatData = {}

        with open(returnTuple[0], "rb") as file1:
            StructureData = pickle.load(file1)
        with open(returnTuple[1], "rb") as file2:
            QualityData = pickle.load(file2)
        with open(returnTuple[2], "rb") as file3:
            LikeStatData = pickle.load(file3)
        with open(returnTuple[3], "rb") as file4:
            DislikeStatData = pickle.load(file4)

        returnStructureData = 0
        returnQualityData = 0
        returnLikeStatData = 0
        returnDislikeStatData = 0

        for k,v in StructureData.items():
            returnStructureData += float(v)

        for k,v in QualityData.items():
            returnQualityData += float(v)

        for k,v in LikeStatData.items():
            returnLikeStatData += float(v)

        for k,v in DislikeStatData.items():
            returnDislikeStatData += float(v)

        returnStructureData = returnStructureData/len(StructureData)
        returnQualityData = returnQualityData/len(QualityData)


        returnTuple = (returnStructureData, returnQualityData, returnLikeStatData, returnDislikeStatData)
        conn.commit()
        conn.close()
        return returnTuple


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
            c.execute("DELETE from messageRatingData WHERE message_ID = (?)", (messageID,))
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
        c.execute("DROP TABLE messageRatingData")
        conn.commit()
        conn.close()


    def displayTableMessages(self):
        """Display the table"""
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

    def displayTableMessageRatings(self):
        """Display the table"""
        """
        Displays all the message ratings.
        :return: null
        """
        conn = sqlite3.connect('APP.db')
        c = conn.cursor()
        c.execute("SELECT * FROM messageRatingData")
        item = c.fetchall()
        conn.commit()
        conn.close()
        return item






