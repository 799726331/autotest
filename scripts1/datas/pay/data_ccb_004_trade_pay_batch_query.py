# -*- encoding: utf-8 -*-
'''
@File    :   trade_pay_batch_query.py
@Time    :   2020/11/26 09:43:27
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   建行-批量支付查询用例数据
'''

# here put the import lib

import time,random

channel="99999998"

class Trade_pay_batch_query_ccb_data():
    """建行-批量支付查询用例数据"""
    cases = [
        {
            "title":"000-查询成功",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"charset":"UTF-8","method":"elm.pmt.trade.pay.batch.query","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"BN202011261451020019"}}
        },
        {
            "title":"001-查询非当前渠道，查询无结果",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"charset":"UTF-8","method":"elm.pmt.trade.pay.batch.query","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"BN202011261451020018"}}
        },
        {
            "title":"002-outBatchNo,为空，查询无结果",
            "expection":"客户批次号不为空",
            "case":{"channel":channel,"charset":"UTF-8","method":"elm.pmt.trade.pay.batch.query","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":""}}
        },
        {
            "title":"003-outBatchNo,不存在，查询无结果",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"charset":"UTF-8","method":"elm.pmt.trade.pay.batch.query","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"345678987654"}}
        },
        {
            "title":"004-outBatchNo,长度超50，查询无结果",
            "expection":"客户批次号格式非法",
            "case":{"channel":channel,"charset":"UTF-8","method":"elm.pmt.trade.pay.batch.query","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"123456789012345678901234567890123456789012345678901"}}
        }
    ]