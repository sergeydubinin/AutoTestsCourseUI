from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.check_button_add_to_basket()
        self.solve_quiz_and_get_code()
        self.check_name_product()
        self.check_price_product()

    def check_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button 'Add to basket' is not " \
                                                                                   "presented"
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def check_name_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "Element 'Name product' is not " \
                                                                                   "presented"
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_in_message = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE).text
        assert name_product == name_product_in_message, "Product names do not match"

    def check_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Element 'Price product' is not " \
                                                                           "presented"
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_product_in_message = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_THE_MESSAGE).text
        assert price_product == price_product_in_message, "Product prices do not match"
