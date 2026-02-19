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
            email = row.get('email', '').strip()
            password = row.get('password', '').strip()
            product = row.get('product', '').strip()
            if email:
                data.append((email, password, product))
    return data

@pytest.mark.parametrize("email, password, product", get_csv_data())
def test_wipro_capstone_flow(driver, email, password, product):
    driver.get("https://practicesoftwaretesting.com/")
    assert "Practice Software Testing" in driver.title
    shop = ToolShopPage(driver)
    shop.login(email, password)
    shop.search_and_add(product)
    shop.manage_cart()
    shop.logout_user()