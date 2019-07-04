"""
Module for holding Home page functionality
"""

from selenium.webdriver.common.by import By
from facebook_ui.pages import base_page


class HomePage(base_page.BasePage):
    """
    Class represents Home page
    """
    _home_menu = (By.ID, 'mainContainer')

    @property
    def loaded(self):
        """
        Property to verify if page has been loaded

        :return: True if page is loaded, False otherwise
        """
        return self.find_element(*self._home_menu).is_displayed()

    def open(self):
        """
        Waits for Main page to open. Overrides BasePage 'open' method,
        instead of opening page by URL we just wait for it to load

        :return: MainPage page object
        """
        self.wait.until(lambda x: self.loaded)
        return self
