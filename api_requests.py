import requests
import json

# get countries from API request


def get_countries():
    # API address
    api_address = 'https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries'
    # get countries using API
    json_data = requests.get(api_address).json()
    countries = json_data['body']

    return countries

# get the capital of the country


def get_capital(country):
    # API address
    api_address = 'https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCapital'
    # get capital of the country using API
    json_data = requests.post(api_address, json.dumps({'country': country})).json()
    capital = json_data['body']['capital']

    return capital

# get the population of the country


def get_population(country):
    # API address
    api_address = 'https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getPopulation'
    # get capital of the country using API
    json_data = requests.post(api_address, json.dumps({'country': country})).json()
    population = json_data['body']['population']

    return population






