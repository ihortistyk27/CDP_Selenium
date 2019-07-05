from pypom import Page
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from facebook_ui.pages import home_page


class LoginPage(Page):
    _email_field = (By.ID, 'email')
    _password_field = (By.NAME, 'pass')
    _login_button = (By.ID, 'loginbutton')

    def __init__(self, driver, base_url=None, **url_kwargs):

        if base_url is not None:
            if not base_url.startswith("http"):
                base_url = "https://{}".format(base_url)
            super().__init__(driver, timeout=60, base_url=base_url, **url_kwargs)

    def open(self):
        """
        Open the login page

        :return: Login page object
        """
        super().open()
        self.driver.switch_to.default_content()
        return self

    def login(self, email: str, password: str):
        """
        Login to Facebook by typing email and password values into
        input fields and clicking 'Log in" button.

        :param email: Email used for log in
        :param password: User password
        :return: HomePage page object

        :Example:

        .. code-block:: python

            from utils import driver_manager
            from pages.login_page import LoginPage

            driver = driver_manager.get_driver()
            login_page = LoginPage(driver, base_url=HOST).open()
            home_page = login_page.login(EMAIL, PASSWORD)
        """

        self.find_element(*self._email_field).send_keys(email)
        self.find_element(*self._password_field).send_keys(password)
        self.find_element(*self._login_button).send_keys("\n")

        try:
            page = home_page.HomePage(self.driver).open()
            return page
        except TimeoutException:
            raise "Could not login with the following email '{}' and password '{}'.".format(email, password)
