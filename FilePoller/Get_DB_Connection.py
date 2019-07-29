# import mysql.connector
#
# def get_dbconnection():
#
#     my_sql=mysql.connector.connect(host='localhost',user='root',password='laxman',database='python_training')
#     my_cursor=my_sql.cursor()
#     #query = "select * from user_details;"
#     query = "insert into user_details(id,name,location) values('5','cheekati','Hyd');"
#
#     print(query)
#     print(my_cursor.execute(query))
#     my_sql.commit()
#     my_sql.close()
#     # result=my_cursor.fetchall()
#     # #result=my_cursor.fetchone()
#     # for i in result:
#     #     print(i)
#
# get_dbconnection()
#
