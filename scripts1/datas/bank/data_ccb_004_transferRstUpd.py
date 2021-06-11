# -*- encoding: utf-8 -*-
'''
@File    :   pay_ccb_transferRstUpd_data.py
@Time    :   2020/11/19 15:09:28
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   农行-付款结果修改
'''

# here put the import lib

import time
channel="99999998"

class TransferRstUpd_134_data():
    """付款结果修改"""
    cases = [
        {
            "title":"000-客户方交易流水号custPyNo长度65位，请求失败",
            "expection":"",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20200626","reqTime":"1592660700424","bankCode":"105","version":"1.0","remark":"单笔支付结果修改"},"transferRsts":[{"custPyNo":"123456789012345678901234567890123456789012345678901234567890123456","rstStatus":"1","rmrk":"支付成功的"}]}}
        },
        {
            "title":"001-客户方交易流水号custPyNo为空，请求失败",
            "expection":"",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20200626","reqTime":"1592660700424","bankCode":"105","version":"1.0","remark":"单笔支付结果修改"},"transferRsts":[{"custPyNo":"","rstStatus":"1","rmrk":"支付成功的"}]}}
        },
        {
            "title":"002-交易结果状态码rstStatus为空，请求失败",
            "expection":"",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20200626","reqTime":"1592660700424","bankCode":"105","version":"1.0","remark":"单笔支付结果修改"},"transferRsts":[{"custPyNo":"abc2020121814","rstStatus":"","rmrk":"支付成功的"}]}}
        },
        {
            "title":"003-交易结果状态码rstStatus为2位数，请求失败",
            "expection":"",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20200626","reqTime":"1592660700424","bankCode":"105","version":"1.0","remark":"单笔支付结果修改"},"transferRsts":[{"custPyNo":"abc2020121814","rstStatus":"45","rmrk":"支付成功的"}]}}
        },
        {
            "title":"004-修改交易成功的数据为交易失败，请求失败",
            "expection":"",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20200626","reqTime":"1592660700424","bankCode":"105","version":"1.0","remark":"单笔支付结果修改"},"transferRsts":[{"custPyNo":"abC202012180935360016","rstStatus":"2","rmrk":"支付失败的"}]}}
        },
        {
            "title":"005-修改交易失败的数据为交易成功，请求失败",
            "expection":"",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":"20200626","reqTime":"1592660700424","bankCode":"105","version":"1.0","remark":"单笔支付结果修改"},"transferRsts":[{"custPyNo":"abc2020121820","rstStatus":"1","rmrk":"支付失败的"}]}}
        },
    ]

