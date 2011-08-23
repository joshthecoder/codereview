from prettytable import PrettyTable

def print_review_list(reviews):
    """Prints a list of review objects."""
    table = PrettyTable(['#', 'Title', 'Creator', 'State'])
    for review in reviews:
        table.add_row([review['number'],
                      review['title'],
                      review['user']['login'],
                      review['state']])
    print table
