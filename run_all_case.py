# coding=utf-8
import unittest
import os
from common.HTMLTestRunner import HTMLTestRunner
from common.send_mail import sendmail
def all_case():

    case_path = 'D:\\autotest\\case'
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
    return discover

if __name__ == '__main__':

    report_path = os.path.join("D:\\autotest\\report","result.html")
    with open(report_path,"wb") as fp:
        runner = HTMLTestRunner(stream=fp,title=u"自动化测试报告：",description=u"执行情况：")
        runner.run(all_case())
    fp.close()

    sendmail()

