'''
-*- coding: utf-8 -*-
@Time    : 2021/6/1 11:48
@Author  : Luzixuan
@File    : test_prodApply_req.py
@contest    : 测试产品开通接口
'''

from scripts1.model.goodlife.goodlife_req import goodlife_req
from scripts1.utils.host import HOST
from scripts1.apis.goodlife import goodlife_api
from scripts1.datas.goodlife.data_001_prodApply import *
from scripts1.datas.goodlife.data_000_custInfoQuery import *

# 切换环境
host = "23"
# host = "100"

# 产品开通接口
def test_prodApply_000():
    api = goodlife_api.ProdApply_Api.api
    payload = goodlife_prodApply_135_data.cases[0]["case"]
    resq = goodlife_req(host=host, api=api, payload=payload)
    print(resq.json())

# 客户信息查询接口-查询成功
def test_custInfoQuery_000():
    api = goodlife_api.CustInfoQuery_Api.api
    payload = goodlife_custInfoQuery_135_data.cases[0]["case"]
    resq = goodlife_req(host=host, api=api, payload=payload)
    print(resq.json())

# 客户信息查询接口-客户查询缺certNo，查询失败
def test_custInfoQuery_001():
    api = goodlife_api.CustInfoQuery_Api.api
    payload = goodlife_custInfoQuery_135_data.cases[1]["case"]
    resq = goodlife_req(host=host, api=api, payload=payload)
    print(resq.json())

def test_prodApplyResult_000():
    api = goodlife_api.ProdApplyResult_Api.api
    payload = goodlife_custInfoQuery_135_data.cases[1]["case"]
    resq = goodlife_req(host=host, api=api, payload=payload)
    print(resq.json())

if __name__ == '__main__':
    # test_prodApply_000()
    test_custInfoQuery_000()
    test_custInfoQuery_001()

