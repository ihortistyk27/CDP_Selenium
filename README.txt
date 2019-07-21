###########
To run tests with dependencies use the following fixture >>  @pytest.mark.dependency(), if it doesn't work then you
need to install this plugin "pip install pytest-dependency".
link to documentation >> https://pytest-dependency.readthedocs.io/en/latest/usage.html

############
To run tests in the appropriate order use the following fixture >>  @pytest.mark.run(order=1), if it doesn't work
then you need to install this plugin "pytest-ordering".
pip install pytest-ordering
link to documentation >> https://pytest-ordering.readthedocs.io/en/develop/index.html

############
For the parallel run you should install this plugin 'pip install pytest-xdist', then add "-n number_of_parallel_run"
to pytest.main() as argument.
link to documentation >> https://pypi.org/project/pytest-parallel/