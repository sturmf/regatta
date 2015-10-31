regatta
=======

A simple sailing race scoring program

[![Build Status](https://travis-ci.org/sturmf/regatta.svg?branch=master)](https://travis-ci.org/sturmf/regatta)
[![Coverage Status](https://coveralls.io/repos/sturmf/regatta/badge.svg?branch=master&service=github)](https://coveralls.io/github/sturmf/regatta?branch=master)

This program is just begining its development, so don't expect a working version any time soon.

The main goal of this project is to learn about the state of the art development tools and workflows while still producing something usefull.

This means especially using the following:

* Distributed version control (GitHub.com)
* Continues integration (Travis-CI)
* Test coverage (Coveralls.io)
* Code review (GerritHub.io)
* Planing and issue tracking (JIRA Software)
* Documentation (JIRA Confluence)


# Contributions from non team members

Feel free to clone the repository on github and submit a pull request. In that case we will create a gerrit review on your behalf. 
Or directly push to gerrit. (FIXME: describe)


# Contributions from team members

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


