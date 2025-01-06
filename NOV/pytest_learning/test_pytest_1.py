import allure
import requests
import pytest

@allure.title("First Positive Test Case")
@allure.description("checking creating booking ")
@pytest.mark.shiva
def test_creat_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url+base_path
    headers = {
        "Content-Type": "application/json"
    }
    payload =  {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url=url,headers=headers,json=payload,)
    assert response_data.status_code == 200

    response_json =response_data.json()
    bookingid = response_json["bookingid"]
    print(bookingid)


