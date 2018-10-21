import pymysql

# 打开数据库连接

# localhost 为 本地连接
# root 为用户名
# password 为密码
# test_data 为数据库
db = pymysql.connect("localhost", "root", "root", "mysql")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()
