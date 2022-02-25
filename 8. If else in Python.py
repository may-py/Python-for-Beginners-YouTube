if True:
    print("It is True")

if False:
    print("It is False")

# # #
if False:
    print("It is True")
else:
    print('It is False')


# Relational operators ==, >, <, >=, <= , !=
a = 6
#
# if a == 7:
#     print('It does match')
# else:
#     print('It does not match')
#
#
# if a==5:
#     print('It is a number 5')
#
# if a==6:
#     print('It is a number 6')
#
# if a==7:
#     print('It is a number 7')

#
if a == 5:
    print('It is a number 5')
elif a == 6:
    print('It is a number 6')
elif a == 7:
    print('It is a number 7')




num = float(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")