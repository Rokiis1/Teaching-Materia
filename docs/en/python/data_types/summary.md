# Summary

This summary brings together concepts from the **Data Types** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships and differences need to be explained clearly.

## Table of Contents: Data Types

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **mutable and immutable objects, ordered and unordered types, core built-in data types, and type casting**. The main goal is to recognize the kinds of values Python provides, understand their basic properties, and explain how values can be converted between compatible types.

**Mutable objects** can be modified in place after they are created. Lists, dictionaries, and sets are common mutable collection types. **Immutable objects** cannot be changed in place. Common examples include `int`, `float`, `complex`, `bool`, `str`, `tuple`, `NoneType`, and `frozenset`. An operation that appears to change an immutable value creates or assigns a different object rather than modifying the original.

The important distinction is that **mutation changes an existing object**, while **reassignment makes a variable refer to another object**. Reassignment is possible regardless of whether the original object is mutable or immutable. Some immutable objects are also hashable, allowing them to be used as dictionary keys or set elements. A tuple containing only hashable values can be a dictionary key, while a list cannot.

**Ordered types** such as `list`, `tuple`, and `str` preserve the positions of their elements and support position-based access through indexes. **Unordered types** such as `set` do not provide a defined element order or positional indexing. Dictionaries preserve insertion order, but they are key-based mappings rather than index-based sequences. Their values are retrieved through keys, not numeric positions.

The distinction between ordering and mutability is important because they describe different properties. A list is ordered and mutable, a tuple is ordered and immutable, and a set is mutable but unordered. These characteristics help determine how a collection can be accessed and changed.

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

The **`None` value** represents the absence of a value and is immutable. It is distinct from `False`, `0`, and `""`, which represent actual Boolean, numeric, and text values. Although all four are falsy, they are not equal.

```py
example_none = None

print(None == False) # False
print(None == 0) # False
print(None == "") # False
```

**Type conversion**, also called **type casting**, converts a value to another type when a different representation is needed. The constructors `float()`, `int()`, `str()`, and `bool()` perform common conversions. A conversion succeeds only when the source value is suitable for the requested type.

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
