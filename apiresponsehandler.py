# Class to handle response from API
import json 

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
