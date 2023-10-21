import unittest
from unittest.mock import MagicMock, patch
from user_logic.login import (verify_password, login, do_login, logout)
from user_logic.signin import (
    encrypt_password, is_user_id_unique, generate_unique_user_id,
    username_available, save_user, signup
)


class TestUserLogicFunctions(unittest.TestCase):
    @patch('user_logic.dataHandler')
    def test_verify_password(self, mock_dataHandler):
        # Mock user details
        user_details = [('username', 'salthashedpassword')]

        # Mock dataHandler.lookUpUserName to return the mock user details
        mock_dataHandler.lookUpUserName.return_value = user_details

        # Correct password
        self.assertTrue(verify_password('salthashedpassword', 'password'))

        # Incorrect password
        self.assertFalse(verify_password('salthashedpassword', 'wrongpassword'))

    @patch('user_logic.request')
    @patch('user_logic.redirect')
    def test_do_login(self, mock_request, mock_redirect):
        mock_request.forms.get.side_effect = ['username', 'password']

        with patch('user_logic.login') as mock_login:
            mock_login.return_value = True
            session_data = {}
            do_login(session_data)
            self.assertEqual(session_data['user'], 'username')
            mock_redirect.assert_called_with('/')

            mock_login.return_value = False
            result = do_login(session_data)
            self.assertEqual(result, "Login failed. <a href='/login'>Try again</a>")

    def test_logout(self):
        session_data = {'user': 'username'}
        logout(session_data)
        self.assertNotIn('user', session_data)

class TestUserFunctions(unittest.TestCase):
    @patch('your_module.dataHandler')
    def test_encrypt_password(self, mock_dataHandler):
        # Mock dataHandler
        mock_dataHandler.lookUpUserID.return_value = []  # No user with the given user_id

        # Test encrypting a password
        encrypted_password = encrypt_password('mypassword')
        self.assertIsInstance(encrypted_password, str)

    @patch('your_module.dataHandler')
    def test_is_user_id_unique(self, mock_dataHandler):
        # Mock dataHandler
        mock_dataHandler.lookUpUserID.return_value = []  # No user with the given user_id

        # User ID is unique
        self.assertTrue(is_user_id_unique('unique_id'))

        # User ID already exists
        mock_dataHandler.lookUpUserID.return_value = [('user_id', 'username', 'password_hash')]
        self.assertFalse(is_user_id_unique('user_id'))

    def test_generate_unique_user_id(self):
        # Test generating a unique user ID
        unique_user_id = generate_unique_user_id()
        self.assertIsInstance(unique_user_id, str)

    @patch('your_module.dataHandler')
    def test_username_available(self, mock_dataHandler):
        # Mock dataHandler
        mock_dataHandler.lookUpUserName.return_value = []  # No user with the given username

        # Username is available
        self.assertTrue(username_available('unique_username'))

        # Username already exists
        mock_dataHandler.lookUpUserName.return_value = [('user_id', 'username', 'password_hash')]
        self.assertFalse(username_available('username'))

    @patch('your_module.dataHandler')
    @patch('your_module.redirect')
    def test_signup(self, mock_dataHandler, mock_redirect):
        # Mock dataHandler
        mock_dataHandler.lookUpUserName.return_value = []  # No user with the given username

        # Mock request.forms.get
        with patch('your_module.request.forms.get') as mock_get:
            mock_get.side_effect = ['username', 'password', 'password', 'retype-password']

            # Test signing up
            session_data = {}
            result = signup(session_data)
            self.assertEqual(session_data['user'], 'username')
            self.assertEqual(result, None)
            mock_redirect.assert_called_with('/')

            # Test non-matching passwords
            mock_get.side_effect = ['username', 'password', 'wrongpassword', 'retype-password']
            result = signup(session_data)
            self.assertNotIn('user', session_data)
            self.assertIn("Password and retype password do not match", result)

            # Test username not available
            mock_get.side_effect = ['username', 'password', 'password', 'retype-password']
            mock_dataHandler.lookUpUserName.return_value = [('user_id', 'username', 'password_hash')]
            result = signup(session_data)
            self.assertNotIn('user', session_data)
            self.assertIn("Username already in use", result)

if __name__ == '__main__':
    unittest.main()
