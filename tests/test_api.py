from unittest.mock import patch, Mock
import requests
import json
import pytest

from app.api import get_cat_facts, API_URL


@pytest.fixture()
def mock_cat_api_response_data():
    with open("tests/data/cats.json", "r") as data:
        return json.load(data)


# Blocked by conftest.py
# def test_get_cat_facts_network():
#     result = get_cat_facts()


@patch("requests.get")
def test_get_cat_facts(mock_get, mock_cat_api_response_data):
    # Mock response data
    mock_response = Mock()
    mock_response.json.return_value = mock_cat_api_response_data
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Call the function
    result = get_cat_facts()

    # Assertions
    assert len(result) == 5
    assert (
        result[0]
        == "Owning a cat can reduce the risk of stroke and heart attack by a third."
    )
    mock_get.assert_called_once_with(API_URL)


@patch("requests.get")
def test_get_cat_facts_status_code_error(mock_get):
    # Configure the mock to return a failed response
    mock_get.return_value.status_code = 404

    # Call the function
    facts = get_cat_facts()

    # Assert the function returns an empty list on failure
    assert facts == []
    mock_get.assert_called_once_with(API_URL)


@patch("requests.get")
def test_get_cat_facts_api_error(mock_get):
    # Simulate an HTTPError
    mock_get.side_effect = requests.exceptions.HTTPError(
        "404 Client Error: Not Found for url"
    )

    # Call the function
    facts = get_cat_facts()

    # Assert the function returns an empty list on failure
    assert facts == []
    mock_get.assert_called_once_with(API_URL)
