# -*- encoding: utf-8 -*-
'''
@File    :   run.py
@Time    :   2020/08/05 11:30:20
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   运行文件：
                1. case_dir：用例项目路径：
                2. report_name：测试报告文件名称
                3. report_dir：测试报表存放路径
                4. host: 测试环境 - 环境代码：135、100、pre
                5. send_email: 是否发送邮件，y/n
                python run.py [项目名]/[用例文件名称] [测试报告名称] [环境代码] [是否发送邮件]
                e.g: 
                    1. 执行指定用例
                        python run.py elimen/test_login.py rport.html 135 YES/NO
                    2. 执行指定项目中全部用例
                        python run.py elimen rport.html 135 YES/NO

'''

# here put the import lib


import os
import sys
sys.path.append(os.getcwd().split("scripts1",1)[0])
from scripts1.utils.send_email import sendEmail
from scripts1.utils.config import FileDir

if __name__ == "__main__":

    try:
        test_ip = ["NO", "135", "100", "134", "pre", "SIT","23","dev2"]
        params = sys.argv[1:]
        case_dir, report_name, host, send_email = params[0], params[1], params[2], params[3]

        if host not in test_ip:
            print("{}:参数错误!请输入一下关键词：{}".format(host, test_ip))
        else:
            if send_email.upper() == "YES" or send_email.upper() == "NO":
                project_name = case_dir.split("/", 1)[0]
                report_file_dir = FileDir.report_dir + "/" + project_name + "/"
                report = report_file_dir + report_name
                if host in ["135", "100", "134", "pre", "SIT","23","dev2"]:
                    os.system(
                        "pytest {}/{} --test_host={} --html={} --self-contained-html".format(
                            FileDir.case_dir,
                            case_dir,
                            host,
                            report
                        )
                    )
                elif host == "NO":
                    os.system(
                        "pytest {}/{} --html={} --self-contained-html".format(
                            FileDir.case_dir,
                            case_dir,
                            report
                        )
                    )
                if send_email.upper() == "YES":
                    sendEmail(report_name, report_file_dir, project_name)
                    print("测试结束，请邮箱查询测试报告！")
                else:
                    print("测试结束，请查看测试报告!")
            else:
                print("{}:参数错误！请输入是否发送邮件：yes/no".format(send_email))

    except Exception as f:
        print(f)
