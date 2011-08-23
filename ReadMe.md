Code Review
===========
A code review tool powered by Github Pull Requests.

Commands
--------

```
list [state=<open|closed>] [merged=<yes|no>]
```
    
Lists code reviews for this repository.

- state:  filter by review's state (default=open)
- merged: filter out reviews that have been merged (default=yes)

```
show <id>
```

Show details of a code review.

- id: Identifier of the review to display
