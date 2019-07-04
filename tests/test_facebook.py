from facebook_ui.utils.driver_menager import get_driver, close_driver
from facebook_ui.pages.login_page import LoginPage

# passw = os.environ['facebook_psswd']

driver = get_driver()
driver.maximize_window()

login_page = LoginPage(driver, "https://www.facebook.com").open()
home_page = login_page.login('tistuk@mail.ru', '270589IHOR')
home_page.log_out()

close_driver()
