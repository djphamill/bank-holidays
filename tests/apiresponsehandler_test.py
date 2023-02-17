import ast
from unittest import TestCase

from apiresponsehandler import APIResponseHandler

class TestAPIResponseHandler(TestCase):
    """
    Tests for methods in the API Response Hanlder
    """

    def test_parse_response_json(self):
        """
        Test to check the response from the API is being parsed correctly.
        """
        with open('tests/data/bank-holidays.json', 'r') as f:
            response_json = f.read()

        with open('tests/data/dates.txt') as f:
            expected_dates = ast.literal_eval(f.read())

        reponsehadler = APIResponseHandler()
        dates = reponsehadler.parse_response_json(response_json)
        self.assertListEqual(dates, expected_dates)