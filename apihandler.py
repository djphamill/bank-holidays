# Class to handle response from API
import datetime
import json 
import requests 

from json import JSONDecodeError

class APIHandler(object):
    """
    Class to handle response from API
    """

    API_ENDPOINT = 'https://www.gov.uk/bank-holidays.json'

    ENGLAND_AND_WALES = 'england-and-wales'
    SCOTLAND = 'scotland'
    NORTHERN_IRELAND = 'northern-ireland'

    NATIONS = [ENGLAND_AND_WALES,
               SCOTLAND,
               NORTHERN_IRELAND]

    EVENTS = 'events'
    DATE = 'date'

    DATE_FORMAT = '%Y-%m-%d'

    RESPONSE_YES = 'yes'
    RESPONSE_NO = 'no'
    RESPONSE_ERROR = 'error'

    def is_it_a_bank_holiday(self):
        """
        Method to run the flow for deciding if it is a bank holiday or not
        """
        try:
            response = self.call_endpoint()
            
            response_json = response.text
            self.validate_response_json(response_json)

            bank_holidays = self.parse_response_json(response_json)

            today= datetime.datetime.today().strftime(self.DATE_FORMAT)
            if today in bank_holidays:
                return True, self.RESPONSE_YES
            else:
                return False, self.RESPONSE_NO
        except:
            return False, self.RESPONSE_ERROR

    def call_endpoint(self):
        """
        Make GET request to API endpoint
        """
        return requests.get(self.API_ENDPOINT)


    def validate_response_json(self, response_json):
        """
        Ensure the API has not changed the format of its json
        """
        try:
            response_dict = json.loads(response_json)
        except JSONDecodeError:
            raise
        
        for key in response_dict.keys():
            if key not in self.NATIONS:
                raise ResponseError


    def parse_response_json(self, repsonse_json):
        """
        Take the response json and return a list of dates that are bank holidays
        """
        bank_holidays_response = json.loads(repsonse_json)
        bank_holiday_dates = []
        for nation in self.NATIONS:
            for event in bank_holidays_response[nation][self.EVENTS]:
                bank_holiday_dates.append(event[self.DATE])
        
        return bank_holiday_dates

class ResponseError(Exception):
    """
    Class for handling response errors
    """
    