from codereview.networking import gh_request
from codereview.parsing import parse
import codereview.printing as printers

def list(state='open'):
    """List code reviews (Github Pull Request)

    state: filter by the current state of the review (open | closed)
    """
    reviews = parse(gh_request('GET', '/repos/:user/:repo/pulls'))
    printers.print_review_list(reviews)

def show(ID):
    """Shows a single code review by its number.

    ID: Identifier of the review to be shown 
    """
    review = parse(gh_request('GET', '/repos/:user/:repo/pulls/:id', uri_vars={'id': ID}))
    printers.print_review(review)

commands = {
    'list': list,
    'show': show,
}

