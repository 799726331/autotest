# -*- encoding: utf-8 -*-
'''
@File    :   test_transfer.py
@Time    :   2020/09/09 09:55:25
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   建行-单笔支付接口测试
'''

# here put the import lib

#  
import sys
import os
sys.path.append(os.getcwd().split("scripts1",1)[0])

# 引入接口、测试用例、ip
from scripts1.apis.bank.ccb_api import *         # 接口
from scripts1.datas.bank.data_ccb_000_transfer import *      # 测试用例
from scripts1.model.bank.bank_req import bank_req


header = {'Content-Type': 'application/json'}

api = Transfer_Api.api

def transfer_data(test_host):
    """用例集"""
    if test_host == "ccb":
        Transfer_Data = Transfer_ccb_Data()
    
    return Transfer_Data

'''
import pytest
cases = []
for i in transfer_data("ccb").cases:
    cases.append ((i["title"],i["case"],i["expection"]))

@pytest.mark.parametrize("title,case,expection",cases)
def test_ccb_transfer(test_host,title,case,expection):
    """建行-单笔支付接口测试"""
    title = title
    resp = bank_req(test_host,case,api)
    assert resp.status_code == 200,"响应状态不为200:{}!".format(resp.status_code)
    assert expection == resp.json()["data"]["rstStatus"]
'''


if __name__ == "__main__":


    import json
    test_data = transfer_data("ccb")

    for i in range(len(test_data.cases)):
        
        if i == 60:
            print("跳过：",i)
        elif i ==0:
            print("测试序号：",i)
            title = test_data.cases[i]["title"]
            case = test_data.cases[i]["case"]
            expection = test_data.cases[i]["expection"]
            # print(case)
            resp = bank_req("100",case,api)
            print(case)
            print(resp.json()["data"]["rstStatus"],"&",expection)
            print(title,":",resp.json())
            print("")
            with open("ccb_transfer.txt","a+",encoding="utf-8")as f:
                f.write("建行-单笔支付接口"+title + ":" + "\n")
                f.write(json.dumps(resp.json(),ensure_ascii=False) + "\n")
                f.write("\n")
        
