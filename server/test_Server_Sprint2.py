import unittest
from unittest import TestCase
from Server import add_post, search_results


class serverTest(TestCase):
    def test_add_post(self):
        session_data = {}
        result = add_post(session_data)

        assert session_data['user'] == 'test_user'

    def test_search_results(self):
        session_data = {'user': 'test_user'}
        search_results(session_data)
        assert 'user' not in session_data

if __name__ == '__main__':
    unittest.main()
