import ast
from json import JSONDecodeError, loads
from parameterized import parameterized
from unittest import TestCase
from freezegun import freeze_time

from apihandler import APIHandler, ResponseError


class TestAPIResponseHandler(TestCase):
    """
    Tests for methods in the API Response Hanlder
    """

    GOOD_FRIDAY = '2022-04-15'
    EASTER_SUNDAY = '2022-04-16'

    def setUp(self):
        self.api_handler = APIHandler()

    def test_parse_response_json(self):
        """
        Test to check the response from the API is being parsed correctly.
        """
        with open('tests/data/bank-holidays.json', 'r') as f:
            response_json = f.read()

        with open('tests/data/dates.txt') as f:
            expected_dates = ast.literal_eval(f.read())

        dates = self.api_handler.parse_response_json(response_json)
        self.assertListEqual(dates, expected_dates)
    
    @parameterized.expand([
        ("not josn format", 'hello', JSONDecodeError),
        ("doesn't start with nation", '{"dates":["2020-01-01","2021-01-01"]}', ResponseError),
        ("dates are of the wrong format", '{"england-and-wales":{"division":"england-and-wales"}, "events":[{"dates":"01-01-2020"}]}', ResponseError)
    ])
    def test_validate_respone_json_raises_exception(self, _, response_json, exception):
        """
        Test that the validator for the response json
        """
        self.assertRaises(exception, self.api_handler.validate_response_json,
                                         response_json)
        
    
    def test_call_endpoint_returns_200(self):
        """
        Test the call_endpoint method returns a 400 response
        """
        response = self.api_handler.call_endpoint()
        self.assertEqual(response.status_code, 200)

    def test_api_handlers_endpoint(self):
        """
        Test the end point has not changed
        """
        expected_endpoint =  "https://www.gov.uk/bank-holidays.json"
        self.assertEqual(self.api_handler.API_ENDPOINT, expected_endpoint)

    def test_call_endpoint_returns_json_content(self):
        """
        Test the call_endpoint methods returns json in its body
        """
        response = self.api_handler.call_endpoint()
        try:
            loads(response.text)
        except ValueError:
            self.fail("Response returned text that was not JSON")

    @freeze_time(GOOD_FRIDAY)
    def test_is_it_a_bank_holiday_good_friday(self):
        """
        Test the is_it_a_bank_holiday method for Good Friday
        """
        sucess, answer = self.api_handler.is_it_a_bank_holiday()
        self.assertTrue(sucess)
        self.assertEqual(answer, 'yes')

    @freeze_time(EASTER_SUNDAY)
    def test_is_it_a_bank_holiday_easter_sunday(self):
        """
        Test the is_it_a_bank_holiday method for Easter Sunday
        """
        success, answer = self.api_handler.is_it_a_bank_holiday()
        self.assertTrue(success)
        self.assertEqual(answer, 'no')
