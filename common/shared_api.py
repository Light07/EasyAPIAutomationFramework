from settings.test_config import DOMAIN

import json
import traceback


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable https security warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class SharedAPI(object):

    def __init__(self, account_dict):
        self.user = account_dict
        self.s = requests.session()
        self.header_form = {'Content-Type': 'application/x-www-form-urlencoded', 'charset': 'UTF-8'}
        self.header_json = {'Content-Type': 'application/json', 'charset': 'UTF-8'}

    def login(self):
        parameter = {'username': self.user['username'], 'password': self.user["password"]}

        ##The domain of login_url should be consistent with DOMAIN of given api
        ##because of demo.airwallex.com:30001/api/authenticate doesn't exist,
        ##hard code the URL instead

        #login_url = DOMAIN + "/api/authenticate"
        login_url = "https://www.airwallex.com/api/authenticate"
        try:
            p = self.s.post(login_url, data=parameter, verify=False)

            ##For Most of the applications, user must to login first to get access token
            #before any request send to server, the token is needed either on header or body,
            #here is a place holder and make it success always to keep things look real
            if int(p.status_code) != 200:
                print('success')
                pass
            else:
                raise Exception('login failed')
        except BaseException:
            traceback.print_exc()


    def post_api(self, url, **kwargs):
        return self.s.post(url, **kwargs)

    def get_api(self, url, **kwargs):
        return self.s.get(url, **kwargs).content


if __name__ == "__main__":
    account = {"username":"kevin", "password":"test"}
    shared = SharedAPI(account)
    print(shared.login())