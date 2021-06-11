# -*- encoding: utf-8 -*-
'''
@File    :   comon_api.py
@Time    :   2020/10/23 15:10:17
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   支付项目公共api
'''

# here put the import lib


class ReqEncrySign_Api():
    """参数加密"""
    api = "/plumberpay/cxf/mockit/reqEncrySign"
    method = "post"

class RspDecry_Api():
    """参数解密"""
    api = "/plumberpay/cxf/mockit/rspDecry"
    method = "post"
