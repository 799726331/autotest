# -*- encoding: utf-8 -*-
'''
@File    :   test_trade_query.py
@Time    :   2020/11/26 09:09:12
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   单笔订单查询接口用例 
'''

# here put the import lib

import os,sys
sys.path.append(os.getcwd().split("scripts1",1)[0])
from scripts1.apis.pay import pay_api
from scripts1.datas.pay.data_002_trade_query import *
from scripts1.model.pay.pay_req import pay_req

api = pay_api.Trade_query.api

def data_list(test_host):
    """获取测试集"""
    if test_host== "135":
        data = Trade_query_135_data()
    elif test_host == "100":
        data = Trade_query_100_data()
    return data

def test_000_trade_query(test_host):
    """000-查询支付成功，查询成功"""
    i= 0
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == resp.json()["rspCode"]

def test_001_trade_query(test_host):
    """001-查询支付失败，查询成功"""
    i= 1
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == resp.json()["rspCode"]

def test_002_trade_query(test_host):
    """002-查询支付中，查询成功"""
    i= 2
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == resp.json()["rspCode"]

def test_003_trade_query(test_host):
    """003-outTxNo，为空，查询无结果"""
    i= 3
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == resp.json()["rspCode"]

def test_004_trade_query(test_host):
    """004-outTxNo，不存在，查询无结果"""
    i= 4
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == resp.json()["rspCode"]

def test_005_trade_query(test_host):
    """005-outTxNo，不当前渠道，查询无结果"""
    i= 5
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == resp.json()["rspCode"]

def test_006_trade_query(test_host):
    """006-outTxNo，长度超过50，查询无结果"""
    i= 6
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == resp.json()["rspCode"]


if __name__ == "__main__":

    import json
    import requests
    test_host = "100"
    cases_list = data_list(test_host)
   

    for i in range(len(cases_list.cases)):
        print("测试序号：",i)
        if i == 700:
            print("跳过：",i)
        elif i >=0 :
            title = cases_list.cases[i]["title"]
            case = cases_list.cases[i]["case"]

            resp = pay_req(test_host,api,case,"99999998")
            print(resp.status_code)
            print(resp.json())
            
            with open("testresult.txt","a+",encoding="utf-8")as f:
                f.write("单笔订单查询接口"+title + ":" + "\n")
                f.write(json.dumps(resp.json(),ensure_ascii=False) + "\n")
                f.write("\n")
            