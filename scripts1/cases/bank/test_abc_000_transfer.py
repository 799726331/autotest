# -*- encoding: utf-8 -*-
'''
@File    :   test_transfer.py
@Time    :   2020/09/09 09:55:25
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   农行-单笔支付接口测试
'''

# here put the import lib

import sys
import os
sys.path.append(os.getcwd().split("scripts1",1)[0])

# 引入接口、测试用例、ip
from scripts1.apis.bank.ccb_api import *         # 接口
from scripts1.datas.bank.data_abc_000_transfer import *      # 测试用例
from scripts1.model.bank.bank_req import bank_req            


header = {'Content-Type': 'application/json'}

api = Transfer_Api.api

def transfer_data(test_host):
    """用例集"""
    if test_host == "abc":
        Transfer_Data = Transfer_abc_Data()
    return Transfer_Data
'''
import pytest
cases = []
for i in transfer_data("abc").cases:
    cases.append ((i["title"],i["case"],i["expection"]))

@pytest.mark.parametrize("title,case,expection",cases)
def test_abc_transfer(test_host,title,case,expection):
    """农行-单笔支付接口测试"""
    title = title
    resp = bank_req(test_host,case,api)
    assert resp.status_code == 200,"响应状态不为200:{}!".format(resp.status_code)
    assert expection == resp.json()["data"]["rstStatus"]
'''


if __name__ == "__main__":

    import json
    import requests
    test_data = transfer_data("abc")

    for i in range(len(test_data.cases)):
        
        if i == 60:
            print("跳过：",i)
        elif i >=0:
            #print("测试序号：",i)
            title = test_data.cases[i]["title"]
            case = test_data.cases[i]["case"]
            print(case)
            
            '''
            header = {'Content-Type':'application/json',"Accept-Encoding":""}
            url1 = "https://sit.elimen.com.cn/plumberpay/cxf/mockit/reqEncrySign"
            url2 = "https://sit.elimen.com.cn/plumberpay/cxf/chnel/v1/payment/transfer"
            url3 = "https://sit.elimen.com.cn/plumberpay/cxf/mockit/rspDecry"
            case = json.dumps(case)
            resp1 = requests.request("post",url1,data=case,headers =header )
            
            params = json.dumps(resp1.json(),ensure_ascii=False)
            resp2 = requests.request("post",url2,data=params,headers =header )
            params3 = json.dumps(resp2.json())
            resp3 = requests.request("post",url3,data=params3,headers =header )
            '''
            resp = bank_req("100",case,api)
            try:
                print(resp.json()["data"]["rstStatus"],test_data.cases[i]["expection"])
                print("农行:",title,":",resp.json())
                print("")
                with open("abc_transfer.txt","a+",encoding="utf-8")as f:
                    f.write("农行-单笔支付接口"+title + ":" + "\n")
                    f.write(json.dumps(resp.json(),ensure_ascii=False) + "\n")
                    f.write("\n")
            except Exception as e:
                print(e)

