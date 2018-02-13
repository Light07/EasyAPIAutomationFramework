__author__ = 'kevin'

import unittest,os
from common.html_report import Generate_Report

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),"test"),\
                                                pattern='*.py',top_level_dir=os.path.dirname(__file__))
    html_report = Generate_Report()
    html_report.generate_report(suite)