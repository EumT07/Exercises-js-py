from multiprocessing import connection
import sqlite3
from employ import Employee



connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

"""
Employee Table
"""
cursor.execute("""CREATE TABLE employees (
                firstName VARCHAR(50),
                lastName VARCHAR(50),
                payment INTERGER
            )""")

#Functions

def insert_emp(employee):
    with connection:
        cursor.execute("""
            INSERT INTO employees VALUES (
            :firstName, :lastName, :payment)""",{
                'firstName':employee.firstName,
                'lastName':employee.lastName,
                'payment':employee.payment 
            })

def get_employees_by_name(lastName = None):
    cursor.execute("SELECT * FROM employees WHERE lastName=:lastName",{'lastName':lastName})
    return cursor.fetchall()

def update_payment(employee, newPayment):
    with connection:
        cursor.execute("""UPDATE employees SET payment = :payment
                        WHERE firstName = :firstName AND lastName = :lastName""",{
                            'firstName':employee.firstName,
                            'lastName':employee.lastName,
                            'payment': newPayment
                        })
                        
def delete_employeed(employee):
    with connection:
        cursor.execute("DELETE FROM employees WHERE firstName = :firstName AND lastName = :lastName", {'firstName':employee.firstName, 'lastName':employee.lastName})

emp_1 = Employee("Eublan","Mata",50000)
emp_2 = Employee("Alberto","Mata",70000)
emp_3 = Employee("Miguel","Luz",70000)

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)


# emps = get_employees_by_name("Mata")
# print(emps)

update_payment(emp_1, 120000)
delete_employeed(emp_2)

emp_Luz = get_employees_by_name("Luz")
print(emp_Luz)
emps = get_employees_by_name("Mata")
print(emps)


connection.commit()
connection.close()