# x = int(input("Enter number: "))
# y = int(input("Enter number: "))
#
# try:
#     z = x/y
#     # a = 'baby yoda' + (x*y)
# except Exception as e:
#     print("Exception occured: ", e)
#     z = 0
# # except TypeError as te:
# #     print("Exception occured: ", te)
# #     a = 0
#
# print("division is: ", z)

try:
    print(1)
    print(20 / 0)
    print(2)
except ZeroDivisionError as z:
    print("Exception occured: ", 3)
finally:
    print(4)
