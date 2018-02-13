import json

from common.shared_api import SharedAPI
from settings.test_config import current_env, Environment
from settings.data_source import AW


class CustomerBankDetailsPage(SharedAPI):
    def __init__(self, account_dict):
        super().__init__(account_dict)
        self.login()
        self.URL = "http://%s.airwallex.com:30001"%Environment[current_env] + "/bank"

    def get_customer_bank_details(self, payment_method, bank_country_code, account_name,\
                                  account_number, swift_code, bsb, aba):

        data = '''{"payment_method":"%s", \
                  "bank_country_code":"%s", \
                  "account_name":"%s",\
                  "account_number":"%s",\
                  "swift_code":"%s",\
                  "bsb":"%s",\
                  "aba":"%s"}'''\
               % (payment_method, bank_country_code,  account_name, account_number, swift_code, bsb, aba)
        return self.post_api(self.URL, data=data, headers=self.header_json)

if __name__ == "__main__":

    CBDP = CustomerBankDetailsPage(AW.accounts)
    test_pass = CBDP.get_customer_bank_details("SWIFT", "US", "John Smith", "123", "ICBCUSBJ", "", "11122233A")
    assert test_pass.status_code == 200
    assert json.loads(test_pass.content.decode('utf-8')) == {'success': 'Bank details saved'}

    test_fail = CBDP.get_customer_bank_details("Kevin", "US", "John Smith", "123", "ICBCUSBJ", "", "11122228A")
    assert test_fail.status_code == 400
    assert json.loads(test_fail.content.decode('utf-8')) == {'error': "'payment_method' field required, the value should be either 'LOCAL' or 'SWIFT'"}

    test_fail1 = CBDP.get_customer_bank_details("SWIFT", "US", "John Smith", "123", "ICBCAUBJ", "", "11122228A")
    assert test_fail1.status_code == 400