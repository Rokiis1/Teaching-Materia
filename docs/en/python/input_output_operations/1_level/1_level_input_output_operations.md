# Level 1

## Table of Contents: Inputs and Outputs Operations

- [Output with print](#output-with-print)
- [Print Separators](#print-separators)
- [Controlling Line Endings](#controlling-line-endings)
- [Escape Characters](#escape-characters)
- [User Input](#user-input)
- [Converting Numerical Input](#converting-numerical-input)
- [Basic String Formatting](#basic-string-formatting)

Python programs often need to communicate with the user. They can **display output** on the screen and **receive input** entered by the user. Python provides the `print()` function for displaying values and the `input()` function for reading text entered through the console.

In this **Inputs and Outputs Operations Level 1**, we will learn the foundations of console input and output. We will begin with `print()`, then control how printed values are separated and where the next output appears. After that, we will use escape characters, read user input, convert numerical input, and introduce basic string formatting with f-strings and the `%` operator.

## Output with print

The `print()` function displays text, numbers, variables, and other values on the screen. A simple call can display one value. Several values can also be passed to `print()` by separating them with commas. Python places a space between these values by default, and the values do not need to have the same data type.

```py
print("Hello, Python") # Hello, Python

name = "Vardenis"
age = 20

print("Name:", name, "Age:", age) # Name: Vardenis Age: 20
```

Calling `print()` without any arguments outputs a blank line. This can be useful when a small visual gap makes console output easier to read.

``` py
print("First section") # First section
print() # (blank line)
print("Second section") # Second section
```

This makes `print()` useful for displaying both fixed messages and stored values. When several values are printed together, however, a space is not always the separator we want. The next section shows how the `sep` parameter changes what appears between printed values.

## Print Separators

When `print()` receives several values, the `sep` parameter controls what Python places between them. The default separator is a single space, but a custom separator can be supplied when the output needs a different structure.

```py
print("Python", "is", "fun") # Python is fun
print("2026", "09", "06", sep="-") # 2026-09-06
```

The separator is inserted only **between** the values passed to `print()`. It does not change the values themselves. While `sep` controls what appears between values, Python also allows us to control what appears after the complete output. The next section introduces the `end` parameter for this purpose.

## Controlling Line Endings

By default, `print()` finishes its output with a newline, so the next `print()` call starts on a new line. The `end` parameter changes what is written after the displayed values, which allows following output to continue on the same line.

```py
print("First") # First
print("Second") # Second

print("Loading", end="...")
print("Done") # Loading...Done
```

!!! note "Default Behavior"

    The default value of `end` is `"\n"`, which represents a newline. Changing `end` affects where the following output begins.

The newline represented by `\n` is also an example of an escape sequence. Escape sequences can be placed inside strings to represent special characters, which is the focus of the next section.

## Escape Characters

**Escape characters** represent special characters inside strings. They begin with a backslash `\` followed by another character. Common escape sequences include `\n` for a newline and `\t` for a horizontal tab. Escape sequences can also represent quotation marks and backslashes when those characters need special handling inside a string.

```py
print("Hello\nWorld")
# Hello
# World

print("Hello\tWorld") # Hello   World
print("She said, \"Hello\"") # She said, "Hello"
print('It\'s a nice day') # It's a nice day
print("C:\\Users\\Student") # C:\Users\Student
```

The `\n` escape sequence starts a new line inside the same string and provides a simple way to produce multiline output. The `\t` sequence inserts horizontal tab spacing, although its exact visual width can vary between terminals and editors. The sequences `\"` and `\'` allow quotation marks to appear when the same quotation mark is used to delimit the string, while `\\` represents a backslash.

Escape sequences give us more control over text that a program displays. So far, however, all values have already been stored in the program. The next section introduces `input()`, which allows a program to receive text from the user while it is running.

## User Input

The `input()` function pauses the program and waits for the user to enter a value. The text passed to `input()` is displayed as a prompt, and the entered value can be assigned to a variable for later use. Prompt strings can use either single or double quotation marks, just like other Python strings.

```py
name = input("Enter your name: ") # Enter your name: Vardenis
print("Hello,", name) # Hello, Vardenis

age = input("Enter your age: ") # Enter your age: 20
print(age) # 20
print(type(age)) # <class 'str'>
```

**`input()` always returns a string**, even when the user enters characters that look like a number. The `type()` function in the example confirms that entering `20` still produces a value of type `str`. This matters because numerical calculations require numerical values rather than strings. The next section shows how input can be converted before it is used in arithmetic.

## Converting Numerical Input

When the user should enter a whole number, the result of `input()` can be converted with `int()`. Decimal input can be converted with `float()`. After conversion, the resulting values can be used in numerical operations.

```py
age = int(input("Enter your age: ")) # Enter your age: 20
print(type(age)) # <class 'int'>

height = float(input("Enter your height in meters: ")) # Enter your height in meters: 1.75
print(type(height)) # <class 'float'>

next_age = age + 1
print("Next year you will be", next_age) # Next year you will be 21
print("Your height is", height, "meters") # Your height is 1.75 meters
```

!!! warning "Convert Numerical Input Before Arithmetic"

    A value returned directly by `input()` is a string. Trying to add an integer to that string raises `TypeError`.

    ```py
    result = input("Enter a number: ") + 5
    # TypeError: can only concatenate str (not "int") to str
    ```

    If the user enters `10`, Python cannot add the string `"10"` to the integer `5`. Convert the input first when a numerical value is required.

    ```py
    result = int(input("Enter a number: ")) + 5
    print(result) # 15
    ```

`int()` and `float()` also require input that can actually be converted to the requested numerical type. If the user enters text such as `"abc"` when a number is expected, Python raises an error. Handling invalid input safely is introduced later when error handling is covered.

Once input has been converted into the required type, it can be used in calculations and displayed with explanatory text. The next section introduces basic string formatting, which provides a convenient way to combine text and values in the same output.

## Basic String Formatting

Programs often need to combine text with values. An **f-string** allows variables and expressions to be inserted directly into a string by placing them inside curly braces `{}`. The letter `f` before the opening quotation mark tells Python to evaluate the values inside those braces and insert their results into the string. **F-strings are the preferred method for string formatting in modern Python**, so they are the main formatting style to learn and use first. In the following example, `height` represents a height value that could have been collected and converted earlier.

```py
name = "Vardenis"
age = 20
height = 1.75

print(f"{name} is {age} years old") # Vardenis is 20 years old
print(f"Height: {height} meters") # Height: 1.75 meters
print(f"Next year you will be {age + 1}") # Next year you will be 21
```

Python also supports the older `%` formatting style. The symbols `%s`, `%d`, and `%f` are **placeholders** that mark where values will be inserted. `%s` represents a string, `%d` represents an integer, and `%f` represents a floating point value. A placeholder can also include additional formatting information. For example, `%.2f` is a floating point placeholder that displays two digits after the decimal point.

```py
name = "Vardenis"
age = 20
height = 1.75

print("%s is %d years old" % (name, age)) # Vardenis is 20 years old
print("%s is %d years old and %.2f meters tall" % (name, age, height)) # Vardenis is 20 years old and 1.75 meters tall
```

At this **Inputs and Outputs Operations Level 1**, the important idea is that formatting allows values to be inserted into strings. **Inputs and Outputs Operations Level 2** builds on this foundation by introducing f-string format specifiers for padding, alignment, width, precision, and additional numeric formatting.
