# coding: utf-8

"""
    tradewatch.io

    Financial market data for Developers

    The version of the OpenAPI document: 3.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tradewatch.models.conversion_info import ConversionInfo

class TestConversionInfo(unittest.TestCase):
    """ConversionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConversionInfo:
        """Test ConversionInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConversionInfo`
        """
        model = ConversionInfo()
        if include_optional:
            return ConversionInfo(
                timestamp = 1704882030,
                rate = 1.23456
            )
        else:
            return ConversionInfo(
                timestamp = 1704882030,
                rate = 1.23456,
        )
        """

    def testConversionInfo(self):
        """Test ConversionInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
