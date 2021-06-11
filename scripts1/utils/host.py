# -*- encoding: utf-8 -*-
'''
@File    :   host.py
@Time    :   2020/09/14 15:54:05
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   None 
'''

# here put the import lib

HOST = {
    "99":"http://10.132.4.99:9050",
    "135":"http://sit2.elimen.com.cn:5515",
    "100":"http://uat.elimen.com.cn:8899",
    "134":"http://10.132.4.134:9050",
    "23":"http://sit.elimen.com.cn:8899",
    "dev2":"http://dev2.elimen.com.cn:8899",
    "pre":"http://pre.elimen.com.cn:58038",
    "135_pay_host":"http://sit2.elimen.com.cn:5515/openGateway",
    "100_pay_host":"http://openapi.uat.elimen.com.cn:5515/openGateway",
    "pre_pay_host":"http://ysc.elimen.com.cn:58038/openGateway",
    "SIT":"https://sit.elimen.com.cn"
}

dbHOST = {
    "23":"10.254.254"
}

if __name__ == '__main__':
    print(HOST["100"])
    # print(type(HOST["99"]))


