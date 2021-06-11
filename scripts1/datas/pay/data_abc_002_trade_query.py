# -*- encoding: utf-8 -*-
'''
@File    :   trade_query_data.py
@Time    :   2020/11/26 09:01:37
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   农行-单笔订单查询用例 
'''

# here put the import lib

import time,random

channel = "99999998"

class Trade_query_abc_data():
    """农行-单笔订单查询"""
    cases = [
        {
            "title":"000-查询支付成功，查询成功",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"ABCB20201229150530000"}}
        },
        {
            "title":"001-查询支付失败，查询成功",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"ABCA20201229150530000"}}
        },
        {
            "title":"002-查询支付中，查询成功",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"B20201126151124000"}}
        },
        {
            "title":"003-outTxNo，为空，查询无结果",
            "expection":"ELM-800030000",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":""}}
        },
        {
            "title":"004-outTxNo，不存在，查询无结果",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"M2020112512121100134"}}
        },
        {
            "title":"005-outTxNo，不在当前渠道，查询无结果",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"AB20201126145102901"}}
        },
        {
            "title":"006-outTxNo，长度超过50，查询无结果",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"M2020112512121101022M202011251212110102212345678901"}}
        }
    ]