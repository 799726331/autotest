# -*- encoding: utf-8 -*-
'''
@File    :   data_002_batchTransfer.py
@Time    :   2020/12/16 11:34:11
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   工行批量支付接口用例
'''

# here put the import lib

import time
import random

channel = "99999998"


class BatchTransfer_icbc_data():
    def __init__(self,bank):
        if bank == "icbc":
            self.pyrCustAccNo = "3602008109001773846"         # 付款方银行账号
            self.pyrAccNm = ""                                  # 付款方银行账号名称
            self.rcvPrtBnkCD = "105375271000"                 # 收款方联行号
            self.rcvPrtCustAccNo = "3602008119200567745"      # 收款方银行账号
            self.rcvPtAcNm = "咐惨温建播茎吻园喝彭魏输移氯"        # 收款方银行账号名称

    def get_case(self):
        cases = [
            {
                "title":"000-全部支付成功：支付成功",
                "expection":["0","0"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"00","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"00","rqsAmt":"9.99","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"000","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"000","rqsAmt":"9.98","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"001-全部支付失败：全部支付失败",
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"00","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"01","rqsAmt":"0.01","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"000","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"000","rqsAmt":"0.51","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":""}]}}
            },
            {
                "title":"002-通过壹链盟校验，部分支付成功，部分支付失败:部分支付成功，部分支付失败", 
                "expection":["0","0"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"02","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"02","rqsAmt":"0.02","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm+"84","ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"002","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"002","rqsAmt":"0.52","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"003-custPyNo重复:全部支付失败", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"03","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"03","rqsAmt":"0.03","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"03","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"003","rqsAmt":"0.53","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"004-单位时间支付金额与账号重复", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"04","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"04","rqsAmt":"0.04","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"004","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"004","rqsAmt":"0.04","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}

            },
            {
                "title":"005-14001581301059666666付款账号不在壹链盟平台", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"05","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"05","rqsAmt":"0.05","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"005","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"005","rqsAmt":"0.55","pyrCustAccNo":"14001581301059666666","rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"006-单笔支付额度限制", 
                "expection":"2",
                "case":""

            },
            {
                "title":"007-支付金额位数校验:整数:支付成功", 
                "expection":["0","0"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"07","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"07","rqsAmt":"7","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"007","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"007","rqsAmt":"7.00","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}

            },
            {
                "title":"008-支付金额位数校验:小数点1位：支付成功", 
                "expection":["0","0"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"08","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"08","rqsAmt":"0.8","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"008","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"008","rqsAmt":"0.58","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"009-支付金额位数校验:小数点3位:全部支付失败", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"09","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"09","rqsAmt":"0.009","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"009","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"009","rqsAmt":"0.59","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"010-支付金额位数校验:中文：支付失败", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"10","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"10","rqsAmt":"一百","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"010","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"010","rqsAmt":"0.60","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"011-支付金额位数校验:字母:支付失败", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"11","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"11","rqsAmt":"1.o0","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"011","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"011","rqsAmt":"0.61","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"012-付款账号名称与付款账号不一致", 
                "expection":["0","0"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"12","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"12","rqsAmt":"0.12","docUser":"","pyReCo":"付款公司名称","pyrDepBnkNm":"中国农业银行","pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":"12180001040011850","pyrAccNm":self.pyrAccNm+"222","pyrAccCgyCd":"02","pyrAdr":"付款方地址","rcvCy":"中国","rcvPr":"广东省","rcvCity":"广州市","settMod":"线上支付","mkrCom":"制单公司","rcvPrtDepBnkNm":"收款方开户行名称","rcvPrtDepBnkNo":"","rcvPrtBnkCD":"105375271000","rcvPrtBnkCgyCd":"01","rcvPrtCustAccNo":"12180001040015323","rcvPtAcNm":"合卑办孔泸仪拥戕予慊观速","rcvPtAcCgyCd":"01","rcvPrtAdr":"收款方地址","urgntTpCd":"01","useNm":"用途名称","rmrk":"用途","cstMblPhNo":"13044444444","sMSCntnt":"短信内容","emailAdr":"123@qq.com","mailCntDsc":"邮件内容描述","rstNoticeUrl":"","ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"012","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"012","rqsAmt":"0.52","docUser":"","pyReCo":"付款公司名称","pyrDepBnkNm":"中国农业银行","pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":"12180001040011850","pyrAccNm":"曹绘金状彤妲于慊官送","pyrAccCgyCd":"02","pyrAdr":"付款方地址","rcvCy":"中国","rcvPr":"广东省","rcvCity":"广州市","settMod":"线上支付","mkrCom":"制单公司","rcvPrtDepBnkNm":"建行天长市支行","rcvPrtDepBnkNo":"","rcvPrtBnkCD":"105375271000","rcvPrtBnkCgyCd":"01","rcvPrtCustAccNo":"12180001040015323","rcvPtAcNm":"合卑办孔泸仪拥戕予慊观速","rcvPtAcCgyCd":"01","rcvPrtAdr":"收款方地址","urgntTpCd":"01","useNm":"用途名称","rmrk":"用途","cstMblPhNo":"13044444444","sMSCntnt":"短信内容","emailAdr":"123@qq.com","mailCntDsc":"邮件内容描述","rstNoticeUrl":"","ccyCd":"CNY"}]}}
            },
            {
                "title":"013-收款账号与收款账号名称不一致", 
                "expection":["0","0"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"13","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"13","rqsAmt":"0.13","docUser":"","pyReCo":"付款公司名称","pyrDepBnkNm":"中国农业银行","pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":"12180001040011850","pyrAccNm":self.pyrAccNm,"pyrAccCgyCd":"02","pyrAdr":"付款方地址","rcvCy":"中国","rcvPr":"广东省","rcvCity":"广州市","settMod":"线上支付","mkrCom":"制单公司","rcvPrtDepBnkNm":"收款方开户行名称","rcvPrtDepBnkNo":"","rcvPrtBnkCD":"105375271000","rcvPrtBnkCgyCd":"01","rcvPrtCustAccNo":"12180001040015323","rcvPtAcNm":self.rcvPtAcNm+"2","rcvPtAcCgyCd":"01","rcvPrtAdr":"收款方地址","urgntTpCd":"01","useNm":"用途名称","rmrk":"用途","cstMblPhNo":"13044444444","sMSCntnt":"短信内容","emailAdr":"123@qq.com","mailCntDsc":"邮件内容描述","rstNoticeUrl":"","ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"013","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"013","rqsAmt":"0.53","docUser":"","pyReCo":"付款公司名称","pyrDepBnkNm":"中国农业银行","pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":"12180001040011850","pyrAccNm":"曹绘金状彤妲于慊官送","pyrAccCgyCd":"02","pyrAdr":"付款方地址","rcvCy":"中国","rcvPr":"广东省","rcvCity":"广州市","settMod":"线上支付","mkrCom":"制单公司","rcvPrtDepBnkNm":"建行天长市支行","rcvPrtDepBnkNo":"","rcvPrtBnkCD":"105375271000","rcvPrtBnkCgyCd":"01","rcvPrtCustAccNo":"12180001040015323","rcvPtAcNm":"合卑办孔泸仪拥戕予慊观速","rcvPtAcCgyCd":"01","rcvPrtAdr":"收款方地址","urgntTpCd":"01","useNm":"用途名称","rmrk":"用途","cstMblPhNo":"13044444444","sMSCntnt":"短信内容","emailAdr":"123@qq.com","mailCntDsc":"邮件内容描述","rstNoticeUrl":"","ccyCd":"CNY"}]}}

            },
            {
                "title":"014-custPyNo为空", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"14","rqsAmt":"0.14","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"014","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"014","rqsAmt":"0.64","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
        
            {
                "title":"015-pyrCustAccNo付款账号为空", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"15","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"15","rqsAmt":"0.15","pyrCustAccNo":"","rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"015","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"015","rqsAmt":"0.65","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            
            {
                "title":"016-rcvPrtBnkCD收款方联行号为空", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"16","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"16","rqsAmt":"0.16","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":"","rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"016","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"016","rqsAmt":"0.66","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"017-rcvPrtCustAccNo收款方客户账号为空",
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"17","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"17","rqsAmt":"0.17","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":"","rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"017","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"017","rqsAmt":"0.67","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"018-rcvPtAcNm收款方账户名称为空",
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"18","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"18","rqsAmt":"0.18","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":"","ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"018","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"018","rqsAmt":"0.68","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"019-rqsAmt为空",
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"19","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"19","rqsAmt":"","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"019","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"019","rqsAmt":"0.69","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"020-ccyCd为空",
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"20","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"20","rqsAmt":"0.20","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":""},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"020","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"020","rqsAmt":"0.70","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"021-ccyCd为7位字符",
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"21","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"21","rqsAmt":"0.21","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNYCNYCNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"021","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"021","rqsAmt":"0.71","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"022-rcvPtAcNm收款方账户名称为",
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"22","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"22","rqsAmt":"0.22","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":"发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德","ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"022","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"022","rqsAmt":"0.72","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"023-rcvPrtCustAccNo收款方客户账号为101",
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"23","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"23","rqsAmt":"0.23","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901","rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"023","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"023","rqsAmt":"0.73","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"024-rcvPrtBnkCD收款方联行号为43位", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"24","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"24","rqsAmt":"0.16","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":"12345678901234567890123456789012345678901234","rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"024","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"024","rqsAmt":"0.74","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"025-pyrCustAccNo付款账号为101位", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"25","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"25","rqsAmt":"0.25","pyrCustAccNo":"123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012","rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"025","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"025","rqsAmt":"0.75","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"026-custPyNo为65位", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"261234567890012345678901234567890123456789001236","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"26","rqsAmt":"0.16","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"026","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"026","rqsAmt":"0.76","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"027-docNo为空", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"27","docNo":"","rqsAmt":"0.27","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"027","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"027","rqsAmt":"0.77","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            },
            {
                "title":"028-docNo为65位", 
                "expection":["-1","-1"],
                "case":{"channel":channel,"data":{"commonInput":{"version":"01","channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","remark":"批量支付"},"transfers":[{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"28","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"2612345678900123456789012345678901234567890012328","rqsAmt":"0.28","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"},{"custPyNo":"icBC"+time.strftime("%Y%m%d%H%M%S")+"028","docNo":"ICBC"+time.strftime("%Y%m%d%H%M%S")+"028","rqsAmt":"0.78","pyrCustAccNo":self.pyrCustAccNo,"rcvPrtBnkCD":self.rcvPrtBnkCD,"rcvPrtCustAccNo":self.rcvPrtCustAccNo,"rcvPtAcNm":self.rcvPtAcNm,"ccyCd":"CNY"}]}}
            }  
        ]
        return cases

if __name__ == "__main__":
    print(BatchTransfer_100_data("abc").get_case()[0]["case"])