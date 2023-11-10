import unittest
from unittest import TestCase
from Server import search, ratings


class serverTest(TestCase):
    def test_search(self):
        session_data = {}
        result = search(session_data)

        assert session_data['user'] == 'test_user'

    def test_ratings(self):
        session_data = {'user': 'test_user'}
        ratings(session_data)
        assert 'user' not in session_data

if __name__ == '__main__':
    unittest.main()
