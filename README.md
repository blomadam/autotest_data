# autotest_data 
![Tests](https://github.com/blomadam/autotest_data/actions/workflows/tests.yml/badge.svg)


### About
This repository is a sandbox for exploration into several areas:
- First, running automated safety checks on data inputs to ML pipelne using [tox][tox] and [GitHub Actions][GH-A].  
- Second, running a test suite with [pytest][pytest], flake8[flake8], and mypy[mypy].
- Third, experimenting with the [Cookiecutter DS][CCDS] project structure.
- Fourth, learning more about the [AACT][AACT] database of clinical trials.
- Finally, various methods of keeping credentials out of repositories.

The impetus for testing these options out came from a video I recently viewed on YouTube by mCoding (see [here][video]).
Of course once I got started there were multiple concepts I wanted to work with, hence the expanding list of resources above.

### Setup notes for AACT
Cloning this repository provides most of the files required to run the tests.  The data
the tests are based on, however, comes from the Aggregate Analysis of ClinicalTrials.gov 
(AACT) database.  This database hosts data submitted to [ClinicalTrials.gov]() about 
proposed medical trials.  Connecting to this account 
[requires free credentials](https://aact.ctti-clinicaltrials.org/users/sign_up).

To use  your credentials with this repository, copy the `credentials.ini.example` file
that should be copied to `credentials.ini`. Then populate `credentials.ini` with your 
username and password for the AACT database.




###### TODO:
- smooth data flows for updated datasets  based on sql queries
- translate helper functions for modern sci-kit learn Pipelines
- concatenate all data
- build model
- check model - use https://stackoverflow.com/questions/61877496/how-to-ensure-persistent-sklearn-models-on-bit-level
- produce outputs
- more tests (refactor for better code coverage?)
- give clean targets in makefile
- create sphinx documentation



[tox]: https://github.com/tox-dev/tox
[GH-A]: https://docs.github.com/en/actions
[pytest]: https://docs.pytest.org/en/latest/
[flake8]: https://flake8.pycqa.org/en/latest/
[mypy]: https://mypy.readthedocs.io/en/stable/index.html
[CCDS]: https://drivendata.github.io/cookiecutter-data-science/
[AACT]: https://aact.ctti-clinicaltrials.org/
[video]: https://www.youtube.com/watch?v=DhUpxWjOhME
