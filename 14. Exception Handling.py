# import builtins
# help(builtins)

#SyntexError
# def hello():
#     print('Hello ABCC')


#NameError
# ABCC = 'Anybody Can Code'
#
# print(ABCC)

#ZeroDivisionError
# print(5+5)
# print(20/0)

#TypeError
# var = 'a'
# print(5+var)


#IndexError
# list = [1,2,3,4,5,6]
# print(list[10])

#KeyError
# dict = {1:"1",2:2,3:3,4:4,5:5}
# print(dict[6])

#FileNotFoundError
# open('id.txt')
# try:
#     open('id.txt')
# except FileNotFoundError as e:
#     print('File not Found:',e)

#ValueError
import math
x = int(input("Enter Number:"))
# print(math.sqrt(x))

try:
    print(f'Squre root of {x} is {math.sqrt(x)}')
# except Exception as e:
#     print("Error occurred ",e) #type(e).__name__
except ValueError as e:
    print("Value error found - ",type(e).__name__,":",e)
else:
    print(x)
finally:
    print('Hello World!')


