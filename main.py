from multiprocessing import freeze_support

import pytest
import os
dir_path = os.getcwd()

pytest_args = ["C:\CDP_Selenium\\tests",
               "--disable-pytest-warnings",
               "-vv",
               "--alluredir", dir_path + "\\report\\allure-results"
               ]

pytest.main(pytest_args)
