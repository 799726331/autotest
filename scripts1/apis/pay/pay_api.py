# -*- encoding: utf-8 -*-
'''
@File    :   pay_api.py
@Time    :   2020/11/19 16:17:17
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   大支付平台业务接口 
'''

# here put the import lib

class Trade_pay():
    """统一付款接口"""
    api = "/api/v2/pmt/trade/pay"
    method = "post"

class Trade_pay_batch():
    """批量付款接口"""
    api = "/api/v2/pmt/trade/pay/batch"
    method = "post"

class Trade_pay_batch_query():
    """批量支付结果查询接口"""
    api = "/api/v2/pmt/trade/pay/batch/query"
    method = "post"

class Trade_query():
    """单笔订单查询"""
    api = "/api/v2/pmt/trade/query"
    method = "post"

class Trade_query_batch():
    """批量订单查询"""
    api = "/api/v2/pmt/trade/query/batch"
    method = "post"

