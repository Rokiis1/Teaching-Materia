# Summary

This summary brings together the most important concepts from the **Inputs and Outputs Operations** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships and differences need to be explained clearly.

## Table of Contents: Inputs and Outputs Operations

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **console output, user input, numerical input conversion and basic string formatting**. The main goal is to understand how Python displays values, receives text from the user, converts numerical input and combines values with readable messages.

The **`print()` function** displays text, numbers, variables and other values on the screen. It can receive one or several values, and values separated by commas are displayed with a space between them by default. The values do not need to have the same data type.

``` py
print("Hello, Python") # Hello, Python

name = "Vardenis"
age = 20
print("Name:", name, "Age:", age) # Name: Vardenis Age: 20
```

Calling `print()` without arguments outputs a blank line, which can be useful for separating sections of console output.

``` py
print("First section") # First section
print() # (blank line)
print("Second section") # Second section
```

The **`sep` parameter** controls what appears between values passed to `print()`. Its default value is a single space, and a custom separator is inserted only between the values rather than changing the values themselves.

``` py
print("Python", "is", "fun") # Python is fun
print("2026", "09", "06", sep="-") # 2026-09-06
```

The **`end` parameter** controls what is written after a `print()` call. By default, `print()` ends with a newline, represented by `"\n"`. Changing `end` allows following output to continue on the same line.

``` py
print("First") # First
print("Second") # Second

print("Loading", end="...")
print("Done") # Loading...Done
```

The important distinction is that **`sep` controls the text between values within one call**, while **`end` controls the text written after that call**. Both affect the presentation of output without changing the values being displayed.

**Escape sequences** represent special characters inside strings and begin with a backslash `\`. The sequence `\n` creates a newline, `\t` inserts a horizontal tab, `\"` and `\'` represent quotation marks, and `\\` represents a backslash.

``` py
print("Hello\nWorld")
# Hello
# World

print("Hello\tWorld") # Hello   World
print("She said, \"Hello\"") # She said, "Hello"
print('It\'s a nice day') # It's a nice day
print("C:\\Users\\Student") # C:\Users\Student
```

The exact visual width of a tab can vary between terminals and editors. Escaping a quotation mark is useful when that same quotation mark delimits the string. The distinction between `end="\n"` and `\n` inside a string is that the former controls the ending of a `print()` call, while the latter creates a newline within the string itself.

The **`input()` function** pauses the program and waits for the user to enter text. Its optional prompt is displayed before the user enters a value. Prompt strings can use either single or double quotation marks, and the returned value can be assigned to a variable.

``` py
name = input('Enter your name: ') # Enter your name: Vardenis
print("Hello,", name) # Hello, Vardenis

age = input("Enter your age: ") # Enter your age: 20
print(age) # 20
print(type(age)) # <class 'str'>
```

**`input()` always returns a string**, even when the user enters characters that look like a number. The `type()` function can verify the resulting type. Numerical input must therefore be converted before it is used in arithmetic.

The **`int()` function** converts suitable input to an integer, while **`float()`** converts suitable input to a floating point number. After conversion, the values can be used in numerical calculations.

``` py
age = int(input("Enter your age: ")) # Enter your age: 20
print(type(age)) # <class 'int'>

height = float(input("Enter your height in meters: ")) # Enter your height in meters: 1.75
print(type(height)) # <class 'float'>

next_age = age + 1
print("Next year you will be", next_age) # Next year you will be 21
print("Your height is", height, "meters") # Your height is 1.75 meters
```

Trying to add an integer directly to a string returned by `input()` raises **`TypeError`**. The input must first be converted to a suitable numerical type.

``` py
result = input("Enter a number: ") + 5
# TypeError: can only concatenate str (not "int") to str
```

``` py
result = int(input("Enter a number: ")) + 5
print(result) # 15
```

Conversion can also fail when the entered text is not valid for the requested type. For example, `int("abc")` and `float("abc")` raise **`ValueError`**. Handling invalid input safely belongs to later error-handling lessons, but the important Level 1 rule is to recognize that conversion requires suitable input.

**String formatting** combines text with values. An **f-string** begins with `f` before the opening quotation mark and uses curly braces `{}` to insert variables or evaluate expressions. F-strings are the preferred method for string formatting in modern Python and are the main formatting style to learn and use first.

``` py
name = "Vardenis"
age = 20
height = 1.75

print(f"{name} is {age} years old") # Vardenis is 20 years old
print(f"Height: {height} meters") # Height: 1.75 meters
print(f"Next year you will be {age + 1}") # Next year you will be 21
```

Python also supports the older **`%` formatting style**. Its placeholders mark where values will be inserted. `%s` represents a string, `%d` represents an integer, and `%f` represents a floating point value. The placeholder `%.2f` displays a floating point value with two digits after the decimal point.

``` py
name = "Vardenis"
age = 20
height = 1.75

print("%s is %d years old" % (name, age)) # Vardenis is 20 years old
print("%s is %d years old and %.2f meters tall" % (name, age, height)) # Vardenis is 20 years old and 1.75 meters tall
```

The important distinction is that **f-strings place variables and expressions directly inside curly braces**, while **`%` formatting uses placeholders and supplies the corresponding values after the `%` operator**. Both can combine text with values, but f-strings are the preferred approach for new Python code. More detailed control over padding, alignment, width, precision and numeric presentation belongs to Level 2.

After reviewing Level 1, you should be able to explain **how `print()` displays values**, distinguish **`sep` from `end`**, recognize the purpose of **common escape sequences**, explain why **`input()` returns a string**, convert suitable input using **`int()` and `float()`**, recognize **`TypeError` and `ValueError`** in basic input situations, and distinguish **f-strings from `%` formatting** while using variables and simple expressions to produce readable output.
