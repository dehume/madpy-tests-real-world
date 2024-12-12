import requests

API_URL = "https://cat-fact.herokuapp.com/facts"


def get_cat_facts():
    output = []
    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        for data in response.json():
            output.append(data.get("text"))

        return output

    except requests.exceptions.RequestException as err:
        print(f"Sorry no cats: {err}")
        return output
