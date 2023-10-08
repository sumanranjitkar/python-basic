# def hash(func):
#     def wrapper():
#         print('#'*10)
#         func()
#         print('#'*10)
#     return wrapper



# @hash
# def hello():
#     print('Hello')

# @hash
# def world():
#     print('world')

# hello()
# #hash(hello)()
# world()

#task
#*********
#%%%%%%%%
##########

def star(func):
    def wrapper():
        print('*'*10)
        func()
        print('*'*10)
    return wrapper

def percent(func1):
    def wrapper():
        print('%'*10)
        func1()
        print('%'*10)
    return wrapper

def hash(func2):
    def wrapper():
        print('#'*10)
        func2()
        print('#'*10)
    return wrapper


@star
@percent
@hash
def hello():
    print('Hello')

# @hash
# def world():
#     print('world')

# hello()
# #hash(hello)()
hello()


#decorator nahalikana # #hash(hello)() rakhera homework