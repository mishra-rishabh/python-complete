# Conditional Statements

Conditional statements allow decision-making by executing different blocks of code based on conditions.

Generally there are 3 types of variations in conditional statements.
- **if**
- **if-else**
- **if-elif-else**


## 1. if Statement

- An "**if statement**" is written by using the `if` keyword.
- It executes if the condition is `True`.
    
    ```python
    a = 33
    b = 200
    if b > a:
        print("b is greater than a")
    ```

### Indentation

Python heavily relies on **indentation** (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

If statement, without indentation (will raise an error):
```python
a = 33
b = 200
if b > a:
print("b is greater than a") # we will get an error
```


## 2. if-else Statement

- The `else` keyword catches anything which isn't caught by the preceding conditions.
    
    ```python
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    else:
        print("b is not greater than a")
    ```


## 3. if-elif-else Statement

- The `elif` keyword is Python's way of saying **"if the previous conditions were not true, then try this condition"**.
- Checks multiple conditions in sequence.

    ```python
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")
    ```


## pass Statement

- `if` statements cannot be empty, but if we for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.

    ```python
    a = 33
    b = 200

    if b > a:
        pass
    ```
