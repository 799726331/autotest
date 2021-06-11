# -*- encoding: utf-8 -*-
'''
@File    :   trade_pay_data.py
@Time    :   2020/11/20 17:04:19
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   农行-统一支付用例
'''

# here put the import lib

import time
import random

channel = "99999998"

pyrAcctNo = "12180001040011850"      # 付款方账号
pyrAcctName = "曹绘金状彤妲于慊官送"                # 付款方账号名称
rcvAcctNo = "12180001040015323"       # 收款方账号
rcvAcctName = "合卑办孔泸仪拥戕予慊观速"                  # 收款方账户名称

class Trade_pay_abc_data():
    """建行-统一支付用例"""
    cases = [
        {
            "title":"000-支付成功",
            "expection":"1",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"flajslkfjsalkfjlkdsajf","nonceStr":"fdslkjflkdsjflksjf","key":"fjsdalkfjlsaj","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"000","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"000","pyrDepBankName":"","pyrDepBankNo":"","pyrBankCgy":"","pyrAcctNo":pyrAcctNo,"pyrAcctName":pyrAcctName,"pyrAcctCgy":"","rcvDepBankName":"","rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":"1.53","useName":"的时间发了","remark":"凡涉及多方了解萨拉","outExtData":"范德萨发撒地方"}}
        },
        {
            "title":"001-仅必填字段，支付成功",
            "expection":"1",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"001","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"001","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"002-客户订单号重复outTxNo，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"20201123101944064","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"002","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"003-客户业务编号重复outBizNo(已支付成功)，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"003","outBizNo":"20201123101944064","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"004-客户业务编号重复outBizNo（支付失败），可支付成功",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"004","outBizNo":"20201124094646001","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"005-客户订单号outTxNo，含有中文，支付成功",
            "expection":"1",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"一","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"005","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"006-客户订单号outTxNo，含有非指定特殊符号，支付成功",
            "expection":"1",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+".-","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"006","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"007-金额校验txAmt，整数，支付成功",
            "expection":"1",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"007","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"007","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3)),"useName":"123456"}}
        },
        {
            "title":"008-金额校验txAmt，1位小数，支付成功",
            "expection":"1",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"008","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"008","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".1","useName":"123456"}}
        },
        {
            "title":"009-金额校验txAmt，3位小数，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"009","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"009","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".101","useName":"123456"}}
        },
        {
            "title":"010-金额校验txAmt，负数，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"010","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"010","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":"-"+str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"011-金额校验txAmt，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"011","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"011","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":"","useName":"123456"}}
        },
        {
            "title":"012-金额校验txAmt，支付长度校验大于16位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"012","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"012","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":"12345678901234567","useName":"123456"}}
        },
        {
            "title":"013-支付场景payScene，非指定场景，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"Q00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"013","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"013","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"014-支付场景payScene，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"014","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"014","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"015-支付产品payProduct，非指定场景，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"Y00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"015","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"015","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"016-支付产品payProduct，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"016","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"016","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"017-支付产品payProduct，长度超过7位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P000001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"017","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"017","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"018-支付场景payScene，长度超过7位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S000001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"018","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"018","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"019-客户订单号outTxNo，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"019","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"020-客户订单号outTxNo，长度为51，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"0200000000000000000000000000000000001","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"020","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"021-客户业务单据编号outBizNo，长度为51，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"021","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"0200000000000000000000000000000000002","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"022-客户业务单据编号outBizNo，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"022","outBizNo":"","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"023-付款方账号，pyrAcctNo，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"023","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"023","pyrAcctNo":"","rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"024-付款方账号，pyrAcctNo，长度为61，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"024","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"024","pyrAcctNo":"4400158130105966666600000000000000000000000009999999999999999","rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"025-收款方开户行号，rcvDepBankNo，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"025","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"025","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"026-收款方开户行号，rcvDepBankNo，长度为13，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"026","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"026","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"1055210000610","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"027-收款方行类别，rcvBankCgy，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"027","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"027","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"028-收款方行类别，rcvBankCgy，长度为3，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"028","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"028","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"001","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"029-收款方行类别，rcvBankCgy，非默认值，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"029","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"029","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"04","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"030-收款方账号，rcvAcctNo，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"030","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"030","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":"","rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"031-收款方账号，rcvAcctNo，长度61位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"031","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"031","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":"6227003320590089522000000000000000000033333333333355555555555","rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"032-收款方账户名称，rcvAcctName，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"032","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"032","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":"","rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"033-收款方账户名称，rcvAcctName，长度121，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"033","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"033","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":"姚九九法律框架萨夫斯基开发技术法律框架萨夫斯基开发技术法律框架萨夫斯基开发技术法律框架萨夫斯基开发技术法律框架萨夫斯基开发技术法律框架萨夫斯基开发技术姚九九法律框架萨夫斯基开发技术法律框架萨夫斯基开发技术法律框架萨夫斯基开发技术法律框架萨夫负","rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"034-收款方账户类别，rcvAcctCgy，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"034","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"034","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"035-收款方账户类别，rcvAcctCgy，长度3，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"035","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"035","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"002","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"036-收款方账户类别，rcvAcctCgy，非默认值，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"036","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"036","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"08","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"037-币种，currCode，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"037","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"037","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"038-币种，currCode，4位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"038","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"038","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNHY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"039-币种，currCode，非默认值，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"039","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"039","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNHY","txAmt":str(random.randint(1,3))+".01","useName":"123456"}}
        },
        {
            "title":"040-用途名称，useName，为空，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"040","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"040","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":""}}
        },
        {
            "title":"041-用途名称，useName，长度501，支付失败",
            "expection":"2",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"041","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"041","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"kdsjflkdsajlkfjdslkjflkdsjflkjdslkfjlkdsjflkdsajflkjdslkfjlkdsjflksdlkjflkdsjflkjdslkfjdslkjflkdsfdsfdsfjfsdflkdsjflkdsajlkfjdslkjflkdsjflkjdslkfjlkdsjflkdsajflkjdslkfjlkdsjflksdlkjflkdsjflkjdslkfjdslkjflkdsfdsfdsfjfsdflkdsjflkdsajlkfjdslkjflkdsjflkjdslkfjlkdsjflkdsajflkjdslkfjlkdsjfdsfsdfdsfdsaflksdlkjflkdsjflkjdslkfjdslkjflkdsfdsfdsfjfsdflkdsjflkdsajlkfjdslkjflkdsjflkjdslkfjlkdsjflkdsajflkjdsfdsafdsafsfdsfdsfdsfdsfdsfljflkdsjsfdsaffdsfdsafdsafsdfdsafsdaflkjdslkfjdsljflkdsjflkjdslkfjdslkjfsfdsfd"}}
        },
        {
            "title":"042-渠道号不正确，支付失败",
            "expection":"Internal Server Error",
            "case":{"channel":"9876543","method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"042","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"042","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"765"}}
        },
        {
            "title":"043-路由method不正确，支付失败",
            "expection":"不存在的方法名",
            "case":{"channel":channel,"method":"elm.pmt.trade1.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"043","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"043","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"765"}}
        },
        {
            "title":"044-字符集非utf-8，支付失败",
            "expection":"字符集错误",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-80","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"044","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"044","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"765"}}
        },
        {
            "title":"045-请求时间格式非法，支付失败",
            "expection":"非法的时间戳参数",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y%m%d %H:%M:%S"),"version":"1.0","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"045","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"045","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"765"}}
        },
        {
            "title":"046-版本号非1.0，支付失败",
            "expection":"不存在的方法名",
            "case":{"channel":channel,"method":"elm.pmt.trade.pay","charset":"UTF-8","reqDateTime":time.strftime("%Y-%m-%d %H:%M:%S"),"version":"1.00","notifyUrl":"","authToken":"5d1ceafcbd05470ca2fe969bed2e6151","nonceStr":"b4rtOaBYPqmtfca2WWs8443M1IPKQI0K","key":"UZ9jHX56tgHWAav9","signType":"RSA","signStr":"wrwrw","md5Str":"","bizCnt":{"payScene":"S00001","payProduct":"P00001","outTxNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"046","outBizNo":"ABC"+time.strftime("%Y%m%d%H%M%S")+"046","pyrAcctNo":pyrAcctNo,"rcvDepBankNo":"105521000061","rcvBankCgy":"01","rcvAcctNo":rcvAcctNo,"rcvAcctName":rcvAcctName,"rcvAcctCgy":"02","currCode":"CNY","txAmt":str(random.randint(1,3))+".01","useName":"765"}}
        }
    ]


if __name__ == "__main__":
    print(Trade_pay_abc_data().cases[1]["case"])