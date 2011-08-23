import requests
from string import Template
from urlparse import urlunsplit

from codereview.configure import configuration
from codereview.fatal import fatal

# Github API connection info
gh = { 'scheme': 'https', 'host': 'api.github.com' }

# Requests session
gh_session = requests.session(auth=configuration.get('gh_credentials'))

# Modified Template that uses : instead of $ for delimiting variables.
class MTemplate(Template): delimiter=':'

def gh_request(method, uri, uri_vars={}, query_vars=None, body=None):
    """Send a request to Github.

    method: HTTP method (GET, POST, etc)
    url: Github resource URI
    uri_vars: variables used during URI variable substitution
    query_vars: variables for the request's query string

    returns: response body content
    """
    # Substitute any variables in the URI string.
    # There are two scopes for variables: local (uri_vars)
    # and global (configuration). Local scope takes precedence
    # in the event of duplicate keys.
    uri = MTemplate(uri).substitute(configuration, **uri_vars)

    # Send request to Github servers.
    url = urlunsplit((gh['scheme'], gh['host'], uri, '', ''))
    response = gh_session.request(method, url, query_vars, data=body)
    if response.ok is False:
        fatal('Github API request failed: %s' % response.error)

    return response.content

