import ast
from json import JSONDecodeError
from parameterized import parameterized
from unittest import TestCase

from apiresponsehandler import APIResponseHandler, ResponseError


class TestAPIResponseHandler(TestCase):
    """
    Tests for methods in the API Response Hanlder
    """

    def setUp(self):
        self.repsonseHandler = APIResponseHandler()

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
    
    @parameterized.expand([
        ("not josn format", "hello", JSONDecodeError),
        ("doesn't start with nation", "{'dates': [2020-01-01, 2021-01-01]}", ResponseError),
        ("dates are of the wrong format", "{'england-and-wales':{'division':'england-and-wales', 'events':[{'dates':'01-01-2020'}]}}", ResponseError)
    ])
    def test_validate_respone_json_raises_exception(self, _, response_json, exception):
        """
        Test that the validator for the response json
        """
        self.assertRaises(exception, self.repsonseHandler.validate_response_json,
                                         response_json)