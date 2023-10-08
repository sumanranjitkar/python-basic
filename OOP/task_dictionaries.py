#user name input magera register garnu paryo 
#ani user login garera logged successfully vanera aaunu paryo
#login gareko macnhe le matra user haru ko list herna paunu paryo


user={}

def registered_user():
    username = input("Enter username for register: ")
    password = input("enter a password: ")
    user[username]=password
    print("Registeration sucessfully !!!")

def login_user():
    username = input("Enter usernme for Login: ")
    password = input("enter a password: ")

    if user.get(username)== password:
        print("Sucessfully login")
    else:
        print("Invalid username or password!")

def display_user():
     print("registered Users: ", user)
    #  print(user.pop(username))



while True:
    Choice = input("""\n enter your choice: 
                   1. User Registration
                   2. User Login 
                   3. Display Users
                   4. Exit\n """  )
    if Choice == '1':
        registered_user()
    elif Choice == '2':
        login_user()
    elif Choice == '3':
        display_user()
    elif Choice == '4':
        break
    else:
        print("invalid choice please choice again: ")
