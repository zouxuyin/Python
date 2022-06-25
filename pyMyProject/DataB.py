import mysql.connector as ms  # 导入链接mysql数据模块
import pandas as pd
import pymysql

pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine  # 写数据库


def Db_R(sql):
    db = pymysql.connect(host='localhost',
                         user='root',
                         passwd='123456',
                         db='test',
                         charset='utf8')
    cursor = db.cursor()
    #   sql = "select * from df"
    df_sql = pd.read_sql(sql, db)
    cursor.close()
    db.close()
    return df_sql


def Db_T(df, b):
    conn = create_engine('mysql://root:123456@localhost:3306/test?charset=utf8')
    df.to_sql(name='user', con=conn, if_exists='append', index=False, index_label=False)

# if __name__ == '__main__':
#
#     sql = "select * from user"
#     ls = Db_R(sql)

