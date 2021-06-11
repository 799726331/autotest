# -*- encoding: utf-8 -*-
'''
@File    :   bank_req.py
@Time    :   2020/10/09 15:28:26
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   自定义建行请求方法
'''

# here put the import lib

import sys
import os
sys.path.append(os.getcwd().split("scripts1",1)[0])
from scripts1.apis.bank.ccb_api import *
from scripts1.apis.bank import common_api

from scripts1.utils.host import HOST         
from scripts1.utils.log import GetLog
import traceback
import requests
import json

log = GetLog().bank_Log()

header = {'Content-Type':'application/json',"Accept-Encoding":""}

# 加密
def ReqEncrySign(host,payload):
    """参数加密接口"""
    try:
        api = common_api.ReqEncrySign_Api.api
        method = common_api.ReqEncrySign_Api.method
        params = json.dumps(payload)
        url = HOST[host] + api   
        log.logger.info("加密地址：{}".format(url))
        log.logger.info("{}:{}".format("加密参数",json.dumps(payload,ensure_ascii=False)))
        resp = requests.request(method, url,headers=header,data=params)
        return resp.json()
    except Exception as r:
        log.logger.error("{}:{}".format("加密参数",json.dumps(payload,ensure_ascii=False)))
        log.logger.error(traceback.format_exc)
        

# 解码
def RspDecry(host,payload):
    """参数解密接口"""
    try:
        params = json.dumps(payload)
        api = common_api.RspDecry_Api.api
        method = common_api.RspDecry_Api.method
        url = HOST[host] + api
        log.logger.info("解密地址：{}".format(url))    
        log.logger.info("{}:{}".format("解密参数",params))
        resp = requests.request(method, url,headers=header,data=params)
        log.logger.info("{}:{}".format("返回报文",resp.json()))
        return resp
    except Exception as r:
        log.logger.error("{}:{}".format("解密参数",json.dumps(payload)))
        log.logger.error(traceback.format_exc)


# 业务功能
def bank_req(host,payload,api,method="post"):
    """
        params:
            host: ip
            payload：请求参数
            api: 接口
            method：请求方式，默认post
    """

    try:
        # 参数加密
        params = ReqEncrySign(host,payload)
        print(params)
        # 业务功能
        params = json.dumps(params)
        url = HOST[host] + api
        log.logger.info("业务地址：{}".format(url))
        log.logger.info("{}:{}".format("业务参数",params))
        resp = requests.request(method,url,data=params,headers=header)
        # print(resp)
        # 返回值解密
        result = RspDecry(host,resp.json())
        return result

    except Exception as r:
        log.logger.error("{}:{}".format("业务参数",payload))
        log.logger.error(traceback.format_exc)
    
if __name__ == '__main__':
    from scripts1.apis.goodlife import goodlife_api
    from scripts1.datas.goodlife.data_000_custInfoQuery import goodlife_query_data
    host = "135"
    api = HOST[host] + goodlife_api.CustInfoQuery_Api().api
    payload = goodlife_query_data().cases[0]["case"]
    reqs = bank_req(host,api,payload)
    print(reqs)