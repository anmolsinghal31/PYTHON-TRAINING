import pytest
import csv
import os
from pages.toolshop_page import ToolShopPage

def get_csv_data():
    data = []
    path = os.path.join(os.getcwd(), 'test_data.csv')
    with open(path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Forcibly strip spaces from both Keys and Values
            email = row.get('email', '').strip()
            password = row.get('password', '').strip()
            product = row.get('product', '').strip()
            if email:
                data.append((email, password, product))
    return data

@pytest.mark.parametrize("email, password, product", get_csv_data())
def test_wipro_capstone_flow(driver, email, password, product):
    driver.get("https://practicesoftwaretesting.com/")
    shop = ToolShopPage(driver)

    # Added explicit synchronization to prevent TimeoutException
    shop.login(email, password)
    shop.search_and_add(product)
    shop.manage_cart()
    shop.logout_user()

#COMMAND TO RUN THIS -  $dt = Get-Date -Format "yyyy-MM-dd_HH-mm"; $env:PYTHONPATH="."; pytest tests/test_csv_driven.py -v -s --html="results/Pytest_Capstone_Report_$dt.html" --self-contained-html