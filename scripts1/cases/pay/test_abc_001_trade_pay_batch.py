# -*- encoding: utf-8 -*-
'''
@File    :   test_trade_pay.py
@Time    :   2020/11/23 09:51:07
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   农行-批量付款接口
'''

# here put the import lib

import os,sys
sys.path.append(os.getcwd().split("scripts1",1)[0])


from scripts1.apis.pay import pay_api
from scripts1.datas.pay.data_abc_001_trade_pay_batch import *
from scripts1.model.pay.pay_req import pay_req


api = pay_api.Trade_pay_batch.api

def data_list():
    """获取测试集"""
    data = Trade_pay_batch_abc_data
    return data

'''
import pytest
cases = []
for i in data_list().cases:
    cases.append ((i["title"],i["case"],i["expection"]))
    #break
@pytest.mark.parametrize("title,case,expection",cases)
def test_ccb_trade_pay_batch(test_host,title,case,expection):
    """农行-批量支付"""
    title = title
    resp = pay_req(test_host,api,case,"99999998")
    assert resp.status_code == 200
    assert expection == eval(resp.json()["rstCnt"])["rstList"][0]["rstSts"]
'''

if __name__ == "__main__":
    import json
    
    cases_list = data_list()

    for i in range(len(cases_list.cases)):
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
        