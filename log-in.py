import mysql.connector
from termcolor import colored

database = mysql.connector.connect(
    host='localhost', port='3306', user='root', password='', database='log_in')

cursor = database.cursor()


def create_user():
    name = input(colored(f"Username: ", 'red'))
    password = input(colored(f"Password: ", 'red'))
    print('---------------------------')

    cursor.execute(
        "INSERT INTO user_account (user_name, u_password) VALUES (%s, %s)", (name, password))
    database.commit()


def road_to_pass():
    sql_code_pass = "SELECT * FROM user_account"
    cursor.execute(sql_code_pass)
    password_d = cursor.fetchall()
    answer = 1
    for a in range(3):
        for x in password_d:
            password = input(colored(f"Password: ", 'red'))
            if password != x[2]:
                print(colored(f"password not correct", 'red'))
                print(colored(f"-------------------", 'red'))
            else:
                print(colored(f"Username correct", 'green'))
                print(colored(f"Password correct", 'green'))
                answer = 0
        if answer == 0:
            break


def log_in():
    sql_code = "SELECT * FROM user_account"
    cursor.execute(sql_code)
    name_data = cursor.fetchall()
    result = 1
    for z in range(3):
        for i in name_data:
            name = input(colored(f"Username: ", 'red'))
            if name != i[1]:
                print(colored(f"Username not correct", 'red'))
                print(colored(f"-------------------", 'red'))
            else:
                result = 0
                break
        if result == 0:
            road_to_pass()
            break


for i in range(1):
    print('--------------------------')
    print(colored(f"type 0 to create account", 'blue'))
    print(colored(f"type 1 to log-in to your account", 'blue'))

while True:
    try:
        confirm = int(input(colored(f":", "red")))
        if confirm == 0 or confirm == 1:
            break
        print(colored(f"<------input should be 0 or 1----->", 'red'))
    except Exception as e:
        print(colored(f"{e}", 'red'))

if confirm == 0:
    print(colored(f"creating user ...", 'blue'))
    create_user()
else:
    print(colored(f"log-in ...", 'blue'))
    log_in()

cursor.close()
database.close()
