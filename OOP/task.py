# create a list named user_list
#collection of Dictionary multiple user
#user name, password
#user input username password
#if the username and password exist or not
#username and password valid print you have been login
#sucessfully else invalid creditials



# user_list = [{"user_name": "a", "password": "1"},
#              {"user_name": "b", "password": "2"},
#              {"user_name": "c", "password": "3"},
#              {"user_name": "d", "password": "4"},]

# username = input("Enter username: ")
# password = input("Enter password: ")

# for user in user_list:
#     if user["user_name"] == username and user["password"] == password:
#         print("You have been logged in successfully!")
#         break
# else:
#     print("Invalid credentials.")







is_Login=False

def login():
    global is_Login
    
    username=input("enter the username: ")
    password=input("enter the password: ")
    

    user_list = [{"user_name":"a" ,"password":"1"}, 
             {"user_name":"b" ,"password":"2"}, 
             {"user_name":"c" ,"password":"3"}, 
             {"user_name":"d" ,"password":"4"}]

    
    for user in user_list:
     if user["user_name"] == username and user["password"] == password:
        is_Login= True
        break
    else:
       is_Login = False


login()
if is_Login:
        print("username and password match")
else:
    print("invalid user_name and password")
