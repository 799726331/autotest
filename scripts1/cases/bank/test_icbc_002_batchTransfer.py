# -*- encoding: utf-8 -*-
'''
@File    :   test_abc_batchTransfer.py
@Time    :   2020/11/11 16:55:04
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   工行-批量支付测试用例 
'''

# here put the import lib
import os,sys
sys.path.append(os.getcwd().split("scripts1",1)[0])

from scripts1.apis.bank.ccb_api import *
from scripts1.datas.bank.data_icbc_002_batchTransfer import *
from scripts1.model.bank.bank_req import bank_req

header = {'Content-Type': 'application/json'}

api = BatchTransfer_Api.api

def batchTransfer_data(test_host):
    """用例集"""
    if test_host == "icbc":
        BatchTransfer_data = BatchTransfer_icbc_data("icbc").get_case()
    return BatchTransfer_data


import pytest
cases = []
test_list = batchTransfer_data("icbc")
for i in range(len(test_list)):
    if i!=6:
        cases.append ((test_list[i]["title"],test_list[i]["case"],test_list[i]["expection"]))

@pytest.mark.parametrize("title,case,expection",cases)
def test_icbc_transfer(test_host,title,case,expection):
    """工行-批量支付测试用例 """
    title = title
    resp = bank_req(test_host,case,api)
    rstStatus_list = []
    for i in range(len(resp.json()["data"])):
        rstStatus_list.append(resp.json()["data"][i]["rstStatus"])
    assert resp.status_code == 200,"响应状态不为200:{}!".format(resp.status_code)
    assert expection == rstStatus_list  
    #assert expection == resp.json()["data"]["rstStatus"]



if __name__ == "__main__":
    
    import json
    test_host = "icbc"
    test_case = batchTransfer_data(test_host)
    for i in range(len(test_case)):
        if i in [6]:
            print(i)

        elif i >=0:
            case = test_case[i]["case"]
            title = test_case[i]["title"]

            resp = bank_req("SIT",case,api)
            rstStatus_list = []
            for i in range(len(resp.json()["data"])):
                rstStatus_list.append(resp.json()["data"][i]["rstStatus"])
            print(rstStatus_list)
            print(title,":",resp.json())
            print("")
            with open("test_result.txt","a+",encoding="utf-8")as f:
                f.write("批量支付接口"+title + ":" + "\n")
                f.write(json.dumps(resp.json(),ensure_ascii=False) + "\n")
                f.write("\n")
    
    