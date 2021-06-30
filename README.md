# Working with Files
## Exception Handling
### File Permissions

#### Error/Exception examples
- `ValueError`
- `SyntaxError`
- `AttributeError`
- `OutOfBounds`
- `KeyError`
- `ZeroDivisionError`
```python
print(1/0) # ZeroDivisionError: division by zero

num = 9
if num > 8 # SyntaxError: invalid syntax
    print(num)
```

#### File Permissions

- `r` This is the default mode to open file for reading
- `w` This mode opens file for writing. If file doesn't exist it creates a new file for us
- `x` Creates a new file, if already exists the operation fails
- `a` Opens the file in Append Mode, if file doesn't exist it creates a new one
- `t` This is the default mode to open in text mode
- `b` This is the default mode to open in binary
- `+` This will open for reading and writing (updating)

**we have `try`, `except` and `finally`**
- `try` works as `if` condition
- `except` works as `elif` condition
- `finally` works as `else` condition, will execute regardless of `try` and `except` conditions
```python
# create a file with required permission and see what errors/exceptions are possible to be seen

# first iteration
file = open("order.txt") # open takes a str arg with file name and extension
print(file) # FileNotFoundError: [Errno 2] No such file or directory: 'order.txt'

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
```
