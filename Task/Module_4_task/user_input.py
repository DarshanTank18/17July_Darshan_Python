import pymysql

try:
    dbcon = pymysql.connect(host='localhost', user='root', password='', database='studinfo')
    print("Database Connected!")
except Exception as e:
    print(e)

cr = dbcon.cursor()

# Table Create
tbl_create = "CREATE TABLE IF NOT EXISTS studinfo(id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), city VARCHAR(20))"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

# Insert data
name = input("Enter Name: ")
city = input("Enter City: ")
insert_data = "INSERT INTO studinfo (name, city) VALUES (%s, %s)"

try:
    cr.execute(insert_data, (name, city))
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)

# # Update data
# u_id = int(input("Enter id: "))
# u_name = input("Enter updated name: ")
# u_city = input("Enter updated city: ")

# update_data = "UPDATE studinfo SET name = %s, city = %s WHERE id = %s"

# try:
#     cr.execute(update_data, (u_name, u_city, u_id))
#     dbcon.commit()
#     print("Record updated!")
# except Exception as e:
#     print(e)