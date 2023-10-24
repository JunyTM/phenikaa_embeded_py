import requests
import variableAndContrants as env
import pymysql.cursors  

# Sử dụng ngrok để public server
# base = "http://192.168.1.21:12002"
# url = base + "/api/traffic"

# def call():
#     data = requests.get(url).json()['data']
    
#     env.TIME_GREEN[0]  = data['time_green']
#     env.TIME_YELLOW[0] = data['time_yellow']
#     env.TIME_RED[0]    = data['time_red']
#     env.TIME_EMER[0]   = data['time_emergency']

#     env.IS_Emer[0] = data['is_emergency']
#     env.IS_Night[0] = data['is_night']
#     env.INFO_SHOW[0] = data['info_show']
#     # print(data)



connection = pymysql.connect(host='192.168.5.129',
                                user='root',
                                password='1234',                             
                                db='simplehr',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
print ("connect successful!!")

def getData():
    with connection.cursor() as cursor: 
        # SQL 
        sql = "SELECT * FROM traffics where id = 1" 
        # Thực thi câu lệnh truy vấn (Execute Query).
        cursor.execute(sql) 
        print ("cursor.description: ", cursor.description) 
        print() 
        for row in cursor:
            print(row)
            env.TIME_GREEN[0]  = row['time_green']
            env.TIME_YELLOW[0] = row['time_yellow']
            env.TIME_RED[0]    = row['time_red']
            env.TIME_EMER[0]   = row['time_emergency']
            env.IS_Emer[0]     = row['is_emergency']
            env.IS_Night[0]    = row['is_night']
            env.INFO_SHOW[0]   = row['info_show']

def updateData():
    cursor = connection.cursor() 
    sql = "Update traffics set Salary = %s, Hire_Date = %s where Emp_Id = %s"   
    # Thực thi sql và truyền 3 tham số.
    rowCount = cursor.execute(sql, (850, newHireDate, 7369 ) ) 
    connection.commit()  
    print ("Updated! ", rowCount, " rows") 
