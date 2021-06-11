'''
@File    :   goodlife_req.py
@Time    :   2021/1/11 21:10 
@Author  :   卢梓轩 
@Version :   Python 3.7.6
@State   :   
'''

import os
import sys
sys.path.append(os.getcwd().split("scripts1",1)[0])
from scripts1.apis.goodlife import common_api
from scripts1.utils.host import HOST
from scripts1.utils.log import GetLog
import traceback
import requests
import json

log = GetLog().goodlife_Log()
header = {'Content-Type':'application/json'}


# 加密方法
def ReqEncrySign(host,params):
    try:
        api = common_api.ReqEncrySign_Api.api
        method = common_api.ReqEncrySign_Api.method
        url = HOST[host] + api
        payload = json.dumps(params)
        log.logger.info("加密地址：{}".format(url))
        log.logger.info("加密报文：{}".format(params))
        resp = requests.request(method,url,headers=header,data=payload)
        return resp
    except Exception as e:
        log.logger.error("加密请求失败,失败原因:{}".format(e))
        log.logger.error("加密报文：{}".format(params))
        log.logger.error(traceback.format_exc())
# 解密方法
def RspDecry(host,params):
    try:
        api = common_api.RspDecry_Api.api
        method = common_api.RspDecry_Api.method
        url = HOST[host]+api
        payload = json.dumps(params)
        resp = requests.request(method,url,headers=header,data=payload)
        log.logger.info("解密地址：{}".format(url))
        log.logger.info("解密报文：{}".format(resp.json()))
        return resp
    except Exception as e:
        log.logger.error("解密请求失败,失败原因:{}".format(e))
        log.logger.error("解密报文：{}".format(params))
        log.logger.error(traceback.format_exc())

# 好生活请求方法
def goodlife_req(host,api,payload,method = "post"):
    try:
        row_resp = ReqEncrySign(host,payload)
        if row_resp.status_code == 200:
            params = json.dumps(row_resp.json())
            url = HOST[host] + api
            log.logger.info("业务地址：{}".format(url))
            log.logger.info("业务报文：{}".format(params))
            resp = requests.request(method,url,headers=header,data=params)
            result = RspDecry(host,resp.json())
            return result
        else:
            log.logger.info("加密响应为失败")
            log.logger.info("加密请求状态：{}".format(row_resp.status_code))
            log.logger.info("业务报文：{}".format(row_resp.json()))
            return row_resp
    except Exception as e:
        log.logger.error("业务请求失败,失败问题:{}".format(e))
        log.logger.error("{}:{}".format("业务参数", payload))
        log.logger.error(traceback.format_exc)



if __name__ == '__main__':
    from scripts1.apis.goodlife import goodlife_api
    # sys.path.append(os.getcwd().split("scripts1", 1)[0])
    from scripts1.datas.goodlife.data_000_custInfoQuery import goodlife_custInfoQuery_135_data
    host = "23"
    api = "/plumber/cxf/chnel/v1/customer/custInfoQuery"
    payload = goodlife_custInfoQuery_135_data().cases[0]["case"]
    # print(type(json.dumps(payload)))

    # reqs = goodlife_req(host,api,payload)

    reqs = ReqEncrySign(host,params=payload)
    print(reqs)



    # reqs = ReqEncrySign(host,payload)
    # print(reqs.json())