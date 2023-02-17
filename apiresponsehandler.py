# Class to handle response from API
import json 

from json import JSONDecodeError

class APIResponseHandler(object):
    """
    Class to handle response from API
    """

    ENGLAND_AND_WALES = 'england-and-wales'
    SCOTLAND = 'scotland'
    NORTHERN_IRELAND = 'northern-ireland'

    NATIONS = [ENGLAND_AND_WALES,
               SCOTLAND,
               NORTHERN_IRELAND]

    EVENTS = 'events'
    DATE = 'date'

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
    