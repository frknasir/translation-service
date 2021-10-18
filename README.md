# About

Translation Service With Google Translation API

## What is needed

- RapidAPI Account
- Pipenv (Virtual Environment)
- Flask (Web Framework)

## Steps to run

- From the terminal, run: `git clone git@github.com:frknasir/translation-service.git`
- cd into the project directory
- From the project directory, run: `pipenv install`
- provide the RAPIDAPI credentials in the `.env` file cc [Google Translation API](https://rapidapi.com/googlecloud/api/google-translate1)
- run: `pipenv run python3 translation_service.py`
- done!

## Endpoints

1. `/` - health check
2. `/detect` - language detection route (required param: text)
3. `/translate` - language translation route (required param: text & target e.g ha, yo, ig)
