from prettytable import PrettyTable
import time

def pretty_timestamp(timestamp):
    """Returns a pretty format of timestamp."""
    parsed = time.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    return time.asctime(parsed)

def print_review_list(reviews):
    """Prints a list of review objects."""
    table = PrettyTable(['#', 'Title', 'Creator', 'State'])
    for review in reviews:
        table.add_row([review['number'],
                      review['title'],
                      review['user']['login'],
                      review['state']])
    print table

"""Review item details template"""
review_tmpl = """\
Title:   {title}
Creator: {creator}
Created: {created}
Merged:  {merged}
Web URL: {web_url}

{body}
"""

def print_review(review):
    """Prints details of a single review item."""
    print review_tmpl.format(
        title=review['title'],
        creator=review['user']['login'],
        created=pretty_timestamp(review['created_at']),
        merged=review['merged_at'] if review['merged'] else 'unmerged',
        web_url=review['html_url'],
        body=review['body'])

def print_review_created(review):
    """Prints a confirmation a review was created successfully."""
    print 'Review Created'

def print_review_updated():
    print 'Review Updated'

