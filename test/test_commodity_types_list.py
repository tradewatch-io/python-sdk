# coding: utf-8

"""
    tradewatch.io

    Financial market data for Developers

    The version of the OpenAPI document: 3.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tradewatch.models.commodity_types_list import CommodityTypesList

class TestCommodityTypesList(unittest.TestCase):
    """CommodityTypesList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommodityTypesList:
        """Test CommodityTypesList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommodityTypesList`
        """
        model = CommodityTypesList()
        if include_optional:
            return CommodityTypesList(
                items = [
                    tradewatch.models.commodity_type_obj.CommodityTypeObj(
                        symbol = '', )
                    ]
            )
        else:
            return CommodityTypesList(
                items = [
                    tradewatch.models.commodity_type_obj.CommodityTypeObj(
                        symbol = '', )
                    ],
        )
        """

    def testCommodityTypesList(self):
        """Test CommodityTypesList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
