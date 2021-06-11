# -*- encoding: utf-8 -*-
'''
@File    :   send_email.py
@Time    :   2020/07/09 16:22:19
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   None 
'''

# here put the import lib

import sys
import os

# smtplib 用于邮件的发信动作
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 用于构建邮件头
from email.header import Header
# 用于添加附件
from email.mime.multipart import MIMEMultipart

from scripts1.utils.config import GetEmailInfo

import time
tm = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime(time.time()))


def sendEmail(report_name, first_dir,project_name="elimen"):
    """
        带附件邮件
        report_name: 附件名称
        file_dir: 附件的文件路径
        return：None
    """
    #-------------1.设置邮箱-------------------#
    #用于构建邮件头
    #发信方的信息：发信邮箱，QQ邮箱授权码report_name:
    
    from_addr = GetEmailInfo.from_addr    
    password = GetEmailInfo.password      
    #收信方邮箱
    to_addr=GetEmailInfo.to_addr          
    to_addr = to_addr.split(",")

    #-------------2.编写邮件正文---------------#
    #邮箱正文内容，第一个参数为正文内容，第二个参数为格式(plain为纯文本)，第三个参数为编码
    msg=MIMEMultipart()
    msg.attach(MIMEText("当前用例已执行完成，请查看附件的测试报表！",'plain','utf-8'))
    #邮件头信息
    msg['From']=Header(from_addr)
    msg['To']=",".join(to_addr)
    msg['Subject']=Header('{}接口测试报告:{}'.format(project_name,tm))#邮件主题

    #----------------3.设置邮件附件----------#
    #可以添加txt、jpg、html等格式的文件
    #att=MIMEText(open('demo_rp2.html','rb').read(),'base64','utf-8')
    file_dir = first_dir + report_name
    att=MIMEText(open(file_dir,'rb').read(),'base64','utf-8')
    att['Content-Type']='application/octet-stream'
    att['Content-Disposition']='attachment;filename="%s"'%(report_name)#设置附件名称
    msg.attach(att)

    #----------------4.设置邮件服务器---------------------#
    #发信服务器
    #smtp_server='smtp.qq.com'
    smtp_server = "smtp.qiye.aliyun.com"
    #开启发信服务，这里使用的是加密传输
    server=smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server,465)

    #---------------5.登录邮件服务器-----------------#
    #登录发信邮箱
    server.login(from_addr,password)
    #发送邮件
    server.sendmail(from_addr,to_addr,msg.as_string())
    #关闭服务器
    server.quit()

if __name__ == "__main__":
    
    sendEmail("带有附件邮件","demo.html")
   
    



