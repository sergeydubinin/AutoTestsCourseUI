import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize("value_link", ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", "offer7",
                                        "offer8", "offer9"])
def test_add_product_to_basket(browser, value_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={value_link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
