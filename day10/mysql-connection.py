#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql as mdb

# CREATE DATABASE IF NOT EXISTS python_test DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

# 打开数据库连接
db = mdb.connect("localhost", "root", "P@ssw0rd", "python_test", charset='utf8' )

# # 连接测试
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()

# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")

# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
# print ('mysql版本为 : %s ' % data);

# # 关闭数据库连接
# db.close()



# # 使用cursor()方法获取操作游标
# cursor = db.cursor()

# # 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# # 创建数据表SQL语句
# sql = 'CREATE TABLE EMPLOYEE (FIRST_NAME  CHAR(20) NOT NULL, LAST_NAME  CHAR(20), AGE INT,  SEX CHAR(1), INCOME FLOAT )';

# # SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

# cursor.execute(sql)

# # 关闭数据库连接
# db.close()




# 使用cursor()方法获取操作游标
# cursor = db.cursor()

# ## SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()

# # 关闭数据库连接
# db.close()




# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE WHERE INCOME = 2000";
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   print(results);
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果
      print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % fname, lname, age, sex, income);
except:
   print ("Error: unable to fecth data");

# 关闭数据库连接
db.close()