"""
Module for holding base page functionality
"""

from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec


class BasePage(Page):
    """
    Class holds BasePage functionality and should be used as parent class for all page objects
    """

    _page_title = (By.XPATH, "//div[@class='_4kny'] //*[@title='Go to Facebook Home']")
    _account_settings = (By.CSS_SELECTOR, "#userNavigationLabel")
    _log_out = (By.XPATH, "//span[@class='_54nh'][contains(.,'Log Out')]")

    @property
    def home_page(self):
        """
        Computers menu

        :return: Home Page object
        """
        from facebook_ui.pages.home_page import HomePage
        return HomePage(self.driver)

    def find_element(self, strategy: By, locator: str) -> WebElement:
        """
        Find web element. Overriding parent method to add return type annotation

        :param strategy: Location strategy (e.g. By.ID)
        :param locator: Location locator (e.g. 'save_button')
        :return: WebElement
        """
        return super().find_element(strategy, locator)

    def get_title(self) -> str:
        """
        Get page title

        :return: Page title
        """
        return self.find_element(*self._page_title).text

    def log_out(self):
        """
        Click on "Log out" button

        :return: Login Page
        """
        from facebook_ui.pages.login_page import LoginPage
        self.find_element(*self._account_settings).click()
        self.wait.until(ec.presence_of_element_located(self._log_out))
        self.find_element(*self._log_out).click()
        return LoginPage(self.driver)
