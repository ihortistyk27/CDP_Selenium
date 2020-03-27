from multiprocessing import freeze_support

import pytest

pytest_args = ["C:\CDP_Selenium\\tests",
               "--disable-pytest-warnings",
               "-vv",
               "--alluredir", "/allure-report"]

pytest.main(pytest_args)
