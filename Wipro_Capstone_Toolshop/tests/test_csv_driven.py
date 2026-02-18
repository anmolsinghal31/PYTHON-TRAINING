import pytest
import csv
import os
from pages.toolshop_page import ToolShopPage


def get_csv_data():
    data = []
    # Using pytest_data.csv as we discussed
    path = os.path.join(os.getcwd(), 'test_data.csv')
    with open(path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Strip spaces to prevent "KeyError"
            clean_row = {k.strip(): v for k, v in row.items()}
            data.append((clean_row['email'], clean_row['password'], clean_row['product']))
    return data


@pytest.mark.parametrize("email, password, product", get_csv_data())
def test_wipro_capstone_flow(driver, email, password, product):
    driver.get("https://practicesoftwaretesting.com/")
    shop = ToolShopPage(driver)

    # These steps now contain internal assertions
    shop.login(email, password)
    shop.search_and_add(product)
    shop.manage_cart()
    shop.logout_user()

#COMMAND TO RUN THIS -  $env:PYTHONPATH="."; python -m pytest tests/test_csv_driven.py -v -s