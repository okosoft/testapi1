import requests
import allure
import pytest

@allure.feature('API Tests')
@allure.story('Test API Response')
@allure.title("Verify API returns status 200 and response 'ok'")
def test_api_response():
    # Define the API endpoint
    url = "https://dog.ceo/api/breeds/image/random"  # Replace with your actual API endpoint

    # Send a GET request with the parameter
    response = requests.get(url)

    print(response)

    # Check if the status code is 200
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    # Check if the returned value is 'ok'
    json_response = response.json()  # Assuming the response is in JSON format
    assert json_response.get('status') == 'success', f"Expected 'ok' but got {json_response.get('value')}"

test_api_response()