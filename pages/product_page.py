from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        # self.should_be_button_add_to_basket()
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()
        self.check_name_product()
        self.check_price_product()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button 'Add to basket' is not " \
                                                                                   "presented"

    def check_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_in_message = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE).text
        assert name_product == name_product_in_message, "Названия товаров не совпадают"

    def check_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_product_in_message = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_THE_MESSAGE).text
        assert price_product == price_product_in_message, "Цены товаров не совпадают"
