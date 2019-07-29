import FilePoller.Get_DB_Connection
import mysql.connector


def execute_query(query_statement):
     my_sql=mysql.connector.connect(host='localhost',user='root',password='laxman',database='python_training')
     my_cursor=my_sql.cursor()
     my_cursor.execute(query_statement)
     my_sql.commit()
     # print(status)
     # if status:
     #      print('Record has been updated successfully')
     # else:
     #      print('Sorry your record', {}, 'update is failed'.format(query_statement))
     my_sql.close()


def on_modified(event):
     print(event.src_path,'has been modified')
     open_file = open(event.src_path ,'r')
     query_statement = open_file.readline()
     #print(query_statement)
     execute_query(query_statement)


def on_created(event):
     print(event.src_path ,'has been created')
     #print(type(event.src_path))
     open_file = open(event.src_path ,'r')
     print(open_file.read())