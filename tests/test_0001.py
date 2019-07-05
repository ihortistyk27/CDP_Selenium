from facebook_ui.pages.login_page import LoginPage
from facebook_ui.utils.constants import Title
from tests.execution_utils.config_loader import Config

cfg = Config()


def test_0001(init_driver):
    """
    Verify that we can successfully login to Facebook.
    """
    login_page = LoginPage(init_driver, base_url=cfg.url('facebook')).open()
    home_page = login_page.login(cfg.credentials('email'), cfg.credentials('password'))
    assert home_page.get_title() == Title.FACEBOOK_HOME
