# -*- encoding: utf-8 -*-
'''
@File    :   data_000_transfer.py
@Time    :   2020/12/11 14:19:40
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   bank银行单笔支付用例
'''

# here put the import lib
import time
import random
channel = "99999998"

pyrDepBnkNm = ""                                # 付款方开户行名称,非必填
pyrCustAccNo = "44001581301059666666"          # 付款方客户账号
pyrAccNm = ""                                   # 付款方账户名称,非必填
rcvPrtDepBnkNm =""                              # 收款方开户行名称,非必填
rcvPrtBnkCD = "105375271000"                    # 收款方联行号
rcvPrtCustAccNo = "6227003320590089522"         # 收款方客户账号
rcvPtAcNm = "姚九九"                             # 收款方账户名称

class Transfer_ccb_Data():
    """
        人民币单笔付款
    """
    cases = [
        {
            "title":"000-支付成功",
            "expection":"1",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0000","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0000","rqsAmt":"1.01","docUser":"单据制单用户","pyReCo":"付款公司名称","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"02","pyrAdr":"付款方地址","rcvCy":"中国","rcvPr":"广东省","rcvCity":"广州市","settMod":"线上支付","mkrCom":"制单公司","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"01","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"01","rcvPrtAdr":"收款方地址","urgntTpCd":"01","useNm":"用途名称","rmrk":"用途","cstMblPhNo":"13044444444","sMSCntnt":"短信内容","emailAdr":"123@qq.com","mailCntDsc":"邮件内容描述","rstNoticeUrl":"付款结果通知地址","ccyCd":"CNY"}}
        },
        {
            "title":"001-仅必填，支付成功",
            "expection":"1",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0001","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0001","rqsAmt":"0.01","docUser":"","pyReCo":"","pyrDepBnkNm":"","pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":"","pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":"","rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"002-custPyNo重复",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0001","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0002","rqsAmt":"0.02","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"003-custPyNo为空",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0003","rqsAmt":"0.03","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"004-单位时间支付金额与账号重复",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0004","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0004","rqsAmt":"0.01","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"005-付款账号不在壹链盟平台",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0005","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0005","rqsAmt":"0.05","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":"45556773827738343","pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"006-账号禁用",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0006","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0006","rqsAmt":"0.06","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":"45556773827243","pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        }, 
        {
            "title":"007-单笔支付额度限制",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0007","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0007","rqsAmt":"99.99","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"008-支付金额位数校验:整数",
            "expection":"1",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0008","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0008","rqsAmt":"8","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"009-支付金额位数校验:小数点1位",
            "expection":"1",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0009","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0009","rqsAmt":"0.9","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"010-支付金额位数校验:小数点3位",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0010","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0010","rqsAmt":"0.101","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"011-支付金额位数校验:中文",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0011","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0011","rqsAmt":"壹佰","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"012-支付金额位数校验:符号",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0012","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0012","rqsAmt":"￥1.12","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"013-支付金额位数校验:字母",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0013","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0013","rqsAmt":"1.oo","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"014-支付金额位数校验:负数",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0014","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0014","rqsAmt":"-0.14","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"015-付款账号名称与付款账号不一致",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0015","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0015","rqsAmt":"0.15","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":"付款户名称","pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"016-收款账号与收款账号名称不一致",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0016","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0016","rqsAmt":"0.16","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":"收款账号名","rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"017-pyrCustAccNo付款方客户账号为空",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0017","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0017","rqsAmt":"0.17","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":"","pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"018-rcvPrtBnkCD收款方联行号为空",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0018","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0018","rqsAmt":"0.18","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":"","rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        
        {
            "title":"019-rcvPrtCustAccNo收款方客户账号为空",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0019","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0019","rqsAmt":"0.19","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":"","rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"020-rcvPtAcNm收款方账户名称为空",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0020","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0020","rqsAmt":"0.20","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":"","rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"021-rqsAmt请求金额为空",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0021","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0021","rqsAmt":"","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"022-ccyCd币种为空",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0022","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0022","rqsAmt":"0.22","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":""}}
        },

        {
            "title":"023-custPyNo付款方客户账号字符长65位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0023123456789012345678901234567890123456789012023","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0023","rqsAmt":"0.23","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"024-源单据编号docNo空",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0024","docNo":"","rqsAmt":"0.24","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"025-源单据编号docNo字符串65位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0025","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0023123456789012345678901234567890123456789012025","rqsAmt":"0.25","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"026-付款方开户行名称pyrDepBnkNm为空，支付成功",
            "expection":"1",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0026","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0026","rqsAmt":"0.26","docUser":"","pyReCo":"","pyrDepBnkNm":"","pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"027-付款方开户行名称pyrDepBnkNm长601位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0027","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0027","rqsAmt":"0.27","docUser":"","pyReCo":"","pyrDepBnkNm":"发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德","pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"028-付款方账户名称pyrAccNm空，支付成功",
            "expection":"1",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0028","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0028","rqsAmt":"0.28","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":"","pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"029-付款方账户名称pyrAccNm长601位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0029","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0029","rqsAmt":"0.29","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":"发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德","pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"030-收款方开户行名称rcvPrtDepBnkNm空，支付成功",
            "expection":"1",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0030","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0030","rqsAmt":"0.30","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":"","rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"031-收款方开户行名称rcvPrtDepBnkNm长601位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0031","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0031","rqsAmt":"0.31","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":"发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德","rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"032-rcvPrtBnkCD收款方联行号为43位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0032","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0032","rqsAmt":"0.32","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":"12345678901234567890123456789012345678901234","rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"033-rcvPrtCustAccNo收款方客户账号为101位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0033","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0033","rqsAmt":"0.33","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":"42143214344214321434421432143442143214344214321434421432143442143214344214321434123456789012345678901","rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"034-rcvPtAcNm收款方账户名称为601位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0034","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0034","rqsAmt":"0.34","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":"发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德","rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}

        },
        {
            "title":"035-ccyCd币种为7位字符串，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0035","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0035","rqsAmt":"0.35","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNYJKIUY"}}
        },
        {
            "title":"036-用途名称userName长601位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0036","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0036","rqsAmt":"0.36","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德萨发生发顺丰打赏发的撒范德","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"037-收款方账户类别代码rcvPtAcCgyCd长度超过3位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0037","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0037","rqsAmt":"0.37","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"002","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"038-收款方行别代码rcvPrtBnkCgyCd长度超过3位，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0038","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0038","rqsAmt":"0.38","docUser":"","pyReCo":"","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"","pyrAdr":"","rcvCy":"","rcvPr":"","rcvCity":"","settMod":"","mkrCom":"","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"002","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"","rcvPrtAdr":"","urgntTpCd":"","useNm":"","rmrk":"","cstMblPhNo":"","sMSCntnt":"","emailAdr":"","mailCntDsc":"","rstNoticeUrl":"","ccyCd":"CNY"}}
        },
        {
            "title":"039-docNo原单据编号重复，已存在成功，支付失败",
            "expection":"2",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0039","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0000","rqsAmt":"0.39","docUser":"单据制单用户","pyReCo":"付款公司名称","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"02","pyrAdr":"付款方地址","rcvCy":"中国","rcvPr":"广东省","rcvCity":"广州市","settMod":"线上支付","mkrCom":"制单公司","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"01","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"01","rcvPrtAdr":"收款方地址","urgntTpCd":"01","useNm":"用途名称","rmrk":"用途","cstMblPhNo":"13044444444","sMSCntnt":"短信内容","emailAdr":"123@qq.com","mailCntDsc":"邮件内容描述","rstNoticeUrl":"付款结果通知地址","ccyCd":"CNY"}}
        },
        {
            "title":"040-docNo原单据编号重复，已存在失败，支付成功",
            "expection":"1",
            "case":{"channel":channel,"data":{"commonInput":{"channel":channel,"reqDate":time.strftime("%Y%m%d"),"reqTime":time.strftime("%H%M%S"),"bankCode":"105","version":"1.0","remark":"单笔支付"},"custPyNo":"ccb"+time.strftime("%Y%m%d%H%M%S")+"0040","docNo":"ccB"+time.strftime("%Y%m%d%H%M%S")+"0038","rqsAmt":"0.39","docUser":"单据制单用户","pyReCo":"付款公司名称","pyrDepBnkNm":pyrDepBnkNm,"pyrDepBnkNo":"","pyrBnkCD":"","pyrBnkCgyCd":"","pyrCustAccNo":pyrCustAccNo,"pyrAccNm":pyrAccNm,"pyrAccCgyCd":"02","pyrAdr":"付款方地址","rcvCy":"中国","rcvPr":"广东省","rcvCity":"广州市","settMod":"线上支付","mkrCom":"制单公司","rcvPrtDepBnkNm":rcvPrtDepBnkNm,"rcvPrtDepBnkNo":"","rcvPrtBnkCD":rcvPrtBnkCD,"rcvPrtBnkCgyCd":"01","rcvPrtCustAccNo":rcvPrtCustAccNo,"rcvPtAcNm":rcvPtAcNm,"rcvPtAcCgyCd":"01","rcvPrtAdr":"收款方地址","urgntTpCd":"01","useNm":"用途名称","rmrk":"用途","cstMblPhNo":"13044444444","sMSCntnt":"短信内容","emailAdr":"123@qq.com","mailCntDsc":"邮件内容描述","rstNoticeUrl":"付款结果通知地址","ccyCd":"CNY"}}
        },
        ]

if __name__ == "__main__":
    print(Transfer_100_Data.cases[1]["case"])
