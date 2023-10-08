# a=10

# def number():
#     #global a  #global a le global a ko value lai local value sanga override garidincha
#     a=11
#     print(a)

# number()
# print(a)


x=10
def outer():
    x=11
    def inner():
        x=12
        return x
    print(x)
    print(inner())
print(x)
outer()
