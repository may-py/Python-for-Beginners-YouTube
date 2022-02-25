# # Range Function
# #range(start, end, step)
# x = range(0,50,10)
#
# print(x)
# print(type(x))
# print(list(x))
#
#
# #Repeat the code
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# #
# #
# for i in range(0,3):
#     print('Hello World',i+1)
# #
# #
# sum = 0
# for i in range(0,500000): #1+2+3+4
#     sum = sum+i  #0+1=1 #1+1=2
# print(sum)
# #
# #
# #
# fruits = ["apple", "banana", "cherry"]
# #
# #
# for x in fruits:
#     print("Hello World",x)
# #
# #
# num = [0, 1, 2,3,4]
#
# for i in num:
#     print(i)
# else:
#     print("No items left.")
# #
# #
# student_name = 'Xyz'
#
# marks = {'Mayur': 90, 'Jeki': 55, 'Rikin': 77}
#
# for student in marks:
#     if student == student_name:
#         print(marks[student])
#         break
# else:
#     print('No entry with that name found.')
#
#
#
#
# # outer loop
# for i in range(1, 11):
#     for j in range(1, 11):
#         # print multiplication
#         print(i * j, end=' ')
#     print()

import re

result = re.findall('welcome to touring','welcome',1)
print(result)
