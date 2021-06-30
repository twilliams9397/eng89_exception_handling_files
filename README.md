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
