#user name input magera register garnu paryo 
#ani user login garera logged successfully vanera aaunu paryo
#login gareko macnhe le matra user haru ko list herna paunu paryo


# my_dict = {}


# keyword = input("Enter a keyword: ")
# value = input("Enter a value: ")


# my_dict[keyword] = value


# print("Dictionary:", my_dict)






user ={}



def registered_user():
    username=input("enter a username to registered: ")
    password=input("enter a password: ")
    user[username]=password
    print("registration sucessful")

def login_user():
    username = input("please type registered username: ")
    password = input("enter your password: ")

    if user.get(username) == password:
      print("login sucessful ")
    else:
      print("login failed , please type valid username and password:")

while True:
    print("\n 1. Register \n 2. Login \n 3. Exit")
    choice = input("enter your choice: ")
    if choice == '1':
        registered_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
        break
    else:
        print(" invalid choice please input valid choices: ")