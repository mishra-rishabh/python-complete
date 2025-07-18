# Datatypes

A data type defines the kind of value a variable can hold and how the computer should interpret it. Variables can store data of different types, and different types can do different things.

## Built-in Data Types

Python has the following data types built-in by default, in these categories:
- **Text Type**: `str`
- **Numeric Types**: `int`, `float`, `complex`
- **Sequence Types**: `list`, `tuple`, `range`
- **Mapping Type**: `dict`
- **Set Types**: `set`, `frozenset`
- **Boolean Type**: `bool`
- **Binary Types**: `bytes`, `bytearray`, `memoryview`
- **None Type**: `NoneType`


## Getting the Data Type

We can get the data type of any object by using the `type()` function.<br/>
**Example:**
```python
x = 5
y = "Zoro"
print(type(x))
print(type(y))
```


## Setting the Data Type

In Python, the data type is set when we assign a value to a variable.

| Example                              | Data Type    |
|--------------------------------------|--------------|
| `x = "Hello World"`                  | `str`        |
| `x = 20`                             | `int`        |
| `x = 20.5`                           | `float`      |
| `x = 1j`                             | `complex`    |
| `x = ["apple", "banana", "cherry"]` | `list`       |
| `x = ("apple", "banana", "cherry")` | `tuple`      |
| `x = range(6)`                       | `range`      |
| `x = {"name": "John", "age": 36}`   | `dict`       |
| `x = {"apple", "banana", "cherry"}` | `set`        |
| `x = frozenset({"apple", "banana", "cherry"})` | `frozenset` |
| `x = True`                           | `bool`       |
| `x = b"Hello"`                       | `bytes`      |
| `x = bytearray(5)`                  | `bytearray`  |
| `x = memoryview(bytes(5))`          | `memoryview` |
| `x = None`                           | `NoneType`   |


## Setting the Specific Data Type

If we want to specify the data type, we can use the constructor functions.

| Example                                               | Data Type    |
|--------------------------------------------------------|--------------|
| `x = str("Hello World")`                               | `str`        |
| `x = int(20)`                                          | `int`        |
| `x = float(20.5)`                                      | `float`      |
| `x = complex(1j)`                                      | `complex`    |
| `x = list(("apple", "banana", "cherry"))`              | `list`       |
| `x = tuple(("apple", "banana", "cherry"))`             | `tuple`      |
| `x = range(6)`                                         | `range`      |
| `x = dict(name="John", age=36)`                        | `dict`       |
| `x = set(("apple", "banana", "cherry"))`               | `set`        |
| `x = frozenset(("apple", "banana", "cherry"))`         | `frozenset`  |
| `x = bool(5)`                                          | `bool`       |
| `x = bytes(5)`                                         | `bytes`      |
| `x = bytearray(5)`                                     | `bytearray`  |
| `x = memoryview(bytes(5))`                             | `memoryview` |


## Casting

If we want to specify the data type of a variable, this can be done with casting.<br/>
**Example:**
```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```


