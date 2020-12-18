from api_lesson.utilities.configuration import *

# connection format is host, database, user, password
# conn = mysql.connector.connect(host='localhost', database='PythonAutomation',
#                                user='root', password='InputLocalRootPass')  # Connection str format
conn = getDBConnection()  # Connection method for clean implementation of conn str

# Check if connection is established, should return True
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * From CustomerInfo')
# row = cursor.fetchone()  # selects the first row and moves cursor to next row
'''
Every time fetchone() is executed the current selected row is fetched,
if it's executed for the first time then the first row is executed
trace the number of times where fetchone() is executed to know the
location of the cursor in the table
'''
# print(row)
# print(row[3])
# row_all = cursor.fetchall()  # fetches all list of tuples from the point of the cursor
# print(row_all)

rows = cursor.fetchall()
print(type(rows))
print(rows)
total_amnt = 0
for row in rows:
    total_amnt = total_amnt + row[2]
print(total_amnt)

# Execute an update query from python code/automation side
tables = ("customerInfo", "Books", "Storage3")
query = "update customerInfo set Location = %s where CourseName = %s"
data = ('Asia', 'Jmeter')
cursor.execute(query, data)
conn.commit()

# Delete a data/row from python/automation code side
del_query = "delete from customerInfo where courseName = 'Appium'"
cursor.execute(del_query)
conn.commit()

conn.close()
