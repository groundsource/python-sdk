"""
base_verb.py

Defines the abstract class for all BXML verbs

@copyright Bandwidth INC
"""

import abc


class AbstractBxmlVerb():

    
    def to_bxml(self):
        """
        Converts the class into its xml representation

        :return str: The string xml representation
        """
        pass
