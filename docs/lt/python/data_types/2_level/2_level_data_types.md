# Table of Contents: Python Data Types Level 2

- [Sequence Types](#sequence-types)
- [Mapping Types (Dictionary)](#mapping-types-dictionary)
- [Set Types](#set-types)
- [Collection Type Casting](#collection-type-casting)

In **Python Data Types Level 1**, we introduced basic data types and several ways to describe them. We worked with strings, numbers, Boolean values, and `None`, and we also discussed ideas such as mutability, order, and type casting. This level builds on those ideas by focusing on collections, which allow multiple items to be grouped inside a single container.

Python provides several built-in collection and sequence types, including `list`, `tuple`, `range`, `dict`, `set`, and `frozenset`. Each type provides a different way to organize and work with multiple values. Strings are also sequence types, but they were introduced in **Python Data Types Level 1**. We will begin with sequence types before moving on to dictionaries, sets, and collection type casting.

## Sequence Types

A **list** is an **ordered** and **mutable** collection that can store multiple values. Lists are commonly used when the stored items may need to change during program execution, such as a collection of products, menu options, or records. An empty list can be created with square brackets, and the `type()` function can be used to confirm that the created value is a `list`.

```py
# Empty list literal
empty_list = []

print(type(empty_list)) # <class 'list'>
```

A list can contain values of the same data type or values of different data types.

```py
# Single data type list literal
single_data_type_list = ["apple", "orange", "banana"]

# Multiple data type list literal
multi_data_type_list = ["Hello", 20, True]
```

A **tuple** is an **ordered** and **immutable** collection that can also store multiple values. Tuples are useful when values belong together and should not be changed in place after the tuple has been created. An empty tuple can be created with parentheses. Tuples can contain values of a single data type or multiple data types, and the number of items can be checked using `len()`.

```py
# Empty tuple literal
empty_tuple = ()

# Single data type tuple literal
single_data_type_tuple = ("apple", "orange", "banana")

# Multiple data type tuple literal
multi_data_type_tuple = ("Hello", 20, True)

# Length of the tuple
print(len(multi_data_type_tuple))  # 3
```

A tuple containing only one item needs a trailing comma. Without the comma, Python treats the value as a normal expression inside parentheses rather than as a tuple.

```py
single_item = ("apple")

print(type(single_item)) # <class 'tuple'>
```

A common use of tuples is storing **fixed records**, such as coordinates, configuration values, or other groups of values where each position has a specific meaning.

> **Note:** Choose a tuple when the values should remain fixed as a group. Use a list when the collection needs to be changed in place.

The final sequence type introduced in this section is `range`. A `range` object is **ordered** and **immutable**, and it is commonly used when working with repeated steps or sequences of integers. Its general form is shown below.

```py
range(start, stop, step)
```

The `start` value is optional and defaults to `0`. The `stop` value is required and is not included in the generated sequence. The `step` value is optional and defaults to `1`. For example, `range(5)` represents the integers from `0` through `4`. A `range` object represents this sequence without immediately displaying all of its values, so converting it to a list is a simple way to inspect the values it represents.

```py
my_range = range(5)

print(list(my_range)) # [0, 1, 2, 3, 4]
```

A starting value can also be provided, and a third argument can be used to control the step between values.

```py
my_range = range(1, 5)
print(list(my_range)) # [1, 2, 3, 4]

my_range = range(1, 6, 2)
print(list(my_range)) # [1, 3, 5]
```

In programs, `range` is commonly used to represent positions, repetitions, or controlled numeric sequences without first storing every number in a separate list. Sequence types organize values by position, while the next collection type organizes related values using keys.

## Mapping Types (Dictionary)

A **dictionary** is a **mutable mapping** that stores data as **key value pairs**. Each key identifies its associated value, which makes dictionaries useful when data has meaningful labels, such as configuration settings, user profiles, or other named values.

An empty dictionary can be created with curly braces. A dictionary containing data places each key together with its associated value.

```py
dict_element = {}

example_dict = {
    "name": "Example",
    "age": 30,
    "is_member": True,
    "balance": 99.95
}
```

Dictionary keys must be **unique**. If the same key is written more than once in a dictionary literal, the later value replaces the earlier one. Dictionaries organize values through key value pairs, while the next collection type focuses on storing unique values.

## Set Types

A **set** is a mutable, non-indexed collection that stores **unique values**. If duplicate values are provided, only one instance of each value is kept. Sets are useful for removing duplicates, tracking unique values, and comparing groups of data. Python also provides `frozenset`, which stores unique values like a set but is **immutable**. An empty set must be created with `set()`, while non-empty sets can be written with curly braces.

```py
empty_set = set()

example_set = {1, 2, 3, 3, 2, 4}

print(example_set)
```

> **Note:** `{}` creates an empty dictionary, not an empty set. Non-empty sets can be written with curly braces, such as `{1, 2, 3}`.

Duplicate values are removed, so the set contains one instance of each unique value. Because sets are non-indexed, their displayed order should not be relied on. A `frozenset` stores unique values like a set, but it cannot be modified after it has been created.

```py
frozen_set_element = frozenset({1, 2, 3, 3, 2, 4})

print(frozen_set_element)
```

Because a `frozenset` is immutable, it can also be **hashable** when its elements are hashable. This gives the idea of hashability introduced in **Python Data Types Level 1** a practical use. A `frozenset` can be used in places where a mutable `set` cannot, such as a dictionary key or as an element inside another set.

```py
permissions = frozenset({"read", "write"})

example_dict = {
    permissions: "editor"
}

print(example_dict[permissions]) # editor
```

Now that the main collection types have been introduced, the next section shows how built-in constructors such as `list()`, `tuple()`, `set()`, and `dict()` can convert compatible values between collection types.

## Collection Type Casting

Collection type casting uses built-in constructors to create one collection type from another compatible value. This follows the same general idea of type casting introduced in **Python Data Types Level 1**. For example, a string can be converted to a list, where each character becomes a separate list element.

```py
text = "apple"
new_list = list(text)

print(new_list) # ['a', 'p', 'p', 'l', 'e']
```

A list can be converted to a tuple, while a string can be converted to a set. When a string is converted to a set, repeated characters are kept only once because sets store unique values.

```py
numbers = [1, 2, 3]
new_tuple = tuple(numbers)

print(new_tuple)  # (1, 2, 3)

letters = set("apple")

print(letters)
```

The displayed order of a set should not be relied on, but the resulting set contains the unique characters `a`, `p`, `l`, and `e`. A sequence of key value pairs can also be converted to a dictionary with `dict()`, where each pair provides a key and its associated value.

```py
person_data = [
    ("name", "Example"),
    ("age", 30)
]

person = dict(person_data)

print(person) # {'name': 'Example', 'age': 30}
```

These constructors make it possible to choose the collection type that best suits a particular task. **Python Data Types Level 3** builds on these concepts by exploring how values within collections are accessed and how different collection types behave.
