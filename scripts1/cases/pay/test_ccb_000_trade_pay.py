# -*- encoding: utf-8 -*-
'''
@File    :   test_trade_pay.py
@Time    :   2020/11/23 09:51:07
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   建行-统一付款接口
'''

# here put the import lib

import os, sys

sys.path.append(os.getcwd().split("scripts1", 1)[0])
from scripts1.apis.pay import pay_api
from scripts1.datas.pay.data_000_trade_pay import *
from scripts1.datas.pay.data_ccb_000_trade_pay import *

from scripts1.model.pay.pay_req import pay_req

api = pay_api.Trade_pay.api


def data_list():
    """
    获取测试集
    """
    data = Trade_pay_ccb_data()
    return data


import pytest
cases = []
for i in data_list().cases:
    cases.append ((i["title"],i["case"],i["expection"]))
@pytest.mark.parametrize("title,case,expection",cases)
def test_pay_ccb_transfer(test_host,title,case,expection):
    """建行-统一付款"""
    title = title
    resp = pay_req(test_host,api,case,"99999998")
    if "rstCnt" in resp.json().keys():
        assert resp.status_code == 200,"响应状态不为200:{}!".format(resp.status_code)
        assert expection == eval(resp.json()["rstCnt"])["rstSts"]
    else:
        assert resp.status_code == 200,"响应状态不为200:{}!".format(resp.status_code)
        assert expection in str(resp.json()), "{}：不存在：{}".format(expection, resp.json())

    

if __name__ == "__main__":

    import json
    import traceback
    import requests
    import random

    header = {'Content-Type': 'application/json', "Accept-Encoding": ""}
    cases_list = Trade_pay_ccb_data()

    for i in range(len(cases_list.cases)):
        print("测试序号：", i)
        if i == 700:
            print("跳过：", i)
        elif i ==0 :
            import time 
            time.sleep(1)
            cases_list = Trade_pay_ccb_data()
            title = cases_list.cases[i]["title"]
            case = cases_list.cases[i]["case"]
            # case["bizCnt"]["outTxNo"] = time.strftime("%Y%m%d%H%M%S")+"00"+str(i)
            # case["bizCnt"]["outBizNo"] = time.strftime("%Y%m%d%H%M%S")+"00"+str(i)
            # case["bizCnt"]["txAmt"] = "0."+str(i)+str(random.randint(1,9))
            resp = pay_req("100", api, case, "99999998")
            # print(resp.elapsed.total_seconds())
            try:
                print("==========================================================")
                # print(case)
                print(resp.status_code)
                print(title, ":", resp.json())

                # print(case["bizCnt"]["outTxNo"])
                # print(case["bizCnt"]["outBizNo"])
                # print(case["bizCnt"]["txAmt"])
                print("")
                if "不存在的方法名" in str(resp.json()):
                    print(111111)
                with open("paytestresult.txt", "a+", encoding="utf-8")as f:
                    f.write("统一支付接口" + title + ":" + "\n")
                    f.write(json.dumps(resp.json(), ensure_ascii=False) + "\n")
                    f.write("\n")
            except Exception as f:
                print(traceback.print_exc())


