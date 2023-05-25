# coding: utf-8
"""
   Python SDK for OpenFGA

   API version: 0.1
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://discord.gg/8naAwJfWN6
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""


class ClientReadChangesRequest():
    """
    ClientReadChangesRequest encapsulates the parameters required to read changes
    """

    def __init__(self, type: str):
        self._type = type

    @property
    def type(self):
        """
        Return type
        """
        return self._type