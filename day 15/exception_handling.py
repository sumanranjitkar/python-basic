# while True:
#  try:
#   a=int (input("enter the number: "))
#   b=int (input("enter the number: "))
#   print(a/b)
#  except:
#   print("something went wrong") 


while True:
 try:
  a=int (input("enter the number: "))
  b=int (input("enter the number: "))
  print(a/b)
 except ZeroDivisionError: #zero le division garna nadina ko lagi except zerodivison error rakhne
  print("Anumber can't be divisible by zero") 
 except ValueError: #interger or float ko thau ma string input halna khojda yo value halne
  print("invalid value , insert only integer value")
 except:
  print("something went wrong")



