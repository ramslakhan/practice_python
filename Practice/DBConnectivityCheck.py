import mysql.connector

def get_dbconnection():

    my_sql=mysql.connector.connect(host='localhost',user='root',password='laxman',database='python_training')
    #print(mysql)
    my_cursor=my_sql.cursor()
    my_cursor.execute("select * from user_details")
    result=my_cursor.fetchall()
    #result=my_cursor.fetchone()
    for i in result:
        return i



