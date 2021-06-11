# -*- encoding: utf-8 -*-
'''
@File    :   test_transferRstQry.py
@Time    :   2020/10/09 15:13:45
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   农行-单笔付款结果查询
'''

# here put the import lib
import os,sys
sys.path.append(os.getcwd().split("scripts1",1)[0])

from scripts1.apis.bank.ccb_api import TransferRstQry_Api
from scripts1.datas.bank.data_abc_001_transferRstQry import *
from scripts1.model.bank.bank_req import bank_req

import json

api, method = TransferRstQry_Api.api, TransferRstQry_Api.method

def transferRstQry_data(test_host):
    """用例集"""
    Transfer_Data = TransferRstQry_abc_Data(test_host).get_case()
    return Transfer_Data

import pytest
cases = []
for i in transferRstQry_data("100"):
    cases.append((i["title"],i["case"],i["expection"]))

@pytest.mark.parametrize("title,case,expection",cases)
def test_abc_transferRstQry(test_host,title,case,expection):
    """农行-单笔付款结果查询"""
    title = title
    resp = bank_req(test_host,case,api,method)
    assert resp.status_code == 200,"响应状态不为200:{}!".format(resp.status_code)
    if "data" in resp.json().keys():
        if "excpVerfDesc" in resp.json()["data"].keys():
            assert expection == resp.json()["data"]["rstStatus"]
            assert "excpVerfDesc" in resp.json()["data"].keys()
        else:
            if "rstStatus" in resp.json()["data"].keys():
                assert expection == resp.json()["data"]["rstStatus"]
            else:
                assert expection == resp.json()["data"]["errDesc"]
    else:
        assert expection == resp.json()["message"]



if __name__ == "__main__":

    test_host = "100"
    TransferRstQry_Data = transferRstQry_data(test_host)
    for i in range(len(TransferRstQry_Data)):
        if i>=0:
            title = TransferRstQry_Data[i]["title"]
            case =  TransferRstQry_Data[i]["case"]
            resp = bank_req("100",case,api,method)
            print(title,":",resp.json())
            print("")
            with open("testresult.txt","a+",encoding="utf-8")as f:
                f.write("单笔支付结果查询："+title + ":" + "\n")
                f.write(json.dumps(resp.json(),ensure_ascii=False) + "\n")
                f.write("\n")

