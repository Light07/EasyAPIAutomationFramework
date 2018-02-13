#coding=utf-8

import json
import unittest

from page.customer_bank_details import CustomerBankDetailsPage

from settings.data_source import AW

class Test_CustomerBankDetailsPage(unittest.TestCase):
    def setUp(self):
        self.page = CustomerBankDetailsPage(AW.accounts)

    def test_payment_local_pass(self):
        """  verify payment_method: LOCAL -- "LOCAL","US", "ke", "1","","","ismusthad' """
        result = self.page.get_customer_bank_details("LOCAL", "US", "ke", "1","","","ismusthad")
        assert result.status_code == 200
        assert json.loads(result.content.decode('utf-8')) == {'success': 'Bank details saved'}

    def test_payment_swift_pass(self):
        """   verify payment_method: SWIFT  "SWIFT", "AU", "kevin", "1234567","ICBKAUSH","123456", "" """
        result = self.page.get_customer_bank_details("SWIFT", "AU", "kevin", "1234567","ICBKAUSH","123456", "")
        assert result.status_code == 200
        assert json.loads(result.content.decode('utf-8')) == {'success': 'Bank details saved'}

    def test_payment_method_blank(self):
        """   verify payment_method balank failed: "Kevin", "US", "John Smith", "123", "ICBCUSBJ", "", "11122228A" "" """
        result = self.page.get_customer_bank_details("Kevin", "US", "John Smith", "123", "ICBCUSBJ", "", "11122228A")
        assert result.status_code == 400
        assert json.loads(result.content.decode('utf-8')) == {'error': "'payment_method' field required, the value should be either 'LOCAL' or 'SWIFT'"}

    def test_country_swift_code_match(self):
        """ verify bank_country and swift_code doesn't mathch, should return 400"""
        result = self.page.get_customer_bank_details("SWIFT", "US", "John Smith", "123", "ICBCAUBJ", "", "11122228A")
        assert result.status_code == 400
        assert json.loads(result.content.decode('utf-8')) == {"error": "The swift code is not valid for the given bank country code: US"}

    @unittest.skip("not run")
    def CustomerBankDetailsPage(self):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":

    def suite():
        return unittest.makeSuite(Test_CustomerBankDetailsPage, "test")
    unittest.main(defaultTest = 'suite')
