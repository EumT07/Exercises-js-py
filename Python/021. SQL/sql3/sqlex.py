import sqlite3
from employ import Employee

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

"""Employee Table"""

# cursor.execute("""CREATE TABLE employees (
#         firstName text,
#         lastName text,
#         payment INTEGER
#         )""")

# 1
# cursor.execute("INSERT INTO employees VALUES ('Eublan','Mata',45000)")
# 2
# cursor.execute("INSERT INTO employees VALUES ('Alberto','Mata',5000)")


"""With Employee Class"""

emp_1 = Employee('Andrea','Jimenez',25500)
emp_2 = Employee('Maria','Jimenez',45500)


"""Insert with Class and questions mark"""

# #1 ?

# cursor.execute("INSERT INTO employees VALUES (?,?,?)",(emp_1.firstName,emp_1.lastName,emp_1.payment))

# connection.commit()

# #2 

# cursor.execute("INSERT INTO employees VALUES (:firstName, :lastName,:payment)",{
#     'firstName':emp_2.firstName, 
#     'lastName':emp_2.lastName,
#     'payment':emp_2.payment})

# connection.commit()


"""Different way that you can use in order to get values"""

#1 Classic
# cursor.execute("SELECT * FROM employees WHERE lastName='Mata'")

# emp_all = cursor.fetchall()
# print(emp_all)

#2 Question mark send it with a tupla
cursor.execute("SELECT * FROM employees WHERE lastName=?", ('Mata',))

mataBrothers = cursor.fetchall()
print(mataBrothers)

#3 Variables
cursor.execute("SELECT * FROM employees WHERE lastName=:lastName", {'lastName':'Jimenez'})

jimenezSisters = cursor.fetchall()
print(jimenezSisters)

connection.commit()
connection.close()