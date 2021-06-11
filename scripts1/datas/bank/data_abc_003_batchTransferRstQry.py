# -*- encoding: utf-8 -*-
'''
@File    :   pay_ccb_batchTransferRstQry_data.py
@Time    :   2020/11/11 15:29:17
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   农行-支付结果批量查询接口用例
'''

# here put the import libbc
import time
channel = "99999998"
class BatchTransferRstQry_abc_Data():
    cases = [
        {
            "title":"000-批量查询成功",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"}}},
            "expection":"S"
        }
        ]