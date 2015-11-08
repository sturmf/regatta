regatta
=======

A simple sailing race scoring program.

[![Build Status](https://travis-ci.org/sturmf/regatta.svg?branch=master)](https://travis-ci.org/sturmf/regatta)
[![Coverage Status](https://coveralls.io/repos/sturmf/regatta/badge.svg?branch=master&service=github)](https://coveralls.io/github/sturmf/regatta?branch=master)
[Reviews](http://reviewboard.rtfs.org/)

This program is just begining its development, so don't expect a working version any time soon.

The main goal of this project is to learn about the state of the art development tools and workflows while still producing something useful.

This means especially using the following:

* Distributed version control ([GitHub.com](https://github.com)) [https://github.com/sturmf/regatta](https://github.com/sturmf/regatta)
* Continues integration ([Travis-CI](https://travis-ci.org)) [https://travis-ci.org/sturmf/regatta](https://travis-ci.org/sturmf/regatta)
* Test coverage ([Coveralls.io](https://coveralls.io)) [https://coveralls.io/github/sturmf/regatta](https://coveralls.io/github/sturmf/regatta)
* Code review ([ReviewBoard](https://www.reviewboard.org)) [http://reviewboard.rtfs.org](http://reviewboard.rtfs.org)
* Code review ([GerritHub.io](http://gerrithub.io)) [https://review.gerrithub.io](https://review.gerrithub.io/#/admin/projects/sturmf/regatta,dashboards)
* Planing and issue tracking ([JIRA Software](https://www.atlassian.com/software/jira)) [https://regatta.atlassian.net](https://regatta.atlassian.net)
* Documentation ([JIRA Confluence](https://www.atlassian.com/software/confluence)) [https://regatta.atlassian.net/wiki](https://regatta.atlassian.net/wiki)

The following tools are still open and not integrated 
* Style guide checking ([flake8](https://pypi.python.org/pypi/flake8)) this seems to combine pep8 and pyflakes
* Style guide checking ([PEP 0008](https://www.python.org/dev/peps/pep-0008))
* Style guide checking ([pyflakes](https://pypi.python.org/pypi/pyflakes))
* Style guide and code checker ([Pylint](http://www.pylint.org))

# Contributions from non team members

Feel free to clone the repository on github and submit a pull request. In that case we will create a gerrit review on your behalf. 
Or directly push to gerrit. (FIXME: describe)


# Contributions from team members (using gerrit)

Since we use gerrit for code review you need to do the following steps to be able to submit a change.

- Clone the source from GitHub.com

  clone git@github.com:sturmf/regatta.git

- Add gerrit as remote (replace user with your username)

  git remote add gerrit ssh://user@review.gerrithub.io:29418/sturmf/regatta

- Add the commit-msg git hook

  curl -Lo .git/hooks/commit-msg http://review.gerrithub.io/tools/hooks/commit-msg
  
  chmod a+x .git/hooks/commit-msg

Now you are ready to create a new new branch and commit on that.

- Create new branch to work on (replace newbranch with your branchname)

  git checkout -b newbranch

- Whenever you are done, squash all commits and submit you change for review
(replace newbranch with your branchname)

  FIXME: squash command
  
  git commit
  
  git push gerrit HEAD:refs/for/newbranch

If you want to update a change, edit your source and commmit the changes with the --amend option leaving the Change-Id intact.

- Resubmit a change (replace newbranch with your branchname)

  git commit --amend
  
  git push gerrit HEAD:refs/for/newbranch


