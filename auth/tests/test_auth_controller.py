import unittest
from auth.controller import AuthController


class AuthControllerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.auth = AuthController()

    def test_generate_token(self):
        data_to_encode = {"data": "42"}
        token = self.auth.generate_token(data_to_encode)
        data_decoded = self.auth.verify_token(token)
        self.assertEqual(list(data_decoded.keys()), ['data', 'exp'])
        self.assertEqual(data_decoded['data'], data_to_encode['data'])