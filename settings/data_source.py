__author__ = 'kevin'

from settings.test_config import current_env
class AW(object):
    accounts = {'UAT':{'username':'kevin', 'password':'test'}, \
                'QA':{'username':'kevin', 'password':'test'}
               }[current_env]

