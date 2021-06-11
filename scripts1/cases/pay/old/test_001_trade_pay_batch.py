# -*- encoding: utf-8 -*-
'''
@File    :   test_trade_pay.py
@Time    :   2020/11/23 09:51:07
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   支付平台-统一付款接口
'''

# here put the import lib

import os,sys
sys.path.append(os.getcwd().split("scripts1",1)[0])


from scripts1.apis.pay import pay_api
from scripts1.datas.pay.data_001_trade_pay_batch import *
from scripts1.model.pay.pay_req import pay_req


api = pay_api.Trade_pay_batch.api

def data_list(test_host):
    """获取测试集"""
    if test_host== "135":
        data = Trade_pay_batch_135_data
    elif test_host == "100":
        data = Trade_pay_batch_100_data
    return data

def test_000_trade_pay_batch(test_host):
    """"000-批量支付，仅必填，支付成功"""
    i = 0
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_001_trade_pay_batch(test_host):
    """"001-支付场景payScene,为空，支付失败"""
    i = 1
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_002_trade_pay_batch(test_host):
    """"002-支付产品，payProduct,为空，支付失败"""
    i = 2
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_003_trade_pay_batch(test_host):
    """"003-批量支付，混合银行，支付成功"""
    i = 3
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_004_trade_pay_batch(test_host):
    """"004-批量支付，部分校验通过，部分校验不通过，支付失败"""
    i = 4
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]


def test_005_trade_pay_batch(test_host):
    """"005-批量支付，校验通过，部分符合银行支付，部分不符合银行支付：符合银行部分支付成功，不符合银行部分支付失败"""
    i = 5
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_006_trade_pay_batch(test_host):
    """"006-批量支付，全部校验不通过，支付失败"""
    i = 6
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_007_trade_pay_batch(test_host):
    """"007-客户批次号outBatchNo，为空，支付失败"""
    i = 7
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]
 
def test_008_trade_pay_batch(test_host):
    """"008-客户订单号，outTxNo，为空，支付失败"""
    i = 8
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_009_trade_pay_batch(test_host):
    """"009-付款方账号，pyrAcctNo，为空，支付失败"""
    i = 9
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_010_trade_pay_batch(test_host):
    """"010-收款方开户行号，rcvDepBankNo，为空，支付失败"""
    i = 10
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_011_trade_pay_batch(test_host):
    """"011-收款方行类别，rcvBankCgy，为空，支付失败"""
    i = 11
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_012_trade_pay_batch(test_host):
    """"012-收款方账号，rcvAcctNo，为空，支付失败"""
    i = 12
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_013_trade_pay_batch(test_host):
    """"013-收款方账户名称，rcvAcctName，为空，支付失败"""
    i = 13
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_014_trade_pay_batch(test_host):
    """"014-收款方账户类别，rcvAcctCgy，为空，支付失败"""
    i = 14
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]
 
def test_015_trade_pay_batch(test_host):
    """"015-币种，currCode，为空，支付失败"""
    i = 15
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_016_trade_pay_batch(test_host):
    """"016-交易金额，txAmt，为空，支付失败"""
    i = 16
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]
 
def test_017_trade_pay_batch(test_host):
    """"017-用途名称，useName，为空，支付失败"""
    i = 17
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]
 
def test_018_trade_pay_batch(test_host):
    """"018-支付场景非指定场景，支付失败"""
    i = 18
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_019_trade_pay_batch(test_host):
    """"019-支付产品，非指定产品，支付失败"""
    i = 19
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_020_trade_pay_batch(test_host):
    """"020-客户批次号，outBatchNo，重复，支付失败"""
    i = 20
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_021_trade_pay_batch(test_host):
    """"021-客户订单号，outTxNo，重复，支付失败"""
    i = 21
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_022_trade_pay_batch(test_host):
    """"022-批量支付，单次50，支付成功"""
    i = 22
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]

def test_023_trade_pay_batch(test_host):
    """"023-批量支付，单次51，支付失败"""
    i = 23
    cases_list = data_list(test_host)
    payload = cases_list.cases[i]["case"]
    expection = cases_list.cases[i]["expection"]
    resp = pay_req(test_host,api,payload,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]













if __name__ == "__main__":
    import json
    
    cases_list = data_list("100")

    for i in range(len(Trade_pay_batch_100_data.cases)):
        print("测试序号：",i)
        if i == 700:
            print("跳过：",i)
        elif i == 0:
            title = cases_list.cases[i]["title"]
            case = cases_list.cases[i]["case"]
            resp = pay_req("100",api,case,"99999998")
            print(title,":",resp.json())
            print("")
            print(eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"])
            with open("batchtestresult.txt","a+",encoding="utf-8")as f:
                f.write("批量支付接口"+title + ":" + "\n")
                f.write(json.dumps(resp.json(),ensure_ascii=False) + "\n")
                f.write("\n")
        