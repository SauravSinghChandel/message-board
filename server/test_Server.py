from unittest import TestCase
import unittest
from Server import do_login, logout

class serverTest(TestCase):
    def test_do_login(self):
        session_data = {}
        result = do_login(session_data)

        assert session_data['user'] == 'test_user'

    def test_logout(self):
        session_data = {'user': 'test_user'}
        logout(session_data)
        assert 'user' not in session_data


if __name__ == '__main__':
    unittest.main()
