# Level 1

## Table of Contents: Data Types

- [Mutable vs Immutable](#mutable-vs-immutable)
- [Ordered vs Unordered](#ordered-vs-unordered)
- [Core built-in data types](#core-built-in-data-types)
- [Built-in Functions](#built-in-functions)
- [Type casting](#type-casting)

**Data Types Level 1** introduces the basic kinds of values used in Python and several important ways to describe them. You will learn the difference between **mutable** and **immutable** objects, understand what **ordered** and **unordered** mean, explore the core built-in data types used for numbers, text, Boolean values, and the absence of a value, use **type()** and **len()** to inspect values, and perform basic **type casting**.

## Mutable vs Immutable

Python objects can be categorized by whether their contents can be changed after the object has been created. **Mutable types** can be modified in place. They are similar to a **whiteboard**, where the existing content can be erased or changed without replacing the whiteboard itself. Python collection types such as `list`, `dict`, and `set` are mutable. These collection types are covered in more detail in **Data Types Level 2**.

![Mutable Python types illustrated](./assets/images/mutable_type_intro_gif.gif)

**Immutable types** cannot be changed after they are created. They are similar to a **printed page**. The page itself cannot be edited after printing, so producing different content requires a new page. In Python, an operation that appears to change an immutable value creates or assigns a different object instead of modifying the original object in place.

Common immutable types include `int`, `float`, `complex`, `bool`, `str`, `tuple`, `NoneType`, and `frozenset`. Tuples are covered in more detail in **Data Types Level 2**, while `frozenset` is introduced later.

![Immutable Python types illustrated](./assets/images/immutable_type_intro_gif.gif)

Immutability matters because immutable objects can be used safely in situations where a value must remain stable. Some immutable objects are also **hashable**, which allows them to be used as dictionary keys or set elements. For example, a tuple containing only hashable values can be a dictionary key, while a list cannot.

!!! note "Reassignment is different from mutation"

    Mutable and immutable describe whether an object can be changed in place. Reassigning a variable is different because the variable can be made to refer to another object regardless of whether the original object is mutable or immutable.

The next distinction concerns how elements are organized and accessed, rather than whether an object can be changed.

## Ordered vs Unordered

Python collection and sequence types can also be described by whether they preserve a defined order and how their elements are accessed. **Ordered types** such as `list`, `tuple`, and `str` preserve the position of their elements. They are similar to a **bookshelf**, where each book has a specific place. These types support position-based access through an `index`. Their collection operations are covered in more detail in **Data Types Level 2**.

![Ordered Python types](./assets/images/ordered_types_intro.png)

**Unordered types** such as `set` do not preserve a defined element order and do not provide position-based access through indexes. A set is more like a **box of toys**, where you work with the items themselves rather than asking for an item at a particular position.

![Unordered Python types illustrated](./assets/images/unordered_types_intro.png)

Dictionaries are also not accessed by numeric position. Instead, a `dict` stores values associated with **keys**, and those keys are used to retrieve the corresponding values. Python dictionaries preserve insertion order, but they are still key-based mappings rather than index-based sequences.

These properties help explain how collections organize information. We can now examine the core built-in types used to represent individual values.

## Core Built-in Data Types

**Documentation and Code Style Level 1** introduced literals for numbers, text, Booleans, and `None`. We now examine their types and the kinds of information they represent.

Python provides the numeric types `int`, `float`, and `complex`. All three are **immutable**. An `int` stores whole numbers, a `float` stores decimal numbers, and `complex` stores numbers with real and imaginary parts. In Python, the imaginary part is written using `j`. For example, `2 + 3j` contains the real part `2` and the imaginary part `3j`.

```py
# Integer literals
integer_literal = 30
negative_integer = -7

# Floating point literals
floating_literal = 19.99
negative_float = -0.001

# Underscores can improve readability in numeric literals
large_integer = 1_000_000
large_float = 1_234.56

# Complex number literal
complex_number = 2 + 3j

print(complex_number) # (2+3j)
```

`int` and `float` are the numeric types you will use most often. The `complex` type is more specialized and is useful in mathematical, scientific, and engineering calculations, such as representing electrical signals or solving equations involving imaginary numbers. Numeric values also support arithmetic operations, which are explored in more detail in the Python operations material.

Programs also frequently need to store and process **text**. The `str` type represents text as an ordered, immutable sequence of characters. Strings can be created with single, double, or triple quotes. Triple quotes can also be used for multiline text and docstrings, as introduced in **Documentation and Code Style Level 1**.

```py
double_quotes = "Hello"
single_quotes = 'Hello'
triple_quotes = """Hello"""
```

Strings support operations such as **concatenation**, which joins strings together, and **slicing**, which extracts part of a string. More detailed string operations are introduced later in the course. While text and numbers represent data values, programs also need to represent logical truth values.

The `bool` type is immutable and has the values `True` and `False`. Python can also interpret non-Boolean values as true or false, a property known as **truthiness**.

```py
example_boolean_true = True
example_boolean_false = False
```

Values such as `False`, `None`, numeric zero, and empty strings or collections are **falsy**. Most nonzero numbers and nonempty strings or collections are **truthy**.

![Truthy and falsy values in Python](./assets/images/python_truthy_falsy_values.png)

The following examples use `bool()` to demonstrate how Python interprets these values.

```py
print(bool(0)) # False
print(bool("")) # False
print(bool(None)) # False
print(bool(10)) # True
print(bool("Python")) # True
```

Logical operators and more detailed uses of truthiness are covered later in **Operations Level 2**. Python also provides the immutable value `None` to represent the absence of a value. Unlike `False`, `0`, and `""`, which represent actual Boolean, numeric, or text values, `None` indicates that no value is present.

```py
example_none = None

print(None == False) # False
print(None == 0) # False
print(None == "") # False
```

The types introduced above can also be inspected using built-in functions. This provides a practical way to check what kind of object a variable refers to and, for suitable objects, how many elements it contains.

## Built-in Functions

**Documentation and Code Style Level 1** introduced `print()` and the basic syntax for calling functions. The built-in functions `type()` and `len()` extend those foundations by allowing us to inspect the types and sizes of objects without importing anything. The **`type()` function** returns the type of an object, making it useful for checking values while learning, inspecting data, or investigating unexpected results.

```py
integer_value = 30
floating_value = 19.99
complex_number = 2 + 3j
text = "Hello"
is_active = True
selected_item = None

print(type(integer_value)) # <class 'int'>
print(type(floating_value)) # <class 'float'>
print(type(complex_number)) # <class 'complex'>
print(type(text)) # <class 'str'>
print(type(is_active)) # <class 'bool'>
print(type(selected_item)) # <class 'NoneType'>
```

The `<class '...'>` notation is Python's representation of a type object. For example, `type(integer_value)` identifies `int`, while `type(selected_item)` identifies `NoneType`.

The **`len()` function** returns the number of elements in an object that supports a length. For a string, it counts characters. It also works with collections such as lists, tuples, dictionaries, and sets, which are explored in more detail in **Data Types Level 2**.

```py
text = "Python"

print(len(text)) # 6
```

The result is `6` because `"Python"` contains six characters. For collections, the same function counts items in a list, key-value pairs in a dictionary, or unique elements in a set.

Not every object supports a length. Numeric values such as integers and floating-point numbers do not, so passing an integer to `len()` raises a `TypeError`.

```py
print(len(42)) # TypeError
```

!!! warning "Length is not available for every type"

    A `TypeError` indicates that the supplied object does not support the requested operation. To count the digits of an integer, convert it to a string first, then use `len()` on that string.

Having inspected the types and sizes of values, we can now examine how to convert a value when a different representation is needed.

## Type casting

Python provides built-in constructors such as `float()`, `int()`, `str()`, and `bool()` that can perform **type conversion**, also called **type casting**. The `float()` constructor can convert an integer or a suitable numeric string to a floating-point number, while `int()` can convert an integer-like string or a floating-point number to an integer. The `str()` constructor produces a string representation of a value, while `bool()` produces its Boolean interpretation.

```py
# Original values
integer_value = 5
floating_value = 3.14
another_integer = 42
text_value = "hello"
empty_string = ""

# Type casting
converted_float = float(integer_value)
converted_integer = int(floating_value)
converted_string = str(another_integer)
boolean_nonempty = bool(text_value)
boolean_empty = bool(empty_string)

# Results
print(converted_float) # 5.0
print(converted_integer) # 3
print(converted_string) # 42
print(boolean_nonempty) # True
print(boolean_empty) # False
```

When `int()` converts a floating-point number, it **truncates toward zero** rather than rounding to the nearest whole number. Both positive and negative values lose their fractional parts.

```py
print(int(3.99)) # 3
print(int(-3.99)) # -3
```

A string containing a valid integer representation can also be converted with `int()`, which is useful when numeric information is initially stored as text.

```py
number_text = "42"
number = int(number_text)

print(number) # 42
```

A string such as `"hello"` does not represent an integer, so attempting to convert it with `int()` raises a `ValueError`.

```py
number = int("hello") # ValueError
```

!!! warning "Failed Conversion"

    A failed conversion stops normal execution unless the error is handled. Error handling is introduced later in the course.

**Data Types Level 2** builds on these foundations by examining how lists, tuples, dictionaries, and sets are created and converted between compatible collection types.
