#02/13/2018
Author: kevin cai
# Generic APIFrameWork
### How to use:

1."Common":  --Common methods to facilitates the whole project.
* html_report: To generate HTML report after test cases run.
* shared_api: Import method like post/get to serve all the API requests.
* txt_report: Independent way to run all the cases under test and generate simple txt format report.

2."Page": --The page under test.
* in this file, only store the page related function/method/date
* test case related to this page should not be included here.
* different page should have separated pages.
* customer_bank_details  page example

3."Settings": --Global settings & configuration & global data.
* __init__:
* data_source: all the account, common test data.
* test config: environment, domain or other common config.


4."test" -- Test cases inherited from pages, this is the cases under test.
* each test file should have a page file accordingly.
* framework will only search the cases under this folder

5."main"  -- Load & run all of the test cases defined in test folder.

* System will automated search all the test method defined in test folder and run them.

### Note:

1. If you want to skip some test or even the whole test class, just put @unittest.skip("description") in front of test case/test class

2. To use the HTML report, you need to download HTMLTestRunner.py from http://tungwaiyip.info/software/HTMLTestRunner.html then put this file to lib folder of your python installation directory.


### Answers:
* This is a very simple framework only developed to address the question, it only show part of my skills not all of my capabilities.
* I didn't write all of the test cases need to be done, because i think the most important thing is how you think when u face a technology problems.
* On root folder of this project, there is a excel file, within it, list all of the test cases need to be done.
* I may write some codes to make the test cases data-driven, so user only need to configure the excel file to execute multiple test cases, this is one thing i didn't do.
* For CI, check the file test_config under settings folder. you only need to configure jenkins like below:
 * cd "%WORKSPACE%\settings
 * python test_config.py" %TEST_ENV%   #TEST_ENV is the choice parameter you configured in jenkins.
* 6. For bug founding, i didn't list it, but you will have it after all of the cases are executed, you can open the html report for details.

### airplay 
