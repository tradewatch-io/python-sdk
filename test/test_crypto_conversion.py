# coding: utf-8

"""
    tradewatch.io

    Financial market data for Developers

    The version of the OpenAPI document: 3.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tradewatch.models.crypto_conversion import CryptoConversion

class TestCryptoConversion(unittest.TestCase):
    """CryptoConversion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CryptoConversion:
        """Test CryptoConversion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CryptoConversion`
        """
        model = CryptoConversion()
        if include_optional:
            return CryptoConversion(
                info = tradewatch.models.conversion_info.ConversionInfo(
                    timestamp = 1704882030, 
                    rate = 1.23456, ),
                query = tradewatch.models.crypto_conversion_query.CryptoConversionQuery(
                    from = '', 
                    to = '', 
                    amount = 1.0E-8, 
                    precision = 56, ),
                result = 1.337
            )
        else:
            return CryptoConversion(
                info = tradewatch.models.conversion_info.ConversionInfo(
                    timestamp = 1704882030, 
                    rate = 1.23456, ),
                query = tradewatch.models.crypto_conversion_query.CryptoConversionQuery(
                    from = '', 
                    to = '', 
                    amount = 1.0E-8, 
                    precision = 56, ),
                result = 1.337,
        )
        """

    def testCryptoConversion(self):
        """Test CryptoConversion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()