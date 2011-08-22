try:
    # Use simplejson if it is installed.
    import simplejson as json
except ImportError:
    # Fallback to the built-in module.
    import json

def parse(content):
    """Parse the given content and return a model of it.

    Github returns content in JSON format.
    We will pass this into the parser which gives us
    back a Python object which will act as our model of the data.
    """
    return json.loads(content)

