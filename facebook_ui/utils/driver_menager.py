import os
from selenium import webdriver
from facebook_ui.utils import constants as const
from selenium.webdriver.chrome.options import Options

_DRIVER_INSTANCE = None

ROOT_PATH = "{}".format(os.path.dirname(os.path.abspath(os.path.join(__file__, ".."))))
PATH = "{}\\drivers".format(ROOT_PATH)


def get_driver(browser: const.Browser = const.Browser.CHROME,
               implicitly_wait: int = 15,
               path: str = None):
    """
    Get needed webdriver

    :param browser: Browser to start
    :param implicitly_wait: Time of implicit wait in seconds
    :param path: Path to driver executables
    :return: Instance of webdriver
    """
    global _DRIVER_INSTANCE

    if path is None:
        path = PATH

    if not _DRIVER_INSTANCE:

        if browser == const.Browser.CHROME:
            opts = Options()
            opts.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

            _DRIVER_INSTANCE = webdriver.Chrome(executable_path="{}\\{}".format(path, "chromedriver.exe"),
                                                chrome_options=opts)

        if browser == const.Browser.INTERNET_EXPLORER:
            _DRIVER_INSTANCE = webdriver.Ie(executable_path="{}\\{}".format(path, "IEDriverServer.exe"))

    _DRIVER_INSTANCE.implicitly_wait(implicitly_wait)
    return _DRIVER_INSTANCE


def close_driver():
    """
    Close existing instance of webdriver
    """
    global _DRIVER_INSTANCE
    if _DRIVER_INSTANCE:
        _DRIVER_INSTANCE.quit()
        _DRIVER_INSTANCE = None
