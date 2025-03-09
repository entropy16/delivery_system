""" Contains CustomTokenAuthentication class. """
from rest_framework.authentication import TokenAuthentication


class CustomTokenAuthentication(TokenAuthentication):
    """ Custom Token Authentication class. """
    keyword = "Bearer"
