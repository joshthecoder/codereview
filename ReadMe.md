Code Review via Github Pull Requests
====================================
A tool for performing code review using Github's pull requests.

Commands
--------

### list [state=<open|closed>] [merged=<yes|no>]
Lists code reviews for the repository.

state:  filter by review's state (default=open)
merged: filter out reviews that have been merged (default=yes)

### show <id>
Shows details of a single code review.

id: Identifier of the review to display

