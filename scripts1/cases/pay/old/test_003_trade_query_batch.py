# -*- encoding: utf-8 -*-
'''
@File    :   test_trade_query_batch.py
@Time    :   2020/11/26 10:20:20
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   批量订单查询用例
'''

# here put the import lib
import os,sys
sys.path.append(os.getcwd().split("scripts1",1)[0])
from scripts1.apis.pay import pay_api
from scripts1.datas.pay.data_003_trade_query_batch import *
from scripts1.model.pay.pay_req import pay_req

api = pay_api.Trade_query_batch.api

def data_list(test_host):
    """获取测试集"""
    if test_host== "135":
        data = Trade_query_batch_135_data()
    elif test_host == "100":
        data = Trade_query_batch_100_data()
    return data

def test_000_trade_query_batch(test_host):
    """000-查询成功"""
    i= 0
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["totalNum"]

def test_001_trade_query_batch(test_host):
    """001-查询条数超过100"""
    i= 1
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection in str(resp.json())

def test_002_trade_query_batch(test_host):
    """002-查询指定日期，查询成功"""
    i= 2
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["totalNum"]

def test_003_trade_query_batch(test_host):
    """003-查询指定outBatchNo，查询成功"""
    i= 3
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["totalNum"]

def test_004_trade_query_batch(test_host):
    """004-查询指定交易状态，查询成功"""
    i= 4
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["totalNum"]

def test_005_trade_query_batch(test_host):
    """005-查询指定txType，查询成功"""
    i= 5
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["totalNum"]

def test_006_trade_query_batch(test_host):
    """006-查询全条件，查询成功"""
    i= 6
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["totalNum"]

def test_007_trade_query_batch(test_host):
    """007-开始日期格式非法，查询无结果"""
    i= 7
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection in str(resp.json())

def test_008_trade_query_batch(test_host):
    """008-结束日期格式非法，查询无结果"""
    i= 8
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection in str(resp.json())

def test_009_trade_query_batch(test_host):
    """009-起始笔数等于数据库现存数，查询无结果"""
    i= 9
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case)
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["totalNum"]

def test_010_trade_query_batch(test_host):
    """010-起始笔数超过数据库现存数，查询无结果"""
    i= 10
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case)
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["totalNum"]


def test_011_trade_query_batch(test_host):
    """011-状态非默认值，查询无结果"""
    i= 11
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection in str(resp.json())

def test_012_trade_query_batch(test_host):
    """012-交易类型非默认值，查询无结果"""
    i= 12
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection in str(resp.json())

def test_013_trade_query_batch(test_host):
    """013-outBatchNo不存在，查询无结果"""
    i= 13
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection in str(resp.json())

def test_014_trade_query_batch(test_host):
    """014-outBatchNo存在非当前渠道，查询无结果"""
    i= 14
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection in str(resp.json())

def test_015_trade_query_batch(test_host):
    """015-outBatchNo超过51，查询无结果"""
    i= 15
    cases_list = data_list(test_host)
    case = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection in str(resp.json())






if __name__ == "__main__":

    import json

    for i in range(len(Trade_query_batch_100_data.cases)):
        print("测试序号：",i)
        if i == 700:
            print("跳过：",i)
        elif i ==9 or i == 10:
            title = Trade_query_batch_100_data.cases[i]["title"]
            case = Trade_query_batch_100_data.cases[i]["case"]
            resp = pay_req("100",api,case)
            print(resp.status_code)
            print(title,":",resp.json())
            print("")
            with open("testresult.txt","a+",encoding="utf-8")as f:
                f.write("批量订单查询接口"+title + ":" + "\n")
                f.write(json.dumps(resp.json(),ensure_ascii=False) + "\n")
                f.write("\n")
        elif i >=0 and i not in [9,10]:
            title = Trade_query_batch_100_data.cases[i]["title"]
            case = Trade_query_batch_100_data.cases[i]["case"]
            resp = pay_req("100",api,case,"99999998")
            print(resp.status_code)
            print(title,":",resp.json())
            print("")
            with open("testresult.txt","a+",encoding="utf-8")as f:
                f.write("批量订单查询接口"+title + ":" + "\n")
                f.write(json.dumps(resp.json(),ensure_ascii=False) + "\n")
                f.write("\n")