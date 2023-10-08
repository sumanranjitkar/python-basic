#Task
#is_Login variable which is global variable
#function login with 2 parameter
#username and password
#is login variable true or false
#if both matches print true else false

is_Login=False
def login(user_name, password):
    global is_Login
    # user_name=="suman"
    # password=="1234"

    if user_name=="suman" and  password =="1234":
        is_Login=True
    else:
        is_login = False
        

login("suman","1234")

if is_Login:

    print("username and password match")
else:
    print("invalid user_name and password")
