from codereview.networking import gh_request
from codereview.parsing import parse, json_encode
import codereview.printing as printers

def list(state='open'):
    """List code reviews (Github Pull Request)

    state: filter by the current state of the review (open | closed)
    """
    reviews = parse(gh_request('GET', '/repos/:user/:repo/pulls'))
    printers.print_review_list(reviews)

def show(ID):
    """Shows a single code review by its number.

    ID: identifier of the review to be shown 
    """
    review = parse(gh_request('GET', '/repos/:user/:repo/pulls/:id', uri_vars={'id': ID}))
    printers.print_review(review)

def create(title, head, base='master', message=''):
    """Create a new code review.

    title: short title of the review
    head: reference to changes being merged in
    base: destination of where merge will be applied
    message: long description of review
    """
    review_info = {
        'title': title,
        'body': message,
        'head': head,
        'base': base,
    }

    data = json_encode(review_info)
    review = parse(gh_request('POST', '/repos/:user/:repo/pulls', body=data))
    printers.print_review_created(review)

def update(ID, **updates):
    """Update a code review.

    You may update one or more of these properties:
      title, body, or state
    """
    # Filter out any None values.
    review_updates = {k:v for k,v in updates.items() if v}

    if len(review_updates) > 0:
        data = json_encode(review_updates)
        gh_request('POST', '/repos/:user/:repo/pulls/:id', uri_vars={'id': ID}, body=data)
        printers.print_review_updated()

