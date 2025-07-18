# Operators

Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

## 1. Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations.

| Operator | Name           | Example   |
|----------|----------------|-----------|
| `+`      | Addition       | `x + y`   |
| `-`      | Subtraction    | `x - y`   |
| `*`      | Multiplication | `x * y`   |
| `/`      | Division       | `x / y`   |
| `%`      | Modulus        | `x % y`   |
| `**`     | Exponentiation | `x ** y`  |
| `//`     | Floor division | `x // y`  |


## 2. Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Example        | Same As        |
|----------|----------------|----------------|
| `=`      | `x = 5`        | `x = 5`        |
| `+=`     | `x += 3`       | `x = x + 3`    |
| `-=`     | `x -= 3`       | `x = x - 3`    |
| `*=`     | `x *= 3`       | `x = x * 3`    |
| `/=`     | `x /= 3`       | `x = x / 3`    |
| `%=`     | `x %= 3`       | `x = x % 3`    |
| `//=`    | `x //= 3`      | `x = x // 3`   |
| `**=`    | `x **= 3`      | `x = x ** 3`   |
| `&=`     | `x &= 3`       | `x = x & 3`    |
| `\|=`     | `x \|= 3`     | `x = x \| 3`   |
| `^=`     | `x ^= 3`       | `x = x ^ 3`    |
| `>>=`    | `x >>= 3`      | `x = x >> 3`   |
| `<<=`    | `x <<= 3`      | `x = x << 3`   |
| `:=`     | `print(x := 3)`| `x = 3` <br/>`print(x)`|


## 3. Comparison Operators

Comparison operators are used to compare two values.

| Operator | Name                        | Example   |
|----------|-----------------------------|-----------|
| `==`     | Equal                        | `x == y`  |
| `!=`     | Not equal                   | `x != y`  |
| `>`      | Greater than                | `x > y`   |
| `<`      | Less than                   | `x < y`   |
| `>=`     | Greater than or equal to    | `x >= y`  |
| `<=`     | Less than or equal to       | `x <= y`  |


## 4. Logical Operators

Logical operators are used to combine conditional statements.

| Operator | Description                                      | Example                          |
|----------|--------------------------------------------------|----------------------------------|
| `and`    | Returns `True` if both statements are true         | `x < 5 and x < 10`               |
| `or`     | Returns `True` if one of the statements is true    | `x < 5 or x < 4`                 |
| `not`    | Reverses the result, returns `False` if true       | `not(x < 5 and x < 10)`         |


## 5. Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

| Operator  | Description                                              | Example      |
|-----------|----------------------------------------------------------|--------------|
| `is`      | Returns True if both variables are the same object       | `x is y`     |
| `is not`  | Returns True if both variables are not the same object   | `x is not y` |


## 6. Membership Operators

Membership operators are used to test if a sequence is presented in an object.

| Operator   | Description                                                                  | Example        |
|------------|------------------------------------------------------------------------------|----------------|
| `in`       | Returns `True` if a sequence with the specified value is present in the object | `x in y`       |
| `not in`   | Returns `True` if a sequence with the specified value is not present in the object | `x not in y`   |


## 7. Bitwise Operators

Bitwise operators are used to compare (binary) numbers.

| Operator | Name                 | Description                                                                 | Example   |
|----------|----------------------|-----------------------------------------------------------------------------|-----------|
| `&`      | AND                  | Sets each bit to 1 if both bits are 1                                       | `x & y`   |
| `\|`      | OR                   | Sets each bit to 1 if one of two bits is 1                                  | `x \| y`   |
| `^`      | XOR                  | Sets each bit to 1 if only one of two bits is 1                             | `x ^ y`   |
| `~`      | NOT                  | Inverts all the bits                                                        | `~x`      |
| `<<`     | Zero fill left shift | Shifts bits left, pushing in 0s from the right and discarding leftmost bits | `x << 2`  |
| `>>`     | Signed right shift   | Shifts bits right, keeping sign bit (leftmost) and discarding rightmost     | `x >> 2`  |

