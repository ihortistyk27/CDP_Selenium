import pytest

from facebook_ui.pages.login_page import LoginPage
from tests.execution_utils.config_loader import Config

cfg = Config()


@pytest.mark.dependency(depends=["test_0001"])
def test_0002(init_driver):
    """
    Verify that we can successfully log out from Facebook.
    """
    login_page = LoginPage(init_driver, base_url=cfg.url('facebook')).open()
    home_page = login_page.login(cfg.credentials('email'), cfg.credentials('password'))
    assert home_page.loaded
    login_page = home_page.log_out()
    assert login_page.loaded
