# -*- encoding: utf-8 -*-
'''
@File    :   test_trade_pay_batch_query.py
@Time    :   2020/11/26 09:50:47
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   批量支付查询用例
'''

# here put the import lib
import os,sys
sys.path.append(os.getcwd().split("scripts1",1)[0])
from scripts1.apis.pay import pay_api
from scripts1.datas.pay.data_004_trade_pay_batch_query import *
from scripts1.model.pay.pay_req import pay_req

api = pay_api.Trade_pay_batch_query.api

def data_list(test_host):
    """获取测试集"""
    if test_host== "135":
        data = Trade_pay_batch_query_100_data()
    elif test_host == "100":
        data = Trade_pay_batch_query_100_data()
    return data

def test_000_trade_pay_batch_query(test_host):
    i= 0
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == resp.json()["rspCode"]

def test_001_trade_pay_batch_query(test_host):
    i= 1
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == resp.json()["rspCode"]

def test_002_trade_pay_batch_query(test_host):
    i= 2
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection in str(resp.json())

def test_003_trade_pay_batch_query(test_host):
    i= 3
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == resp.json()["rspCode"]

def test_004_trade_pay_batch_query(test_host):
    i= 4
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection in str(resp.json())


if __name__ == "__main__":

    import json

    for i in range(len(Trade_pay_batch_query_100_data.cases)):
        print("测试序号：",i)
        if i == 700:
            print("跳过：",i)
        elif i >=0 :
            title = Trade_pay_batch_query_100_data.cases[i]["title"]
            case = Trade_pay_batch_query_100_data.cases[i]["case"]
            resp = pay_req("100",api,case,"99999998")
            print(title,":",resp.json())
            print("")
            with open("testresult.txt","a+",encoding="utf-8")as f:
                f.write("批量订单查询接口"+title + ":" + "\n")
                f.write(json.dumps(resp.json(),ensure_ascii=False) + "\n")
                f.write("\n")