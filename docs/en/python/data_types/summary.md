# Summary

This summary brings together the most important concepts from the **Data Types** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships and differences need to be explained clearly.

## Table of Contents: Data Types

- [Level 1](#level-1)

## Level 1

Level 1 reviews **mutability and ordering**, the core built-in types, **`type()` and `len()`**, and basic **type casting**. The focus is on recognizing the properties of values, inspecting them, and understanding which conversions are possible.

**Mutable objects** can be modified in place after they are created. Lists, dictionaries, and sets are common mutable collection types. **Immutable objects** cannot be changed in place. Common examples include `int`, `float`, `complex`, `bool`, `str`, `tuple`, `NoneType`, and `frozenset`. An operation that appears to change an immutable value creates or assigns a different object rather than modifying the original.

**Mutation changes an existing object**, while **reassignment makes a variable refer to another object**. Reassignment is possible regardless of the original object's mutability. Some immutable objects are also **hashable**, allowing them to be used as dictionary keys or set elements. A tuple containing only hashable values can be a dictionary key, while a list cannot.

**Ordered types** such as `list`, `tuple`, and `str` preserve the positions of their elements and support position-based access through indexes. **Unordered types** such as `set` do not provide a defined element order or positional indexing. Dictionaries preserve insertion order, but they are key-based mappings rather than index-based sequences. Their values are retrieved through keys, not numeric positions.

Ordering and mutability are independent properties. A list is ordered and mutable, a tuple is ordered and immutable, and a set is mutable but unordered.

Python's three numeric types are **`int`, `float`, and `complex`**, and all three are immutable. An `int` represents whole numbers, a `float` represents decimal numbers, and a `complex` value contains real and imaginary parts. Python writes the imaginary part using `j`.

```py
integer_value = 30
floating_value = 19.99
complex_number = 2 + 3j

print(integer_value) # 30
print(floating_value) # 19.99
print(complex_number) # (2+3j)
```

Integers and floating-point numbers are used for most introductory quantities, such as counts, prices, and measurements. Complex numbers are more specialized and are useful in mathematical, scientific, and engineering calculations. Numeric literals can also contain underscores to improve readability, as in `1_000_000`.

The **`str` type** represents text as an ordered, immutable sequence of characters. Strings can be created with single, double, or triple quotes. They support operations such as concatenation, which joins strings, and slicing, which extracts part of a string.

```py
double_quotes = "Hello"
single_quotes = 'Hello'
triple_quotes = """Hello"""

print(double_quotes) # Hello
print(single_quotes) # Hello
print(triple_quotes) # Hello
```

The **`bool` type** is immutable and has two values, `True` and `False`. Python can also interpret non-Boolean values as true or false, a property known as **truthiness**. `False`, `None`, numeric zero, and empty strings or collections are falsy, while most nonzero numbers and nonempty strings or collections are truthy.

```py
print(bool(0)) # False
print(bool("")) # False
print(bool(None)) # False
print(bool(10)) # True
print(bool("Python")) # True
```

The **`None` value** is immutable and represents the absence of a value. Unlike `False`, `0`, and `""`, it does not represent an actual Boolean, numeric, or text value. Although all four are falsy, they are not equal.

```py
example_none = None

print(None == False) # False
print(None == 0) # False
print(None == "") # False
```

The core types can also be inspected with built-in functions. **`type()`** returns an object's type, while **`len()`** returns the number of elements in an object that supports a length. These functions are useful for checking values and understanding the structure of data.

```py
print(float(5)) # 5.0
print(int(3.14)) # 3
print(str(42)) # 42
print(bool("hello")) # True
print(bool("")) # False

number_text = "42"
number = int(number_text)
print(number) # 42
```

The `int()` constructor **truncates floating-point values toward zero** rather than rounding them to the nearest whole number. Both positive and negative values lose their fractional parts.

```py
print(int(3.99)) # 3
print(int(-3.99)) # -3
```

Not every value can be converted to every type. For example, `"42"` can be converted to an integer, but `"hello"` cannot. An unsuccessful conversion raises a `ValueError` and stops normal execution unless the error is handled.

```py
number = int("hello") # ValueError
```

The important distinctions are that **mutability describes whether an object can change in place**, **ordering describes how elements are organized**, and **type casting changes a value's representation when conversion is possible**. These properties are separate and help explain why different types support different operations.

After reviewing Level 1, you should be able to explain **mutable and immutable objects**, distinguish **mutation from reassignment**, describe **ordered and unordered types** and the key-based nature of dictionaries, recognize the purposes of **`int`, `float`, `complex`, `str`, `bool`, and `None`**, explain **truthy and falsy values**, distinguish **`None` from other falsy values**, use **`float()`, `int()`, `str()`, and `bool()`** for basic conversions, and explain **truncation and failed conversions**.
