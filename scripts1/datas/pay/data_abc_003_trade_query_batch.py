# -*- encoding: utf-8 -*-
'''
@File    :   trade_query_batch_data.py
@Time    :   2020/11/26 10:11:13
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   农行-批量订单查询用例数据 
'''

# here put the import lib
import time,random

channel = "99999998"

class Trade_query_batch_abc_data():
    cases = [
        {
            "title":"000-查询成功",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"","startDate":"","endDate":"","outset":"0","offset":"2","rstSts":"","txType":""}}
        },
        {
            "title":"001-查询条数超过100",
            "expection":"最大支持查询100笔",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"","startDate":"","endDate":"","outset":"0","offset":"101","rstSts":"","txType":""}}
        },
        {
            "title":"002-查询指定日期，查询成功",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"","startDate":"20201124","endDate":"20201126","outset":"0","offset":"2","rstSts":"","txType":""}}
        },
        {
            "title":"003-查询指定outBatchNo，查询成功",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"ABCBN202012291505300000","startDate":"","endDate":"","outset":"0","offset":"2","rstSts":"","txType":""}}
        },
        {
            "title":"004-查询指定交易状态，查询成功",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"","startDate":"","endDate":"","outset":"0","offset":"2","rstSts":"1","txType":""}}
        },
        {
            "title":"005-查询指定txType，查询成功",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"","startDate":"","endDate":"","outset":"0","offset":"2","rstSts":"","txType":"001"}}
        },
        {
            "title":"006-查询全条件，查询成功",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"BN202011261451020013","startDate":"20201124","endDate":"20201126","outset":"0","offset":"2","rstSts":"2","txType":"001"}}
        },
        {
            "title":"007-开始日期格式非法，查询无结果",
            "expection":"开始日期格式非法",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"M20201125121211010","startDate":"2020-1124","endDate":"20201124","outset":"0","offset":"2","rstSts":"1","txType":"001"}}
        },
        {
            "title":"008-结束日期格式非法，查询无结果",
            "expection":"结束日期格式非法",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"M20201125121211010","startDate":"20201124","endDate":"2020-11-24","outset":"0","offset":"2","rstSts":"1","txType":"001"}}
        },
        {
            "title":"009-起始笔数等于数据库现存数，查询无结果",
            "expection":"0",
            "case":{"channel":"00000010","method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"","startDate":"","endDate":"","outset":"493","offset":"2","rstSts":"","txType":""}}
        },
        {
            "title":"010-起始笔数超过数据库现存数，查询无结果",
            "expection":"0",
            "case":{"channel":"00000010","method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"","startDate":"","endDate":"","outset":"494","offset":"2","rstSts":"","txType":""}}
        },
        {
            "title":"011-状态非默认值，查询无结果",
            "expection":"交易结果状态码非法",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"","startDate":"","endDate":"","outset":"0","offset":"2","rstSts":"999","txType":""}}
        },
        {
            "title":"012-交易类型非默认值，查询无结果",
            "expection":"交易类型不存在",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"","startDate":"","endDate":"","outset":"0","offset":"2","rstSts":"","txType":"1000"}}
        },
        {
            "title":"013-outBatchNo不存在，查询无结果",
            "expection":"0",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"4242342","startDate":"","endDate":"","outset":"0","offset":"2","rstSts":"","txType":""}}
        },
        {
            "title":"014-outBatchNo存在非当前渠道，查询无结果",
            "expection":"0",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"BH20201126145102900","startDate":"","endDate":"","outset":"0","offset":"2","rstSts":"","txType":""}}
        },
        {
            "title":"015-outBatchNo超过51，查询无结果",
            "expection":"0",
            "case":{"channel":channel,"method":"elm.pmt.trade.query.batch","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"outBatchNo":"112345678901234567890123456789012345678901234567890","startDate":"","endDate":"","outset":"0","offset":"2","rstSts":"","txType":""}}
        }
    ]

if __name__ == "__main__":
    print(Trade_query_batch_abc_data.cases[11]["case"])