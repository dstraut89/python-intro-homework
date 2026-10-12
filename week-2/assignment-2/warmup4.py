# The error that I hit this week was this:
# $ git commit -m "add warmup2.py"
# On branch main
# Your branch is up to date with 'origin/main'.
#
# Untracked files:
#  (use "git add <file>..." to include in what will be committed)
#        warmup3.py
#
# nothing added to commit but untracked files present (use "git add" to track)
#
#
# What cause it was that I hadn't pushed yet, I was trying to gather all my files first.
# I fixed it by going through the steps for each file one at a time : git add ... then git commit .... then git push.....
