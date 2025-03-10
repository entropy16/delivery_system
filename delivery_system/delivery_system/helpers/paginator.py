""" Paginator helper definition. """
from delivery_system.settings import DEFAULT_RANGE


def paginate(data, headers):
    """ Paginate method for GET verbs. """
    _range = headers.get("Range", DEFAULT_RANGE).split("-")

    return data[int(_range[0]):int(_range[1])]
