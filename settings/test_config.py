import sys

__author__ = 'kevin'

Environment = {"UAT":"preview", "QA":"demo"}

#used by CI
def config(env):
    env_set = env
    if not env_set or env_set not in Environment.keys():
        env_set = "UAT"
    return env_set

current_env = config(sys.argv[1])

DOMAIN = "http://%s.airwallex.com" % Environment[current_env]