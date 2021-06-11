# -*- encoding: utf-8 -*-
'''
@File    :   test_pay_ccb_batchTransferRstQry.py
@Time    :   2020/11/11 15:34:41
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   建行-支付结果批量查询接口
'''

# here put the import lib
import sys
import os

sys.path.append(os.getcwd().split("scripts1",1)[0])

from scripts1.apis.bank.ccb_api import *
from scripts1.datas.bank.data_ccb_003_batchTransferRstQry import *
from scripts1.model.bank.bank_req import bank_req


header = {'Content-Type': 'application/json'}

api =BatchTransferRstQry_Api.api

def batchTransferRstQry_data(test_host):
    """用例集"""
    if test_host == "ccb":
       batchTransferRstQry_Data = BatchTransferRstQry_ccb_Data()
    return batchTransferRstQry_Data

# 用例
def test_000_pay_ccb_BatchTransferRstQry(test_host):
    """支付结果批量查询"""
    i = 0
    test_data = batchTransferRstQry_data("ccb")
    case = test_data.cases[i]["case"]
    expection = test_data.cases[i]["expection"]
    resp = bank_req(test_host,case,api)
    assert resp.status_code == 200,"响应状态不为200:{}!".format(resp.status_code)
    assert expection == resp.json()["rspCode"]

if __name__ == "__main__":

    import json
    test_host = "ccb"
    test_data = batchTransferRstQry_data(test_host)
    for i in range(len(test_data.cases)):
        case = test_data.cases[i]["case"]
        title = test_data.cases[i]["title"]
        resp = bank_req("SIT",case,api)
        print(title,":",resp.json())
        print("")
        with open("testresult.txt","a+",encoding="utf-8")as f:
            f.write("支付结果批量查询接口"+title + ":" + "\n")
            f.write(title + ":" + json.dumps(resp.json(),ensure_ascii=False) + "\n")
            f.write("\n")


            