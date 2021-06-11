'''
@File    :   db.py
@Time    :   2021/3/14 14:45 
@Author  :   卢梓轩 
@Version :   Python 3.7.6
@State   :  数据库连接查询
'''

import pymysql
from scripts1.utils.log import GetLog
from scripts1.utils.config import Get_Db

log = GetLog().goodlife_Log()


def db_select_001(host,dct_Id):
    # 建立数据库连接
    db = pymysql.Connect(
        host = Get_Db().host_dir,
        port = Get_Db().port_dir,
        user = Get_Db().user_dir,
        passwd = Get_Db().passwd_dir,
        db='',
        charset=''
    )
    # 从数据库中查询
    sql="SELECT dct_state FROM {}_ylm_ecome.ec_dct WHERE dct_id = '{}'".format(host , dct_Id)
    # 获取游标
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        # 执行sql语句并存在于游标
        results=cursor.fetchone()
        # 获取一条记录
        sql_res = str(results[0])
        log.logger.info("融资单dct_state状态为：{}".format(sql_res))
        return (sql_res)
    except:
        print('Error:unable to fetch data')
    db.close()
    # 关闭数据库连接

def db_select_002(host,dct_Id):
    # 建立数据库连接
    db = pymysql.Connect(
        host='10.254.254.30',
        port=3306,
        user='demo',
        passwd='demo123',
        db='',
        charset=''
    )
    # 从数据库中查询
    sql="SELECT pmt_state FROM '{values1}'_ylm_ecome.ec_dct_fee_dtl WHERE dct_id = '{values2}' AND fee_type = 'tPSFee'".format(values1 = host,values2 = dct_Id)
    # 获取游标
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        # 执行sql语句并存在于游标
        results=cursor.fetchone()
        # 获取一条记录
        sql_res = str(results[0])
        log.logger.info("融资单tPSFee的pmt_state状态为：{}".format(sql_res))
        return (sql_res)
    except:
        print('Error:unable to fetch data')
    db.close()
    # 关闭数据库连接

def db_select_003(host,dct_Id):
    # 建立数据库连接
    db = pymysql.Connect(
        host='10.254.254.30',
        port=3306,
        user='demo',
        passwd='demo123',
        db='',
        charset=''
    )
    # 从数据库中查询
    sql="SELECT pmt_state FROM '{values1}'_ylm_ecome.ec_dct_fee_dtl WHERE dct_id = '{values2}' AND fee_type = 'bankFee'".format(values1 = host,values2 = dct_Id)
    # 获取游标
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        # 执行sql语句并存在于游标
        results=cursor.fetchone()
        # 获取一条记录
        sql_res = str(results[0])
        log.logger.info("融资单bankFee的pmt_state状态为：{}".format(sql_res))
        return (sql_res)
    except:
        print('Error:unable to fetch data')
    db.close()
    # 关闭数据库连接


def db_select_004(host,dct_Id):
    # 建立数据库连接
    db = pymysql.Connect(
        host='10.254.254.30',
        port=3306,
        user='demo',
        passwd='demo123',
        db='',
        charset=''
    )
    # 从数据库中查询
    sql="SELECT pmt_state FROM '{values1}'_ylm_ecome.ec_dct_fee_dtl WHERE dct_id = '{values2}' AND fee_type = 'bankIns'".format(values1 = host,values2 = dct_Id)
    # 获取游标
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        # 执行sql语句并存在于游标
        results=cursor.fetchone()
        # 获取一条记录
        sql_res = str(results[0])
        log.logger.info("融资单bankIns的pmt_state状态为：{}".format(sql_res))
        return (sql_res)
    except:
        print('Error:unable to fetch data')
    db.close()
    关闭数据库连接


if __name__ == '__main__':
    a = db_select_001('sit','311de6d87b5c4cc8ad52f8eeb75a19da')
    print(a)





#获取游标
# 游标：游标的设计是一种数据缓冲区的思想，用来存放sql语句执行结果。
# 游标是在先从数据表中检索除数据之后才能继续灵活操作的技术。类似于指针，指向数据结构堆栈中的指针，用来pop出所指向的数据，并且只能每次取一个。
# cursor=db.cursor()
# print(conn)
# print(cursor)
# 1、从数据库中查询
# sql="INSERT INTO login(user_name,pass_word)"
# sql="SELECT dct_state FROM dev2_ylm_ecome.ec_dct WHERE dct_id ='48e4767163e34e4ebabc1524c8d6e80b'"
# cursor执行sql语句
# cursor.execute(sql)
# 打印执行结果的条数
# print(cursor._query(sql))
# print(a)
# print(cursor.fetchall()[0][0])
# for row in cursor.fetchall():
#         print(row)

