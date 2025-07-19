# Strings

* We know what string are but we must also know that `string` takes more space than other datatypes like `int`, `float`, etc. This happens because `string` stores every character with their own **unicode**.
* **Unicode** is a universal character encoding standard that assigns a unique number **(code point)** to every charcater regardless of language.
* Like **"A"** unicode is **65**. We can check them by using `ord()` function in python and convert them back using `chr()` function.
* Strings in python are surrounded by either single quotation marks, or double quotation marks. `'hello'` is the same as `"hello"`.


## Strings are Arrays

- Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
- However, Python does not have a character data type, a single character is simply a string with a length of 1.
- **Square brackets** can be used to access elements of the string.
- Indexing starts with **0** and **negative indexing** (from the last) starts with **-1**.<br/>
    **Example:**
    ```python
    # Get the character at position 1 (remember that the first character has the position 0)
    a = "Hello, World!"
    print(a[1])         # positive indexing, o/p: e
    print(a[-2])        # negative indexing, o/p: d
    ```

## String Length

To get the length of a string, use the `len()` function.<br/>
**Example:**
```python
a = "Beerus"
print(len(a))
```

## Check String

To check if a certain phrase or character is present in a string, we can use the keyword `in`.<br/>
**Example:**
```python
txt = "Python is easy to learn"
print("free" in txt)
```

## Check if NOT

To check if a certain phrase or character is **NOT** present in a string, we can use the keyword `not in`.<br/>
**Example:**
```python
txt = "Python is easy to learn"
print("very" not in txt)
```

## Slicing

- We can return a range of characters by using the slice syntax.
- Specify the start index and the end index, separated by a colon, to return a part of the string.
- **[start:end:steps]** <br/>
    **Example:**
    ```python
    # Get the characters from position 0 to position 6 (not included)
    a = "Python Coder"
    print(a[0:6:1])
    ```

### Slice From the Start

By leaving out the start index, the range will start at the first character.

**Example:** Get the characters from the **start** to **position 5 (not included)**
```python
b = "Hello, World!"
print(b[:5])
```

### Slice To the End

By leaving out the end index, the range will go to the end.

**Example:** Get the characters from position 2, and all the way to the end:
```python
b = "Hello World!"
print(b[2:])
```

## Modify Strings

Python has a set of built-in methods that you can use on strings.

- **Upper Case:** The `upper()` method returns the string in upper case.
    ```python
    a = "Hello, World!"
    print(a.upper())
    ```
- **Lower Case:** The `lower()` method returns the string in lower case.
    ```python
    a = "Hello, World!"
    print(a.lower())
    ```
- **Remove Whitespace:**
    * Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
    * The `strip()` method removes any whitespace from the beginning or the end.
    ```python
    a = " Hello, World! "
    print(a.strip()) # returns "Hello, World!"
    ```


## String Methods

Python has a set of built-in methods that you can use on strings.

| Method         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `capitalize()` | Converts the first character to upper case                                 |
| `casefold()`   | Converts string into lower case                                             |
| `center()`     | Returns a centered string                                                   |
| `count()`      | Returns the number of times a specified value occurs in a string           |
| `encode()`     | Returns an encoded version of the string                                   |
| `endswith()`   | Returns True if the string ends with the specified value                   |
| `expandtabs()` | Sets the tab size of the string                                             |
| `find()`       | Searches the string for a specified value and returns its position         |
| `format()`     | Formats specified values in a string                                       |
| `format_map()` | Formats specified values in a string                                       |
| `index()`      | Searches the string for a specified value and returns its position         |
| `isalnum()`    | Returns True if all characters are alphanumeric                            |
| `isalpha()`    | Returns True if all characters are in the alphabet                         |
| `isascii()`    | Returns True if all characters are ASCII characters                        |
| `isdecimal()`  | Returns True if all characters are decimals                                |
| `isdigit()`    | Returns True if all characters are digits                                  |
| `isidentifier()`| Returns True if the string is an identifier                               |
| `islower()`    | Returns True if all characters are lower case                              |
| `isnumeric()`  | Returns True if all characters are numeric                                 |
| `isprintable()`| Returns True if all characters are printable                               |
| `isspace()`    | Returns True if all characters are whitespaces                             |
| `istitle()`    | Returns True if the string follows the rules of a title                    |
| `isupper()`    | Returns True if all characters are upper case                              |
| `join()`       | Joins the elements of an iterable to the end of the string                 |
| `ljust()`      | Returns a left-justified version of the string                             |
| `lower()`      | Converts a string into lower case                                          |
| `lstrip()`     | Returns a left-trimmed version of the string                               |
| `maketrans()`  | Returns a translation table to be used in translations                     |
| `partition()`  | Returns a tuple where the string is parted into three parts                |
| `replace()`    | Returns a string with a specified value replaced                           |
| `rfind()`      | Searches the string and returns the last position of a specified value     |
| `rindex()`     | Searches the string and returns the last position of a specified value     |
| `rjust()`      | Returns a right-justified version of the string                            |
| `rpartition()` | Returns a tuple where the string is parted into three parts                |
| `rsplit()`     | Splits the string at the specified separator, and returns a list           |
| `rstrip()`     | Returns a right-trimmed version of the string                              |
| `split()`      | Splits the string at the specified separator, and returns a list           |
| `splitlines()` | Splits the string at line breaks and returns a list                        |
| `startswith()` | Returns True if the string starts with the specified value                 |
| `strip()`      | Returns a trimmed version of the string                                    |
| `swapcase()`   | Swaps cases, lower case becomes upper case and vice versa                  |
| `title()`      | Converts the first character of each word to upper case                    |
| `translate()`  | Returns a translated string                                                |
| `upper()`      | Converts a string into upper case                                          |
| `zfill()`      | Fills the string with a specified number of 0 values at the beginning      |
