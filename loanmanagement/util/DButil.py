import mysql.connector as sql

class getconnection:
    def dbconnection(self):
        try:
            conn = sql.connect(host='localhost', database='sample', user='loan_manag', password='karthikeyan@26')
            if conn.is_connected:
                print("Database is connected:")
        except Exception as e:
            print("Error : ",e)



stmt=conn.cursor()
create_str='''
create table customer
(
customer_id int primary key,
name varchar(50),
email varchar(50),
phone_num varchar(50),
address varchar(50),
credit_score int
)
'''

stmt.execute(create_str)

stmt=conn.cursor()
create_str='''
create table loan
(
loan_id int primary key,
principle_amount int,
interest_rate int,
loan_term varchar(25),
loan_type varchar(25),
loan_status varchar(25)
)
'''

stmt.execute(create_str)

def insert():
    customer_id = int(input("Enter roll no "))
    name = input("Enter name")
    email = input("Enter your email")
    phone_num = input("enter your phone_number ")
    address = input("Enter your address ")
    credit_score = input("Enter your credit_score ")

    create_insert = '''insert into student(customer_id,name,email,phone_num,address,credit_score) values( %s, %s, %s, %s,%s,%s)'''
    data = [(customer_id,name,email,phone_num,address,credit_score)]
    stmt = conn.cursor()
    stmt.executemany(create_insert, data)
    conn.commit()
    print('Inserted Successfully: ')


def delete():
    customer_id = int(input("Enter the customer_id for deletion"))
    delete_str = f'delete from customer where customer_id={customer_id}'
    stmt = conn.cursor()
    stmt.execute(delete_str)
    conn.commit()
    print("Deleted Successfully ")

def update():
    customer_id = int(input("Enter customer_id "))
    name = input("Enter name")
    email = input("Enter your email")
    phone_num = input("enter your phone_number ")
    update_str = 'update customer set name=%s,email=%s,phone_num=%s where customer_id=%s'
    data = [(name, email, phone_num)]
    stmt = conn.cursor()
    stmt.executemany(update_str, data)
    conn.commit()
    print("updated successfully")


def select():
    select_str='select * from customer'
    stmt=conn.cursor()
    stmt.execute(select_str)
    data=stmt.fetchall()
    for i in data:
        print(i)
