# -*- encoding: utf-8 -*-
'''
@File    :   trade_query_data.py
@Time    :   2020/11/26 09:01:37
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   单笔订单查询用例 
'''

# here put the import lib

import time,random
#channel = "00000010"
channel = "99999998"
class Trade_query_135_data():
    cases = [
        {
            "title":"000-查询支付成功，查询成功",
            "expection":"",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"2020112506590066"}}
        },
        {
            "title":"001-查询支付失败，查询成功",
            "expection":"",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"2020112506590065"}}
        },
        {
            "title":"003-查询支付中，查询成功",
            "expection":"",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"M20201125121211001"}}
        },
        {
            "title":"004-outTxNo，为空，查询无结果",
            "expection":"",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":""}}
        },
        {
            "title":"005-outTxNo，不存在，查询无结果",
            "expection":"",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"M2020112512121100134"}}
        },
        {
            "title":"006-outTxNo，不当前渠道，查询无结果",
            "expection":"",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"M20201125121211010"}}
        },
        {
            "title":"007-outTxNo，长度超过50，查询无结果",
            "expection":"",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"M2020112512121101022M202011251212110102212345678901"}}
        },
    ]


class Trade_query_100_data():
    """100环境测试数据"""
    cases = [
        {
            "title":"000-查询支付成功，查询成功",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"A20201126151124000"}}
        },
        {
            "title":"001-查询支付失败，查询成功",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"A20201126151124003"}}
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
            "title":"005-outTxNo，不当前渠道，查询无结果",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"AB20201126145102901"}}
        },
        {
            "title":"006-outTxNo，长度超过50，查询无结果",
            "expection":"ELM-000000000",
            "case":{"channel":channel,"method":"elm.pmt.trade.query","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outTxNo":"M2020112512121101022M202011251212110102212345678901"}}
        },
    ]