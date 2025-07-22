# Loops

Loops allow us to execute a block of code multiple times without rewriting it.


## The range() Function

- To loop through a set of code a specified number of times, we can use the `range()` function.
- The `range()` function returns a sequence of numbers, starting from **0** by default, and increments by **1 (by default)**, and ends at a specified number.
- The `range()` function defaults to **0** as a starting value, however it is possible to specify the starting value by adding a parameter: `range(2, 6)`, which means values from **2** to **6 (but not including 6)**.
- The `range()` function defaults to increment the sequence by **1**, however it is possible to specify the increment value by adding a third parameter: `range(2, 30, 3)`


## Types of Loops

In Python, there are 2 types of loops-
- **For loop**
- **While loop**


## 1. For Loops

- A `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
- This is less like the `for` keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
- With the `for` loop we can execute a set of statements, once for each item in a list, tuple, set etc.

    ```python
    for x in range(6):
        print(x)
    ```

### The break Statement

With the `break` statement we can stop the loop before it has looped through all the items.

```python
for i in range(1, 21):
    if (i == 15):
        break
    else:
        print(i)
```

### The continue Statement

With the `continue` statement we can stop the current iteration of the loop, and continue with the next.

```python
for i in range(1, 21):
    if (i == 15):
        continue
    else:
        print(i)
```

### Else in For Loop

The `else` keyword in a `for` loop specifies a block of code to be executed when the loop is finished.

```python
# Print all numbers from 0 to 5, and print a message when the loop has ended
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```

**Note**: The `else` block will **NOT** be executed if the loop is stopped by a `break` statement.

```python
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
```