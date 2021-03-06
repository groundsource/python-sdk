# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ApiCreateCallRequest(object):

    """Implementation of the 'ApiCreateCallRequest' model.

    TODO: type model description here.

    Attributes:
        mfrom (string): Format is E164
        to (string): Format is E164
        call_timeout (float): TODO: type description here.
        answer_url (string): TODO: type description here.
        username (string): TODO: type description here.
        password (string): TODO: type description here.
        answer_method (AnswerMethodEnum): TODO: type description here.
        disconnect_url (string): TODO: type description here.
        disconnect_method (DisconnectMethodEnum): TODO: type description
            here.
        tag (string): TODO: type description here.
        application_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mfrom": 'from',
        "to": 'to',
        "answer_url": 'answerUrl',
        "application_id": 'applicationId',
        "call_timeout": 'callTimeout',
        "username": 'username',
        "password": 'password',
        "answer_method": 'answerMethod',
        "disconnect_url": 'disconnectUrl',
        "disconnect_method": 'disconnectMethod',
        "tag": 'tag'
    }

    def __init__(self,
                 mfrom=None,
                 to=None,
                 answer_url=None,
                 application_id=None,
                 call_timeout=None,
                 username=None,
                 password=None,
                 answer_method=None,
                 disconnect_url=None,
                 disconnect_method=None,
                 tag=None):
        """Constructor for the ApiCreateCallRequest class"""

        # Initialize members of the class
        self.mfrom = mfrom
        self.to = to
        self.call_timeout = call_timeout
        self.answer_url = answer_url
        self.username = username
        self.password = password
        self.answer_method = answer_method
        self.disconnect_url = disconnect_url
        self.disconnect_method = disconnect_method
        self.tag = tag
        self.application_id = application_id

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        mfrom = dictionary.get('from')
        to = dictionary.get('to')
        answer_url = dictionary.get('answerUrl')
        application_id = dictionary.get('applicationId')
        call_timeout = dictionary.get('callTimeout')
        username = dictionary.get('username')
        password = dictionary.get('password')
        answer_method = dictionary.get('answerMethod')
        disconnect_url = dictionary.get('disconnectUrl')
        disconnect_method = dictionary.get('disconnectMethod')
        tag = dictionary.get('tag')

        # Return an object of this model
        return cls(mfrom,
                   to,
                   answer_url,
                   application_id,
                   call_timeout,
                   username,
                   password,
                   answer_method,
                   disconnect_url,
                   disconnect_method,
                   tag)
