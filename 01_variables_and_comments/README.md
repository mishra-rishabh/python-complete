# Variables and Comments

## Comments

- Comments can be used to explain Python code.
- Comments can be used to make the code more readable.
- Comments starts with a `#`, and Python interpreter will ignore them.

### Multi-Line Comment

- Python does not really have a syntax for multiline comments.
- Since Python will ignore **string literals** that are not assigned to a variable, we can add a **multiline string (triple quotes)** in our code, and place our comment inside it.
- This **String Literal** is called **Doc String**.
    ```python
    """
    This is a multi-line comment
    """
    ```


## Variables

- Variables are containers for storing data values.
- Python has no command for declaring a variable.
- A variable is created the moment you first assign a value to it. <br/>
    **Example:**
    ```python
    x = 3
    name = "Naruto"
    ```
- Variables do not need to be declared with any particular type, and can even change type after they have been set. <br/>
    **Example**
    ```python
    x = 5           # x is of type int
    x = "Naruto"    # x is now of type str
    ```

### Rules for Python Variables

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.

    **Legal Variable Names**
    ```python
    myvar = "Naruto"
    my_var = "Naruto"
    _my_var = "Naruto"
    myVar = "Naruto"
    MYVAR = "Naruto"
    myvar2 = "Naruto"
    ```

    **Illegal Variable Names**
    ```python
    2myvar = "Naruto"
    my-var = "Naruto"
    my var = "Naruto"
    ```

### Naming Convention

* Camel Case: `animeCharacter = "Light Yagami"`
* Pascal Case: `AnimeCharacter = "Light Yagami"`
* Snake Case: `anime_character = "Light Yagami"`