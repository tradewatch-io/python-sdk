# coding: utf-8

"""
    tradewatch.io

    Financial market data for Developers

    The version of the OpenAPI document: 3.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tradewatch.models.crypto_exchange_item import CryptoExchangeItem

class TestCryptoExchangeItem(unittest.TestCase):
    """CryptoExchangeItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CryptoExchangeItem:
        """Test CryptoExchangeItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CryptoExchangeItem`
        """
        model = CryptoExchangeItem()
        if include_optional:
            return CryptoExchangeItem(
                id = '',
                name = '',
                year_established = 56
            )
        else:
            return CryptoExchangeItem(
                id = '',
                name = '',
                year_established = 56,
        )
        """

    def testCryptoExchangeItem(self):
        """Test CryptoExchangeItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
