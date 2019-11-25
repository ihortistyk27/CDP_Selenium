import pytest
import facebook_ui.utils.driver_menager as dm
from tests.execution_utils.config_loader import Config as Properties


Properties.initialize('config.ini')


# @pytest.yield_fixture(scope="session")
@pytest.fixture
def init_driver():
    driver = dm.get_driver()
    driver.maximize_window()
    yield driver
    dm.close_driver()
