# def hello_world():
#     print("hello world")

# hello_world()
# hello_world()
# hello_world()

#argument and variable
# def hello_world(name):
#     print(f"hello !! {name} how are you?")

# hello_world('ram')
# hello_world('shyam')

#create a function name person 
#attribute name , age, gender, location

# def hello_world(name, age , gender,location, hobby):
#     print(f"""hello !! my name is  {name} ,
#            my age is {age} , my gender is {gender}, 
#             my address is {location} , my hobby is {hobby} """)

# hello_world("suman", 30 ,"male","basantapur","reading books")



# def hello_world(name, hobbies):
#     print(f'{name}')
#     for hobby in hobbies:
#         print(hobby)

# hello_world('ram', ['coding', 'cycling','hiking'])


#args and kwargs

# def numbers(*numbers):
#     print(numbers)
# numbers(1,2,3,4,5,6,7)

#iteration
# def person(*names):
#     for name in names:
#        print(name)
# person('ram','shyam','sdsd','snfdj')

#kwargs
def person(**person):
    print(f"""hello!!{person['name']},
          your age is {person['age']},
          gender is {person['gender']}""")

person(name='ram', age=20, gender= 'male')


   