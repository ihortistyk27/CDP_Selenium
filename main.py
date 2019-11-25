from multiprocessing import freeze_support

import pytest

pytest_args = ["C:\CDP_Selenium\\tests",
               "--disable-pytest-warnings",
               "-vv"]
#               "--tests-per-worker=2"]

pytest.main(pytest_args)
