#print(list(range(10)))

# for i in range(2, 10,2 ): # last of 2 is result will be increment by 2 
#     print(i)

#kwargs
def person(**person):
    print(f"""hello!!Your name is {person['name']},
           your age is {person['age']},
           gender is {person['gender']}""")

person(name='ram', age=20, gender= 'male')