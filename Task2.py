import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="Login_system")
cur = con.cursor()

def user_registration():
    import re
    Name = input("Enter the username: ")
    Password = input("enter the password: ")
    def check(email):

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, email)):
            print("Username is valid!!")
        else:
            print("Invalid USername!!Enter valid email with ""@"", "".""")

    if __name__ == '__main__':
        check(Name)
    cur.execute("""SELECT username FROM Login_system where username =\"""" + Name + """\";""")
    result = cur.fetchone()
    if result != None:
        print("Enter username:")
    else:
        password = Password
        flag = 0
        while True:
            if (len(password) >= 16) and (len(password)<=5):
                flag = -1
                break
            elif not re.search("[a-z]", password) and re.search("[A-Z]", password):
                flag = -1
                break
            elif not re.search("[0-9]", password) and re.search("[_@$]", password):
                flag = -1
                break
            elif re.search("\s", password):
                flag = -1
                break
            else:
                flag = 0
                cur.execute("""INSERT INTO Login_system (username, password) VALUES (\"""" + Name + """\",\"""" + Password + """\")""")
                con.commit()
                break

        if flag == -1:
            print("Password INVALID!!!")
            print("Enter valid password with at least one lower case letter, upper case letter, digit and a special character")
    

def user_login():
    user_name = input("Enter username: ")
    def check_name(name):
        import re
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, name)):
            print("Username successful")
        else:
            print("Username Invalid!!!")
            quit()
    if __name__ == '__main__':
        check_name(user_name)

    cur.execute("""SELECT username FROM Login_system where username =\"""" + user_name + """\";""")
    result = cur.fetchone()
    if result == None:
        print("Enter  a valid email id!!")
    else:
        for i in result:
            name = i
            break


    pwd = input("Enter your password: ")
    import re
    password = pwd
    flag = 0
    while True:
        if (len(password) >= 16) and (len(password)<=5):
            flag = -1
            break
        elif not re.search("[a-z]", password) and re.search("[A-Z]", password):
            flag = -1
            break      
        elif not re.search("[0-9]", password) and re.search("[_@$]", password):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            print("Password created successfully!!")
            break

    if flag == -1:
        print("Password INVALID!!!")
        print("Enter valid password with at least one lower case letter, upper case letter, digit and a special character")
       

    cur.execute("""SELECT password FROM Login_system where password =\"""" + pwd + """\";""")

    result = cur.fetchone()
    if result == None:
        print("Enter correct password")
        print("Menu: 1. Register 2.Forgot Password 3.Login 4.Exit")
        x = int(input("Enter your choice:"))
        if x == 1:
            user_registration()
        elif x == 2:
            username1 = input("Enter username for getting password: ")
            cur.execute("""SELECT password from Login_system where username =\"""" + username1 + """\";""")
            result = cur.fetchone()
            for i in result:
                print("Your password is:", i)
        elif x == 3:
            user_login()
        elif x == 4:
            return

    elif result != None:
        for i in result:
            password = i
        print("Login has been successful!!")

    else:
        return


while(True):
    print("Menu")
    print("1. Register Here")
    print("2. Login")
    print("3. Exit")
    n = int(input("Enter the value: "))
    if n == 1:
        user_registration()
    elif n == 2:
        user_login()
    elif n==3:
        print("####EXIT####")
    else:
        break