from flask import Flask, request
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)

DETECT_BASE_URL = os.getenv('DETECT_BASE_URL')
TRANSLATE_BASE_URL = os.getenv('TRANSLATE_BASE_URL')
HEADERS = {
    'x-rapidapi-host': os.getenv('RAPID_API_HOST'),
    'x-rapidapi-key': os.getenv('API_KEY'),
    'content-type': "application/x-www-form-urlencoded"
}


@app.route('/')
def health_check():
    return 'Translation Service is up.'


@app.route('/detect', methods=['POST'])
def detect():
    # parse args
    text = request.form.get('text')

    # url encode text
    long_list_of_words = text.split(' ')
    url_encoded_text = f"q={'%20'.join(long_list_of_words)}"

    payload = url_encoded_text

    # make the request
    r = requests.post(DETECT_BASE_URL, data=payload, headers=HEADERS)

    return r.json()


@app.route('/translate', methods=['POST'])
def translate():
    # parse args
    text = request.form.get('text')
    target = request.form.get('target')

    # url encode text
    long_list_of_words = text.split(' ')
    url_encoded_text = f"q={'%20'.join(long_list_of_words)}&target={target}"
    payload = url_encoded_text

    r = requests.post(TRANSLATE_BASE_URL, data=payload, headers=HEADERS)

    return r.json()


if __name__ == '__main__':
    app.run(debug=True)
