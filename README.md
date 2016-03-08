regatta
=======

A simple sailing race scoring program.

[![Build Status](https://travis-ci.org/sturmf/regatta.svg?branch=master)](https://travis-ci.org/sturmf/regatta)
[![Coverage Status](https://coveralls.io/repos/sturmf/regatta/badge.svg?branch=master&service=github)](https://coveralls.io/github/sturmf/regatta?branch=master)
[![Code Health](https://landscape.io/github/sturmf/regatta/master/landscape.svg?style=flat)](https://landscape.io/github/sturmf/regatta/master)
[Reviews](http://reviewboard.rtfs.org/)

This program is just beginning its development, so don't expect a working version any time soon.

The main goal of this project is to learn about the state of the art development tools and workflows while still producing something useful.

This means especially using the following:

* Distributed version control ([GitHub.com](https://github.com)) [https://github.com/sturmf/regatta](https://github.com/sturmf/regatta)
* Continous integration ([Travis-CI](https://travis-ci.org)) [https://travis-ci.org/sturmf/regatta](https://travis-ci.org/sturmf/regatta)
* Test coverage ([Coveralls.io](https://coveralls.io)) [https://coveralls.io/github/sturmf/regatta](https://coveralls.io/github/sturmf/regatta)
* Code review ([ReviewBoard](https://www.reviewboard.org)) [http://reviewboard.rtfs.org](http://reviewboard.rtfs.org)
* Code smells ([Landscape.io](https://landscape.io)) [https://landscape.io/github/sturmf/regatta/](https://landscape.io/github/sturmf/regatta/)
* Style guide checking ([flake8](https://pypi.python.org/pypi/flake8)) this combines [PEP 0008](https://www.python.org/dev/peps/pep-0008) and [pyflakes](https://pypi.python.org/pypi/pyflakes)
* Planing and issue tracking ([JIRA Software](https://www.atlassian.com/software/jira)) [https://regatta.atlassian.net](https://regatta.atlassian.net)
* Documentation ([JIRA Confluence](https://www.atlassian.com/software/confluence)) [https://regatta.atlassian.net/wiki](https://regatta.atlassian.net/wiki)


# Running the program

To run the program execute

    cd regatta && python3 main.py

To run the style guide checks run

    flake8 regatta

To run the tests execute

    python3 setup.py test

or

    PYTHONPATH=. py.test-3

To create the documentation run

    python3 setup.py build_sphinx

or

    cd docs && make html


# Contributions from non team members

Feel free to clone the repository on github and submit a pull request. You can also create a reviewboard review request which we will try to complete asap.


