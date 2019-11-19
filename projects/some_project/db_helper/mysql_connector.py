import pymysql.cursors  
 
# Подключиться к базе данных.
connection = pymysql.connect(host='db4free.net',
                             port=3306,
                             user='alex_may',
                             password='4jKQZDa9QExQziW',                             
                             db='shop_may',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")
 
try:
  
 
    with connection.cursor() as cursor:
       
        # SQL 
        sql = "SELECT Dept_No, Dept_Name FROM Department "
         
        # Выполнить команду запроса (Execute Query).
        cursor.execute(sql)
         
        print ("cursor.description: ", cursor.description)
 
        print()
 
        for row in cursor:
            print(row)
             
finally:
    # Закрыть соединение (Close connection).      
    connection.close()