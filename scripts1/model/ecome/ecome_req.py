# -*- encoding: utf-8 -*-
'''
@File    :   ecome_req.py
@Time    :   2020/10/13 15:29:38
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   佣金e收公共请求类 
'''

# here put the import lib
import sys
import os
sys.path.append(os.getcwd().split("scripts1",1)[0])
from scripts1.apis.ecome.ecome_apis import *
from scripts1.utils.host import HOST         
from scripts1.utils.log import GetLog
import traceback
import requests
import json

log = GetLog.ecome_log

header = {'Content-Type': 'application/json'}


# 加密
def ReqEncrySign(host,payload):
    """参数加密接口"""
    try:
        params = json.dumps(payload)
        #log.logger.info("{}:{}".format("加密前参数",params))
        api,method = ReqEncryApi.api,ReqEncryApi.method
        url = HOST[host] + api    
        resp = requests.request(method, url,headers=header,data=params)
        return resp.json()
    except Exception as r:
        log.logger.error("{}:{}".format("加密前参数",payload))
        log.logger.error(traceback.format_exc)
        

# 解码
def RspDecry(host,payload):
    """参数解密接口"""
    try:
        params = json.dumps(payload)
        api = RspDecryApi.api
        method = RspDecryApi.method
        url = HOST[host] + api    
        #log.logger.info("{}:{}".format("解密参数",params))
        resp = requests.request(method, url,headers=header,data=params)
        log.logger.info("{}:{}".format("返回报文",resp.json()))
        return resp
    except Exception as r:
        log.logger.error("{}:{}".format("解密参数",params))
        log.logger.error(traceback.format_exc)


# 业务功能
def ecome_req(host,payload,api,method="post"):
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

        # 业务功能
        params = json.dumps(params)
        url = HOST[host] + api
        #log.logger.info("{}:{}".format("加密后参数",params))
        resp = requests.request(method,url,data=params,headers=header)
        
        # 返回值解密
        result = RspDecry(host,resp.json())
        return result

    except Exception as r:
        log.logger.error("{}:{}".format("加密后参数",payload))
        log.logger.error(traceback.format_exc)
    