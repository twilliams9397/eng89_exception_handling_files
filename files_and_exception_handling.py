# print(1/0) # ZeroDivisionError: division by zero
#
# num = 9
# if num > 8 # SyntaxError: invalid syntax
#     print(num)

# create a file with required permission and see what errors/exceptions are possible to be seen

# first iteration
# file = open("order.txt") # open takes a str arg with file name and extension
# print(file) # FileNotFoundError: [Errno 2] No such file or directory: 'order.txt'

# second iteration, without file

try:
    file = open("order.txt")
    print("File found.")
except FileNotFoundError as errmsg: # creating alias (nickname) as variable
    print(f"File not found: {errmsg}.") # this block will run as file is not found in try block
finally:
    print("Thank you for visiting, see you again!") # this block runs regardless of try and except

# now create order.txt file
# above code will return File found and finally block

# apply DRY - OOP - Python Packaging
#        1     2          3
# 1 create function to execute above
# 2 within a class
# 3 place within package so can be imported
