from dataHandler import dataBaseHandler
from unittest import TestCase

class TestUserStorage(TestCase):
    def setUp(self):
        self.handler = dataBaseHandler()

    def tearDown(self):
        self.handler.removeUser("10")

    def test_addUser(self):
        user = (10, "John", "12345")
        self.handler.addUser(user)
        self.assertEqual(self.handler.lookUpUserID(user[0])[0], user)

    def test_lookUpUserID(self):
        user = (10, "John", "12345")
        self.handler.addUser(user)
        self.assertEqual(self.handler.lookUpUserID(user[0])[0], user)

    def test_lookUpUserName(self):
        user = (10, "John", "12345")
        self.handler.addUser(user)
        self.assertEqual(self.handler.lookUpUserName(user[1])[0], user)

    def test_removeUser(self):
        user = (10, "John", "12345")
        self.handler.addUser(user)
        self.handler.removeUser(user[0])
        with self.assertRaises(IndexError):
            self.assertNotEqual(self.handler.lookUpUserName(user[1])[0], user)

class TestMessageStorage(TestCase):
    def setUp(self):
        self.handler = dataBaseHandler()
        user = (11, "Johnny", "12345")
        self.handler.addUser(user)
        message = ("21-02-2023 17:42", "Johnny", "Hello", "1")
        self.handler.addMessage(message)

    def tearDown(self):
        user = (11, "Johnny", "12345")
        message = ("21-02-2023 17:42", "Johnny", "Hello", "1")
        self.handler.deleteMessage(message[1], message[3])
        self.handler.removeUser(str(user[0]))

    def test_addMessage(self):
        user = (11, "Johnny", "12345")
        message = ("21-02-2023 17:42", "Johnny", "Hello", 1)
        self.assertEqual(self.handler.lookUpSpecificMessage(user[1], message[3])[0], message)

    def test_deleteMessage(self):
        user = (11, "Johnny", "12345")
        message = ("21-02-2023 17:42", "Johnny", "Hello", 1)
        self.handler.addMessage(message)
        self.handler.deleteMessage(message[1], message[3])
        with self.assertRaises(IndexError):
            self.assertNotEqual(self.handler.lookUpSpecificMessage(user[1], message[3])[0], message)




if '__name__' == '__main__':
    unittest.main()