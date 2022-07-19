"""
learn by python
"""
#learn

# myName = "aLi issa"
# str = {
#     "ahmad" :12,
#     "mmm": input("Enter your first name:" ) 
# }
# name = input("Enter your last name: ")
# num1= input("Enter Number1: ")
# num2= input("Enter number2: ")
# print( "hello " + str["mmm"] + " "+ name)
# result = float(num1) + float(num2)
# print(result)

# cars=['bmw', 'marcedes', 'ALFAROMEO', 'Ferrari']

# print(len(cars))
# for x in cars :
#     print(x)

# def myfunction(name, pos):
#     # num1= input("Enter Number1: ")
#     # num2= input("Enter number2: ")
#     # result = float(num1) + float(num2)
#     # print(result)
#     # print('hello', name)
#     # print("I like to " + cars[2])
#     # cars.extend([12,14,14])
#     # cars.append("kia")
    
#     # cars.insert(2, "ahmad")
#     # cars.remove('bmw')
#     # cars.pop()

#     # print(cars)
#     # cars.reverse()
    
#     # print(cars)
#     print("hello " + name + "\nyour are : " + pos)

    
# myfunction(input("Enter your name: "), input("Enter position: "))
# def cube(num):
#     return num*num*num
    
# print(cube(6))
# def max(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(max(7,50,50))

num1= float(input("Enter First num :"))
op = input("Enter operation :")
num2 = float(input("Enter Second Num: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 + num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print( num1 * num2)
else :
    print("Please Enter Valid Operation")
