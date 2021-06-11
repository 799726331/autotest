# -*- encoding:utf-8 -*-
'''
@File    :  pay_req.py
@Time    :  2020/11/23 10:02:28
@Author  :  lzx
@Version :  Python 3.7.6
@State   :  支付平台公共请求 
'''

# here put the import lib

import os,sys
sys.path.append(os.getcwd().split("scripts1",1)[0])
from scripts1.apis.pay import common_api
from scripts1.utils.host import HOST
from scripts1.utils.log import GetLog
import traceback
import requests
import json

log = GetLog().pay_Log()
header = {'Content-Type':'application/json',"Accept-Encoding":""}


def reqEncrySign_v2_req(host,params):
    """加密"""
    try:
        api = common_api.ReqEncrySign_V2.api
        method = common_api.ReqEncrySign_V2.method
        url = HOST[host] + api
        payload = json.dumps(params)
        log.logger.info("加密地址：{}".format(url))
        log.logger.info("加密报文：{}".format(params))
        resp = requests.request(method,url,headers=header,data=payload)
        return resp
    except Exception as f:
        log.logger.error("加密报文：{}".format(params))
        log.logger.error(traceback.format_exc())


def rspDecry_v2_req(host,channel,params):
    """解密"""
    try:
        rspDecry_v2 = common_api.RspDecry_V2(channel)
        api = rspDecry_v2.api
        method = rspDecry_v2.method
        url = HOST[host]+api
        payload = json.dumps(params)
        log.logger.info("解密地址：{}".format(url))
        log.logger.info("解密报文：{}".format(params))
        resp = requests.request(method,url,headers=header,data=payload)
        return resp
    except Exception as f:
        log.logger.error("解密报文：{}".format(params))
        log.logger.error(traceback.format_exc())


def pay_req(host,api,payload,channel="00000010",method="post"):
    try:
        if host == "135":
            pay_host = "135_pay_host"
        elif host == "100":
            pay_host = "100_pay_host"
        elif host == "pre":
            pay_host = "pre_pay_host"

        # 加密
        row_resp = reqEncrySign_v2_req(host,payload)

        if row_resp.status_code == 500:
            log.logger.info("加密请求状态：{}".format(row_resp.status_code))
            log.logger.info("业务报文：{}".format(row_resp.json()))
            return row_resp

        else:
            params = json.dumps(row_resp.json())

            url = HOST[pay_host] + api

            log.logger.info("业务地址：{}".format(url))
            log.logger.info("业务报文：{}".format(params))

            # 业务请求
            print(params)
            resp = requests.request(method,url,headers=header,data=params)

            if "key" in resp.json().keys():
                
                # 解密请求
                result = rspDecry_v2_req(host,channel,resp.json())
                log.logger.info("解密响应：{}".format(result.json()))
                return result
            else:
                log.logger.info("业务响应：{}".format(resp.json()))
                return resp

    except Exception as f:
        log.logger.error("请求报文：{}".format(params))
        log.logger.error(traceback.format_exc())


if __name__ == "__main__":
    params = {
        "channel":"00000010",
        "method":"elm.pmt.trade.pay",
        "charset":"UTF-8",
        "reqDateTime":"2020-11-24 12:19:44",
        "version":"1.0",
        "notifyUrl":"",
        "authToken":"5d1ceafcbd05470ca2fe969bed2e6151",
        "nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K",
        "key":"UZ9jHX56tgHWAav9",
        "signType":"RSA",
        "signStr":"wrwrw",
        "md5Str":"",
        "bizCnt":{
            "payScene":"S00001",
            "payProduct":"P00001",
            "outTxNo":"20201124101944005",
            "outBizNo":"20201124101944005",
            "pyrAcctNo":"44001581301059666666",
            "rcvDepBankNo":"105521000061",
            "rcvBankCgy":"01",
            "rcvAcctNo":"6227003320590089522",
            "rcvAcctName":"姚九九",
            "rcvAcctCgy":"02",
            "currCode":"CNY",
            "txAmt":"1.01",
            "useName":"123456"
        }
    }    
    api = "/api/v2/pmt/trade/pay"
    reps = pay_req("135",api,params,"00000010")
    print(reps.json())

