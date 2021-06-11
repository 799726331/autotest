'''
@File    :   data_000_custInfoQuery.py
@Time    :   2021/1/11 22:07 
@Author  :   卢梓轩 
@Version :   Python 3.7.6
@State   :   
'''

import random
import time

certNo = "110101199003076704"

class goodlife_custInfoQuery_23_data():
    cases = [
        {
            "title": "000-客户查询成功，查询成功",
            "expection": "S",
            "case": {"channel":"00000009","data":{"commonInput":{"version":"1.0.0","channel":"00000009","reqDate":"20210107","reqTime":"181317","remark":""},"certNo":certNo}}
        },
        {
            "title": "001-客户查询缺certNo，查询失败",
            "expection": "S",
            "case": {"channel": "00000009", "data": {"commonInput": {"version": "1.0.0", "channel": "00000009", "reqDate": "20210107", "reqTime": "181317","remark": ""}, "certNo": ""}}
        }
    ]

if __name__ == '__main__':
    print(goodlife_custInfoQuery_135_data().cases[0]["case"])