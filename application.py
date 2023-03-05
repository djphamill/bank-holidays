from flask import Flask

from apihandler import APIHandler

app = Flask(__name__)

@app.route("/")
def is_it_a_bank_holiday():
    api_handler = APIHandler()
    _, answer = api_handler.is_it_a_bank_holiday()
    return "<head><title>Bank Holiday?</title></head><p>" + answer + "</p>"