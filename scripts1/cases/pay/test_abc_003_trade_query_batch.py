# -*- encoding: utf-8 -*-
'''
@File    :   test_trade_query_batch.py
@Time    :   2020/11/26 10:20:20
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   农行-批量订单查询用例
'''

# here put the import lib
import os,sys
sys.path.append(os.getcwd().split("scripts1",1)[0])
from scripts1.apis.pay import pay_api
from scripts1.datas.pay.data_abc_003_trade_query_batch import *
from scripts1.model.pay.pay_req import pay_req

api = pay_api.Trade_query_batch.api

def data_list(test_host):
    """获取测试集"""
    
    data = Trade_query_batch_abc_data()
    return data

import pytest
cases = []
for i in data_list().cases:
    cases.append ((i["title"],i["case"],i["expection"]))
    #break
@pytest.mark.parametrize("title,case,expection",cases)
def test_ccb_trade_query_batch(test_host,title,case,expection):
    """农行-批量订单查询用例"""
    title = title
    resp = pay_req(test_host,api,case,"99999998")
    if len(resp.json()["rstCnt"]) != 1 :
        assert resp.status_code == 200
        assert expection in str(resp.json())
    else:
        assert resp.status_code == 200
        assert expection == eval(resp.json()["rstCnt"])["totalNum"]


if __name__ == "__main__":

    import json

    for i in range(len(Trade_query_batch_abc_data.cases)):
        print("测试序号：",i)
        if i == 700:
            print("跳过：",i)
        elif i ==9 or i == 10:
            title = Trade_query_batch_abc_data.cases[i]["title"]
            case = Trade_query_batch_abc_data.cases[i]["case"]
            resp = pay_req("100",api,case)
            print(resp.status_code)
            print(title,":",resp.json())
            print("")
            with open("testresult.txt","a+",encoding="utf-8")as f:
                f.write("批量订单查询接口"+title + ":" + "\n")
                f.write(json.dumps(resp.json(),ensure_ascii=False) + "\n")
                f.write("\n")
        elif i >=0 and i not in [9,10]:
            title = Trade_query_batch_abc_data.cases[i]["title"]
            case = Trade_query_batch_abc_data.cases[i]["case"]
            resp = pay_req("100",api,case,"99999998")
            print(resp.status_code)
            print(title,":",resp.json())
            print("")
            with open("testresult.txt","a+",encoding="utf-8")as f:
                f.write("批量订单查询接口"+title + ":" + "\n")
                f.write(json.dumps(resp.json(),ensure_ascii=False) + "\n")
                f.write("\n")