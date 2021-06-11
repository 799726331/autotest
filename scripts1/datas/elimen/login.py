# -*- encoding: utf-8 -*-
'''
@File    :   login.py
@Time    :   2020/09/04 15:02:19
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   登录测试用例 
'''

# here put the import lib
class Cases():
    case = [
        {
            "no": "000",
            "title": "正常登录",
            "payload":{"username":"jiulong","password":"QXMlMzqHu4BJL0CruuvgJmkKmFIQeiE+ExEOth8Xvo8Qg4gYG0OFlxgaH4vT0+fb5TBqPvNzRr00t10rFMDhJVfvxRaGMchFRltVSA/bL9jO1vKE/Dg2Am+9kqmQa+QKdYTIKGlnynUMXZrVf/NInNPfmNXOzT8wu+jfB0PZl8o=","rememberMe":"TRUE","kaptchaReceived":"!@#$","client":"frontend","grant_type":"password","appCode":"GOVERNOR","qrcodeLogin":"FALSE","loginUUid":"","uuid":"","certNo":"","loginMethod":"pwd","loginEnd":"portal"},
            "expect":"登录成功！"
        },
        {
            "no": "001",
            "title": "验证码为空",
            "payload":{"username":"jiulong","password":"QXMlMzqHu4BJL0CruuvgJmkKmFIQeiE+ExEOth8Xvo8Qg4gYG0OFlxgaH4vT0+fb5TBqPvNzRr00t10rFMDhJVfvxRaGMchFRltVSA/bL9jO1vKE/Dg2Am+9kqmQa+QKdYTIKGlnynUMXZrVf/NInNPfmNXOzT8wu+jfB0PZl8o=","rememberMe":"TRUE","kaptchaReceived":"","client":"frontend","grant_type":"password","appCode":"GOVERNOR","qrcodeLogin":"FALSE","loginUUid":"","uuid":"","certNo":"","loginMethod":"pwd","loginEnd":"portal"},
            "expect":"验证码不能为空！"
        },
        {
            "no": "002",
            "title": "用户名为空",
            "payload":{"username":"","password":"QXMlMzqHu4BJL0CruuvgJmkKmFIQeiE+ExEOth8Xvo8Qg4gYG0OFlxgaH4vT0+fb5TBqPvNzRr00t10rFMDhJVfvxRaGMchFRltVSA/bL9jO1vKE/Dg2Am+9kqmQa+QKdYTIKGlnynUMXZrVf/NInNPfmNXOzT8wu+jfB0PZl8o=","rememberMe":"TRUE","kaptchaReceived":"!@#$","client":"frontend","grant_type":"password","appCode":"GOVERNOR","qrcodeLogin":"FALSE","loginUUid":"","uuid":"","certNo":"","loginMethod":"pwd","loginEnd":"portal"},
            "expect":"请输入手机号/登录名！"
        },
        {
            "no": "003",
            "title": "密码为空",
            "payload":{"username":"jiulong","password":"","rememberMe":"TRUE","kaptchaReceived":"!@#$","client":"frontend","grant_type":"password","appCode":"GOVERNOR","qrcodeLogin":"FALSE","loginUUid":"","uuid":"","certNo":"","loginMethod":"pwd","loginEnd":"portal"},
            "expect":"请输入密码！"
        },
        {
            "no": "004",
            "title": "密码错误",
            "payload":{"username":"jiulong","password":"RhXtBGUnTpG/idCrN1eSm0UxnGdeBA50Q0LtBZyWM4paKdA3NS7WFCRzIez1FK6gwCYvTSJ4CiFExrxwnCzTMZDnbDy1+rvqv7Tvpsr+sYNkklzI7+LbHlYti88QVBC72Z8z9svy2Bc1ns/sAKU83UIt7e60T6JKeONkNHCWkQY=","rememberMe":"TRUE","kaptchaReceived":"!@#$","client":"frontend","grant_type":"password","appCode":"GOVERNOR","qrcodeLogin":"FALSE","loginUUid":"","uuid":"","certNo":"","loginMethod":"pwd","loginEnd":"portal"},
            "expect":"手机号码/登录名或密码错误"
        }
    ]
