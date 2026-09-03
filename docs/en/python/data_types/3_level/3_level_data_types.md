# Table of Contents: Python Data Types Level 3

- [Indexed sequence types](#indexed-sequence-types)
- [Non-indexed and Non-subscriptable Types](#non-indexed-and-non-subscriptable-types)
- [How mutable and immutable data types work](#how-mutable-and-immutable-data-types-work)
- [List Data Type](#list-data-type)
- [Dictionary Data Type](#dictionary-data-type)
- [Set Data Type](#set-data-type)
- [Strings Data type](#strings-data-type)
- [Tuple Data Type](#tuple-data-type)
- [Copy](#copy)

In **Python Data Types Levels 1 and 2**, we introduced Python's core data types, their basic properties, and the collection types used to store multiple values. This level builds on that foundation by exploring how values are accessed and changed, how mutable and immutable objects behave, and how copying affects collections. We begin with indexing, slicing, dictionary keys, and membership before moving into nested structures and the behavior of individual collection types.

## Indexed sequence types

Python provides square bracket notation `[]` for accessing values in sequences and dictionaries. Lists, strings, and tuples use integer indices to identify positions, while dictionaries use keys rather than positional indices. For sequences, **positive indexing** counts from the beginning and **negative indexing** counts from the end. Square brackets are also used for **slicing**, which selects a range of values from an ordered sequence.

![indexing_slice_notation](../assets/images/indexing_slice_notation.png)

The main forms are indexing with `[n]`, slicing with `[start:stop]`, and extended slicing with `[start:stop:step]`. We will begin with positive and negative indexing for sequences and then compare this positional access with dictionary key access.

```py
items = [10, 20, 30, 40, 50] # List example
phrase = "Python" # String example
tup = (100, 200, 300, 400) # Tuple example

# Positive indexing (index 0)
print("List first element:", items[0]) # List first element: 10
print("String first character:", phrase[0]) # String first character: P
print("Tuple first element:", tup[0]) # Tuple first element: 100

# Negative indexing (last element)
print("List last element:", items[-1]) # List last element: 50
print("String last character:", phrase[-1]) # String last character: n
print("Tuple last element:", tup[-1]) # Tuple last element: 400

# Dictionary access by key
person = {"name": "Test", "age": 30}

print("Name value:", person["name"]) # Name value: Test
print("Age value:", person["age"]) # Age value: 30
```

Slicing extends indexing by selecting part of a sequence. Writing `[:]` or `[::]` selects the full sequence, while start and stop values limit the selected range. Extended slicing adds a step that controls the interval between selected elements.

```py
text = "Python" # String example
numbers = [10, 20, 30, 40, 50] # List example
tupl = (100, 200, 300, 400, 500) # Tuple example

# Entire sequence
print(text[:], numbers[:], tupl[:]) # Python [10, 20, 30, 40, 50] (100, 200, 300, 400, 500)
# Positive slicing (from index 1 to 3)
print(text[1:4], numbers[1:4], tupl[1:4]) # yth [20, 30, 40] (200, 300, 400)
# Negative slicing (using negative indices)
print(text[-4:-1], numbers[-4:-1], tupl[-4:-1]) # tho [20, 30, 40] (200, 300, 400)
# Extended slicing with step (every 2nd element)
print(text[::2], numbers[::2], tupl[::2]) # Pto [10, 30, 50] (100, 300, 500)
```

> **Note:** When you use a `step` with negative indices, such as `text[-4:-1:2]`, Python applies the step interval in the same way as it does with positive indices.

Slice boundaries may extend beyond the available indices without raising `IndexError`. If the requested range does not select any elements, Python returns an empty sequence. With a positive step, slicing moves from left to right, so a start position that comes after the stop position produces an empty result.

```py
text = "Python"
numbers = [10, 20, 30, 40, 50]

print(text[-5:3]) # 'Pyt'
print(text[-3:3]) # ''
print(numbers[-5:3]) # [10, 20, 30]
print(numbers[-3:3]) # []

result = numbers[3:1]
print(result) # []
```

This behavior differs from direct indexing. An expression such as `numbers[10]` raises `IndexError` when the requested position does not exist. A slice is more tolerant of out-of-range boundaries, although an extended slice with a step of `0` is invalid and raises `ValueError`.

Square brackets are used for access and slicing, but working with sequences also introduces an important distinction between **reassignment** and **in-place modification**. For example, using `+` with a list creates a new list, and assignment then makes the variable refer to that new object.

```py
items = [1, 2, 3]
items = items + [4, 5]

print(items) # [1, 2, 3, 4, 5]
```

The expression `items + [4, 5]` creates a new list, and the assignment rebinds `items` to that new object rather than modifying the original list in place. Strings and tuples also support concatenation, but because they are immutable, concatenation creates new objects that can then be assigned to variables.

> **Note:** The original list object is not modified by `+`. Instead, `items` is rebound to the newly created list. The similar-looking expression `items += [4, 5]` normally modifies a list in place, so the two forms can behave differently when other variables refer to the same list. The `+=` operator is explored in more detail in the Python operations material.

```py
text = "Hello"
text = text + " World"

print(text) # Hello World

tup = (1, 2, 3)
tup = tup + (4, 5)

print(tup) # (1, 2, 3, 4, 5)
```

Sets and dictionaries do not support concatenation with `+`.

```py
my_set = {1, 2, 3}
my_set = my_set + {4} # TypeError

my_dict = {"a": 1}
my_dict = my_dict + {"b": 2} # TypeError
```

Sets and dictionaries therefore require different ways to work with their contents. Before exploring those operations in their dedicated sections, it is important to distinguish between types that support square bracket access and types that do not.

## Non-indexed and Non-subscriptable Types

Square bracket notation does not work in the same way with every Python data type. **Sets** are non-indexed and do not support subscripting, so their elements cannot be accessed by position. Types such as `int`, `float`, `bool`, and `None` also do not support subscripting.

Dictionaries behave differently because a **dictionary is subscriptable**, but the value inside the square brackets is interpreted as a key rather than as a numeric position. An integer can therefore appear inside the brackets when that integer actually exists as a dictionary key.

```py
item_dict = {0: "zero"}

print(item_dict[0]) # zero
```

Trying to subscript a set raises `TypeError`. A dictionary supports subscripting, but requesting a key that does not exist raises `KeyError`.

```py
item_set = {1, 2, 3, 4, 5}

print(item_set[0]) # TypeError: 'set' object is not subscriptable

item_dict = {"a": 1, "b": 2}

print(item_dict["a"]) # 1
print(item_dict[0]) # KeyError: 0
```

The distinction is important. `item_set[0]` raises `TypeError` because a set cannot be subscripted at all. `item_dict["a"]` succeeds because `"a"` is an existing dictionary key, while `item_dict[0]` raises `KeyError` because the dictionary supports subscripting but does not contain the key `0`.

Programs often contain **nested structures**, where one collection stores another collection. Common examples include lists containing lists, dictionaries, sets, or tuples, as well as dictionaries containing lists or other dictionaries. In these structures, square brackets can be chained to move through each level of the data. Understanding which objects support square bracket access therefore prepares us for the next topic, where indexing and dictionary keys are combined to work with nested values.

## Nested access and assignment using square brackets

Square brackets `[]` access elements by index in sequences and by key in dictionaries. When structures are nested, the same notation can be chained so that each pair of square brackets moves one level deeper into the data.

A list can contain another list. Because lists are mutable, square bracket notation can be used both to access a nested value and to update it with assignment.

```py
numbers = [1, 2, [10, 20, 30]]

print(numbers[2]) # [10, 20, 30]
print(numbers[2][1]) # 20

numbers[2][1] = 99

print(numbers) # [1, 2, [10, 99, 30]]
```

The same idea applies when a dictionary contains a list. The first pair of square brackets selects the dictionary value by key, and the second pair selects an element from the nested list. Because that nested list is mutable, its selected value can also be changed.

```py
profile = {
    "username": "admin",
    "roles": ["editor", "moderator"]
}

print(profile["roles"][0]) # editor

profile["roles"][0] = "admin"

print(profile) # {'username': 'admin', 'roles': ['admin', 'moderator']}
```

A dictionary can also contain another dictionary. Chained keys move through each dictionary level, and assignment can update an existing value or add a new key value pair to the nested dictionary.

```py
config = {
    "database": {
        "host": "localhost",
        "port": 5432
    }
}

print(config["database"]["port"]) # 5432

config["database"]["port"] = 3306
config["database"]["user"] = "root"

print(config) # {'database': {'host': 'localhost', 'port': 3306, 'user': 'root'}}
```

A list can contain a set, but the set itself remains non-indexed. Square brackets can access the set through its position in the outer list, but they cannot select an individual element inside that set. Because the outer list is mutable, assignment can instead replace the entire set stored at that position.

```py
data = [
    {1, 2, 3},
    {4, 5, 6}
]

print(data[0]) # {1, 2, 3}

data[0][1] # TypeError

data[0] = {10, 20, 30}

print(data) # [{10, 20, 30}, {4, 5, 6}]
```

> **Note:** Sets do not guarantee display order, so the elements in the printed sets may appear in a different order.

A list containing a tuple behaves differently. Tuples are indexed, so their values can be accessed with square brackets, but tuples are immutable and their individual values cannot be replaced through assignment. The mutable outer list can still replace the entire tuple.

```py
data = [
    (10, 20, 30),
    (40, 50, 60)
]

print(data[0]) # (10, 20, 30)
print(data[0][1]) # 20

data[0][1] = 99 # TypeError

data[0] = (100, 200, 300)

print(data) # [(100, 200, 300), (40, 50, 60)]
```

Square brackets therefore provide a path through nested structures, but what can be changed depends on the object reached at the end of that path. A nested list or dictionary can be modified, a tuple cannot be modified internally, and a set cannot be indexed at all. These differences lead directly to the broader distinction between **mutable** and **immutable** objects.

## How mutable and immutable data types work

In **Python Data Types Level 1**, we introduced the difference between mutable and immutable data types. **Mutable data types** can be changed in place, while **immutable data types** cannot. When an operation appears to change an immutable value, Python creates a new object and the variable is reassigned to that object.

The built-in `id()` function helps us observe this behavior. It returns an integer that identifies a particular object during its lifetime. The actual number, such as `140245849646464`, is not important and may be different each time the program runs. What matters is whether the number stays the same or changes after an operation.

```py
my_list = [1, 2, 3]

print("Original list:", my_list) # Original list: [1, 2, 3]
print("Original id:", id(my_list)) # The ID will vary

my_list.append(4)

print("Modified list:", my_list) # Modified list: [1, 2, 3, 4]
print("Modified id:", id(my_list)) # Same ID as before
```

Because a list is **mutable**, `append()` changes the existing list in place. The contents change from `[1, 2, 3]` to `[1, 2, 3, 4]`, but both calls to `id(my_list)` return the same number during that run. This tells us that `my_list` still refers to the same list object.

Strings behave differently because they are **immutable**.

```py
text = "Hello"

print("Before:", text, id(text)) # Before: Hello <original ID>

text = text + " world"

print("After:", text, id(text)) # After: Hello world <different ID>
```

The two `id()` values are different because `"Hello world"` is a new string object. The original `"Hello"` string was not modified. Instead, `text` was reassigned so that it refers to the newly created string. The important distinction is therefore not whether a variable can be assigned another value, because variables can be reassigned in either case. The difference is whether the existing object itself can be modified.

This distinction becomes especially important when multiple variables refer to the same mutable object, which we will examine later when working with copies. With this foundation established, we can now examine the individual collection types in more detail, beginning with lists.

## List Data Type

In Python, a **list** is a **mutable**, ordered sequence of elements. Because lists are mutable, their contents can be changed in place by adding, removing, replacing, or reordering elements. Lists can store simple values such as numbers and strings, but they are also commonly used to store structured records such as dictionaries, nested lists, and other collections.

Different list methods are useful for different kinds of changes. `append()` adds one element to the end, `insert()` adds one element at a specific position, and `extend()` adds multiple elements. Similarly, `remove()`, `pop()`, and `clear()` remove elements in different ways depending on what the program needs to remove.

To add a single element to the **end** of a list, use `append(element)`. Use `append()` when one new item needs to be added and its exact position is not important beyond placing it after the existing elements.

```py
valid_users = []

user = {
    "name": "example1",
    "email": "example@example.com",
    "active": True
}

if user["email"] != "":
    valid_users.append(user)

print(valid_users) # [{'name': 'example1', 'email': 'example@example.com', 'active': True}]
```

In this example, one validated user is added to the end of `valid_users`. This approach is useful when a program receives or produces items one at a time, such as accepted form submissions, successful API results, processed files, or completed tasks.

If one element must be added at a **specific position**, use `insert(index, element)` instead of `append()`. Existing elements at that position and after it are shifted to the right.

```py
subjects = ["Math", "History", "Science"]

subjects.insert(1, "English")

print(subjects) # ['Math', 'English', 'History', 'Science']
```

The index `1` places `"English"` between `"Math"` and `"History"`. Use `insert()` when a new element needs to appear at a particular position rather than at the end of the list.

When several elements need to be added to an existing list, use `extend(iterable)`. Unlike `append()`, which adds its argument as one element, `extend()` takes the elements from another iterable and adds them individually to the end of the list.

```py
monday_logs = [
    {"event": "login"},
    {"event": "upload"}
]

tuesday_logs = [
    {"event": "download"},
    {"event": "logout"}
]

monday_logs.extend(tuesday_logs)

print(monday_logs) # [{'event': 'login'}, {'event': 'upload'}, {'event': 'download'}, {'event': 'logout'}]
```

Here, both records from `tuesday_logs` are added individually to `monday_logs`. Use `extend()` rather than `append()` when the goal is to combine the elements of two collections into one list. For example, it can combine records loaded from several files, results from different data sources, or logs collected on different days.

Once elements have been added, they may also need to be removed. The appropriate method depends on what the program knows about the element. Use `remove()` when its value is known, `pop()` when its position is known and the removed value is needed, and `clear()` when every element should be removed.

The `remove(value)` method deletes the **first element equal to the specified value**.

```py
active_features = [
    "search",
    "notifications",
    "dark_mode"
]

active_features.remove("notifications")

print(active_features) # ['search', 'dark_mode']
```

In this example, the program knows the value `"notifications"` but does not need to know its index. This makes `remove()` useful when deleting a known name, option, tag, or other value from a list.

> **Note:** If the specified value does not exist in the list, `remove()` raises `ValueError`.

Use `pop(index)` when the program knows the **position** of an element and also needs the value that was removed. Unlike `remove()`, `pop()` returns the removed element, allowing it to be stored in a variable and used afterward.

```py
tasks = [
    {"task": "download file"},
    {"task": "parse data"},
    {"task": "save results"}
]

current_task = tasks.pop(0)

print("Current task:", current_task["task"]) # Current task: download file
print("Remaining tasks:", tasks) # [{'task': 'parse data'}, {'task': 'save results'}]
```

Here, `pop(0)` removes the first task from the list and returns that dictionary. The returned dictionary is stored in `current_task`, so the program can work with the task after removing it from the list. Use `pop()` when an item should be taken out of a list and then used, such as taking the next task from a small task list or retrieving the most recent item from a history.

> **Note:** Using `pop(0)` works for small lists, but it becomes inefficient for large queues because all remaining elements must shift to new positions. For programs that require efficient queue operations, Python provides `collections.deque`.

If no index is supplied, `pop()` removes and returns the **last element**. This is useful when the program needs the most recently added element.

```py
history = [
    "open file",
    "edit title",
    "save file"
]

last_action = history.pop()

print("Last action:", last_action) # Last action: save file
print("Remaining history:", history) # ['open file', 'edit title']
```

Here, `"save file"` is both removed from `history` and stored in `last_action`. This behavior is useful for last-in, first-out operations, where the most recently added item is handled first.

To remove **all elements** while keeping the same list object, use `clear()`. Use this method when the contents are no longer needed but the list itself will continue to be used.

```py
pending_logs = [
    {"event": "login"},
    {"event": "profile_update"}
]

print("Sending:", pending_logs) # Sending: [{'event': 'login'}, {'event': 'profile_update'}]

pending_logs.clear()

print("Pending logs:", pending_logs) # []
```

In this example, the collected logs have already been handled, so `clear()` empties the list before it is used to collect another batch. Unlike removing elements individually, `clear()` removes the entire contents of the list in one operation.

After adding and removing elements, another common operation is changing their order. The `sort()` method rearranges the existing list in place. By default, comparable values are arranged in **ascending order**.

The result depends on the type of values being sorted. Numbers are ordered numerically, while strings are compared character by character according to their Unicode values. This means uppercase and lowercase letters can appear in different parts of the result, and strings containing digits are ordered as text rather than as numbers.

```py
scores = [85, 40, 92, 70, 60]
scores.sort()
print(scores) # [40, 60, 70, 85, 92]

names = ["example", "Example", "banana", "Apple"]
names.sort()
print(names) # ['Apple', 'Example', 'banana', 'example']

numbers_as_text = ["1", "2", "10", "11", "3"]
numbers_as_text.sort()
print(numbers_as_text) # ['1', '10', '11', '2', '3']
```

The numeric list is arranged from lowest to highest. With strings, uppercase `"Apple"` and `"Example"` appear before the lowercase values because uppercase and lowercase characters have different Unicode values. The values in `numbers_as_text` are also strings, so Python compares them character by character rather than numerically. This is why `"10"` and `"11"` appear before `"2"`. Their first character is `"1"`, which comes before `"2"`. If the same values were integers, `10` and `11` would be placed after `2` because integers are compared numerically.

Use `sort()` when the existing list should remain in sorted order. The method modifies the list in place and returns `None` rather than returning a new sorted list, so `new_scores = scores.sort()` assigns `None` to `new_scores`. The optional `reverse` and `key` parameters provide additional control over how the list is ordered.

Use `reverse=True` when the values should be arranged in **descending order** instead of the default ascending order. For example, an application may display available report years from the most recent to the oldest.

```py
report_years = [2022, 2025, 2021, 2024, 2023]

report_years.sort(reverse=True)

print(report_years) # [2025, 2024, 2023, 2022, 2021]
```

The `key` parameter is useful when each list element contains several values and one particular value should determine the order. For example, these dictionaries can be ordered by their `"score"` values.

```py
results = [
    {"user": "Example1", "score": 78},
    {"user": "Example2", "score": 92},
    {"user": "Example3", "score": 85}
]

def score_value(record):
    return record["score"]

results.sort(key=score_value)

for result in results:
    print(result["user"], result["score"]) # Prints Example1 78, Example3 85, then Example2 92
```

The `score_value()` function returns the `"score"` from each dictionary, so `sort()` uses that value for comparison and arranges the records from the lowest score to the highest. The same `key` and `reverse` parameters can be used together when the selected value should be ordered in the opposite direction.

```py
results.sort(key=score_value, reverse=True)

for result in results:
    print(result["user"], result["score"]) # Prints Example2 92, Example3 85, then Example1 78
```

Here, `key=score_value` still selects the score for comparison, while `reverse=True` changes the direction so that the highest score appears first. This completes the basic use of `key` with the `sort()` method. Passing functions as arguments is explored more deeply in **Functions Level 3**, including when working with the built-in `sorted()` function.

Sorting arranges elements according to their values or a selected comparison value. Reversing is different because it simply flips the order that already exists. The `reverse()` method changes the existing list in place, while `[::-1]` creates a new reversed list.

```py
processing_queue = ["job_1", "job_2", "job_3", "job_4"]

processing_queue.reverse()

print(processing_queue) # ['job_4', 'job_3', 'job_2', 'job_1']

original_queue = ["job_1", "job_2", "job_3", "job_4"]

reversed_queue = original_queue[::-1]

print(original_queue) # ['job_1', 'job_2', 'job_3', 'job_4']
print(reversed_queue) # ['job_4', 'job_3', 'job_2', 'job_1']
```

Use `reverse()` when the existing list itself should be reversed. Use `[::-1]` when the original order should remain unchanged and a separate reversed list is needed.

Lists are useful when elements are organized and accessed by **position**, but structured data often needs values to be identified by names or labels instead of numeric indices. Dictionaries provide this key-based organization, which builds on the collection concepts introduced with lists.

## Dictionary Data Type

Next, let’s explore another important data type in Python, `dict`, also known as a **mapping type**. A dictionary is a **mutable mapping type** that stores data as **key-value pairs** and uses keys rather than numeric indexes to identify values. Dictionaries often contain lists, other dictionaries, and mixed data types, which makes them useful for representing structured information.

Dictionary values can be accessed directly with square brackets when a key is expected to exist. When a key may be missing, `get()` provides an alternative because it can return `None` or a supplied default value instead of raising a `KeyError`. Consider an application configuration object.

```py
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "user": "admin",
            "password": "secret"
        }
    },
    "features": {
        "logging": True,
        "debug": False
    }
}
```

The `"database"` value can be retrieved with `get()`. This is the basic form of the method and returns the value stored under the requested key.

```py
db_config = config.get("database")
print(db_config) # {'host': 'localhost', 'port': 5432, 'credentials': {'user': 'admin', 'password': 'secret'}}
```

When the required value is deeper inside nested dictionaries, `get()` can be chained.

```py
db_port = config.get("database", {}).get("port")
print(db_port) # 5432
```

The first `get()` retrieves `"database"`. If that key is missing, the default `{}` supplies an empty dictionary, so `get("port")` can still be called without raising a `KeyError`. The same approach can handle an optional nested key that may not exist, either by returning `None` or by using a supplied fallback value.

```py
timeout = config.get("database", {}).get("timeout")
print(timeout) # None

timeout = config.get("database", {}).get("timeout", 30)
print(timeout) # 30
```

Because `"timeout"` is missing, the first call returns `None`, while the second returns the supplied default value `30`. Use a default when the program has a suitable fallback for an optional value.

Sometimes the program needs to know whether a key exists rather than retrieve a fallback value. In that situation, use the `in` operator.

```py
if "database" in config:
    print(config["database"]) # {'host': 'localhost', 'port': 5432, 'credentials': {'user': 'admin', 'password': 'secret'}}
```

Use `in` when the existence of the key affects the next action. Once the check succeeds, direct square bracket access can be used safely for that key. Use `get()` instead when the program mainly needs a value and can continue with `None` or another default if the key is absent.

```py
users = {
    "admins": [
        {"name": "Example1", "active": True},
        {"name": "Example2", "active": False}
    ],
    "editors": [
        {"name": "Example3", "active": True}
    ]
}
```

The list stored under `"admins"` can be retrieved and indexed to access its first record. Access can then continue into that record to retrieve a specific value.

```py
first_admin = users.get("admins", [])[0]
print(first_admin) # {'name': 'Example1', 'active': True}

admin_name = users.get("admins", [])[0].get("name")
print(admin_name) # Example1
```

In both expressions, `get("admins", [])` retrieves the list and `[0]` selects its first dictionary. The second expression continues into that dictionary with `get("name")` to retrieve the name.

> **Note:** The default empty list prevents a `KeyError` when `"admins"` is missing, but `[0]` still raises an `IndexError` if the list is empty. When the list may be empty, check it before accessing the first element.

Direct square bracket access behaves differently when a dictionary key does not exist. Instead of returning a default value, it raises a `KeyError`.

```py
print(users["moderators"][0]["name"]) # KeyError
```

When the key or its list may be missing, retrieve the list with `get()` and check that it contains an element before accessing `[0]`.

```py
moderators = users.get("moderators", [])

if moderators:
    print(moderators[0].get("name"))
else:
    print("No moderators found") # No moderators found
```

This handles both a missing `"moderators"` key and an empty moderators list without attempting to access an unavailable element.

Because dictionaries are mutable, key-value pairs can be added or changed after the dictionary is created. When one specific entry needs to be added or changed, direct key assignment is the simplest approach.

```py
config["database"]["timeout"] = 30
print(config["database"]) # {'host': 'localhost', 'port': 5432, 'credentials': {'user': 'admin', 'password': 'secret'}, 'timeout': 30}
```

Because `"timeout"` does not already exist, the assignment adds it to the nested `"database"` dictionary. If the key already existed, the same syntax would replace its current value. Use direct assignment for one specific entry. When several entries need to be applied together, use `update()`.

The `update()` method applies one or more key-value pairs to an existing dictionary. Existing keys receive new values, while missing keys are added. This makes the method useful both for changing existing entries and adding new ones, especially when several related values need to be applied together.

```py
config = {
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "features": {
        "logging": True
    }
}
```

The same `update()` method can change an existing key, add a missing key, or apply several key-value pairs at once.

```py
# Change an existing key
config["database"].update({"port": 3306})
print(config) # {'database': {'host': 'localhost', 'port': 3306}, 'features': {'logging': True}}

# Add a missing key
config["database"].update({"timeout": 30})
print(config) # {'database': {'host': 'localhost', 'port': 3306, 'timeout': 30}, 'features': {'logging': True}}

# Change several related values
config["database"].update({
    "host": "db.internal",
    "port": 5432
})
print(config) # {'database': {'host': 'db.internal', 'port': 5432, 'timeout': 30}, 'features': {'logging': True}}
```

In the first operation, `"port"` already exists, so its value changes from `5432` to `3306`. In the second, `"timeout"` does not exist, so it is added as a new key-value pair. The final operation changes `"host"` and `"port"` together, showing why `update()` is more convenient than separate assignments when several entries need to be applied at once.

`update()` can also modify a dictionary stored inside another collection. In the following list, `users[1]` selects the second user dictionary before `update()` changes its `"active"` value.

```py
users = [
    {"id": 1, "name": "Example1", "active": True},
    {"id": 2, "name": "Example2", "active": False}
]

users[1].update({"active": True})
print(users) # [{'id': 1, 'name': 'Example1', 'active': True}, {'id': 2, 'name': 'Example2', 'active': True}]
```

Only the `"active"` value in that record changes, while its other fields remain unchanged.

`update()` can also apply the contents of another dictionary to an existing record.

```py
user_profile = {
    "id": 3,
    "name": "Charlie"
}
extra_data = {
    "email": "charlie@example.com",
    "role": "editor"
}
user_profile.update(extra_data)
print(user_profile) # {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com', 'role': 'editor'}
```

The keys from `extra_data` are added to `user_profile`. If both dictionaries contained the same key, the value from `extra_data` would replace the existing value. Use this form when a collection of key-value pairs from another dictionary should be applied to an existing record.

The replacement behavior can also be used deliberately when one dictionary should override selected values from another.

```py
settings = {
    "theme": "light",
    "language": "en"
}
override = {
    "theme": "dark"
}
settings.update(override)
print(settings) # {'theme': 'dark', 'language': 'en'}
```

Both dictionaries contain `"theme"`, so `"dark"` replaces `"light"`. The `"language"` value remains unchanged because `override` does not contain that key.

Another useful dictionary method is `setdefault(key, default)`. It returns the existing value when the key is already present. If the key is missing, it creates the key with the supplied default value and returns that value. This makes `setdefault()` useful for building grouped or nested data without replacing values that were already stored.

Imagine processing events and grouping their actions by user. The goal is to create a dictionary in which each user is associated with a list of actions.

```py
events = [
    {"user": "Example1", "action": "login"},
    {"user": "Example2", "action": "login"},
    {"user": "Example1", "action": "upload"},
    {"user": "Example2", "action": "logout"},
]

activity_log = {}

for event in events:
    user = event["user"]
    action = event["action"]
    activity_log.setdefault(user, []).append(action)

print(activity_log) # {'Example1': ['login', 'upload'], 'Example2': ['login', 'logout']}
```

If the `user` key does not exist, `setdefault()` creates it with an empty list `[]`. If the key already exists, it returns the existing list. In both cases, `append()` adds the action to that list. Using `update()` here would behave differently because it can replace an existing value.

```py
activity_log.update({"Example1": []})
```

If `"Example1"` already contains actions, this call replaces that list with a new empty list. `setdefault()` avoids that replacement by preserving an existing value.

The same behavior is useful when a nested section should be created only if it is missing.

```py
config = {
    "features": {
        "auth": True
    }
}

logging_config = config.setdefault("logging", {})
logging_config.setdefault("level", "INFO")
logging_config.setdefault("format", "json")

print(config) # {'features': {'auth': True}, 'logging': {'level': 'INFO', 'format': 'json'}}
```

If `"logging"` is missing, the first `setdefault()` creates an empty dictionary for it. The following calls add `"level"` and `"format"` only when those keys are missing, so existing configuration values are preserved.

`setdefault()` can also collect several values under each category.

```py
results = [
    {"category": "math", "score": 80},
    {"category": "science", "score": 90},
    {"category": "math", "score": 85}
]

scores_by_category = {}

for result in results:
    scores_by_category.setdefault(result["category"], []).append(result["score"])

print(scores_by_category) # {'math': [80, 85], 'science': [90]}
```

For the first `"math"` result, `setdefault()` creates an empty list and `80` is appended. When `"math"` appears again, the existing list is returned and `85` is appended to it. This collects several values under the same category without overwriting earlier values.

Dictionaries also provide `keys()`, `values()`, and `items()` for working with their stored data. `keys()` provides the keys, `values()` provides the values, and `items()` provides each key together with its value.

```py
user_profile = {
    "id": 3,
    "name": "Charlie",
    "role": "editor"
}

print(user_profile.keys()) # dict_keys(['id', 'name', 'role'])
print(user_profile.values()) # dict_values([3, 'Charlie', 'editor'])
print(user_profile.items()) # dict_items([('id', 3), ('name', 'Charlie'), ('role', 'editor')])

for key, value in user_profile.items():
    print(key, value) # id 3, then name Charlie, then role editor
```

Choose the method according to what the program needs. When only the keys are needed, use `keys()`. When only the stored values are needed, use `values()`. When both are needed, `items()` provides each key together with its corresponding value, which is especially useful during iteration.

> **Note:** `keys()`, `values()`, and `items()` return dictionary view objects rather than lists. These views reflect later changes made to the dictionary.

After adding and updating entries, dictionaries also provide several ways to remove them. Use `del` when a known key should simply be removed, `pop()` when the removed value is also needed, `popitem()` when the most recently added pair should be removed, and `clear()` when every entry should be removed.

The `del` keyword is a Python statement rather than a dictionary method. Use it when a known key should be removed and the removed value is not needed afterward.

```py
user_profile = {
    "id": 101,
    "name": "Example1",
    "email": "Example1@example.com",
    "session": {
        "token": "abc123",
        "expires": "2026-01-01"
    }
}

del user_profile["session"] # Remove session data after logout

print(user_profile) # {'id': 101, 'name': 'Example1', 'email': 'Example1@example.com'}
```

Here, the user record remains while only the `"session"` entry is removed. This is commonly used when temporary or sensitive data is no longer needed, such as session information after logout.

> **Note:** If the key does not exist, `del` raises a `KeyError`.

Unlike `del`, the `pop()` method removes a key and returns its value. Use `pop()` when the value should still be available after the entry is removed.

```py
cache = {
    "page:/home": "<html>...</html>",
    "page:/about": "<html>...</html>"
}

expired_page = cache.pop("page:/home")

print("Expired cache entry:", expired_page) # Expired cache entry: <html>...</html>
print("Remaining cache:", cache) # {'page:/about': '<html>...</html>'}
```

The removed value is returned, so the program can still process it. This is commonly used when removed data must still be processed, such as during cache invalidation or task consumption.

When the key may not exist, a default value can be supplied to `pop()`.

```py
settings = {
    "theme": "dark",
    "language": "en"
}
timezone = settings.pop("timezone", "UTC")

print("Timezone:", timezone) # Timezone: UTC
print(settings) # {'theme': 'dark', 'language': 'en'}
```

Because `"timezone"` is missing, no entry is removed and `"UTC"` is returned. This eliminates the need for extra `if key in dict` checks when a fallback value is sufficient.

`popitem()` removes and returns the **most recently added** key-value pair. Unlike `pop()`, it does not require a specific key.

```py
request_context = {
    "request_id": "req-001",
    "user": "Example1",
    "debug": True
}
last_entry = request_context.popitem()

print("Removed:", last_entry) # Removed: ('debug', True)
print(request_context) # {'request_id': 'req-001', 'user': 'Example1'}
```

This is useful when dictionaries act as stacks or temporary stores, or when **reverse-order processing** is required.

> **Note:** Calling `popitem()` on an **empty dictionary** raises a `KeyError`.

The `clear()` method removes every key-value pair while keeping the dictionary object itself. Use it when all current contents are no longer needed but the same dictionary will continue to be used.

```py
session_data = {
    "user_id": 42,
    "cart": ["item1", "item2"],
    "auth_token": "xyz789"
}

session_data.clear() # Reset session after logout
print(session_data) # {}
```

After `clear()`, `session_data` becomes `{}` while the dictionary object itself remains available for reuse. This makes `clear()` appropriate when all existing entries should be removed at once without replacing the dictionary itself.

Dictionaries organize values through keys, allowing structured data to be read and changed by meaningful identifiers rather than numeric positions. Sets organize collections differently by focusing on unique values instead of key-value relationships, which is the next data type we will examine.

## Set Data Type

A set is a **non-indexed collection of unique elements**. Unlike lists and tuples, sets do not allow duplicate values. Sets are also **mutable**, so elements can be added or removed after the set has been created. Because sets do not provide positional access, they are especially useful when the important questions are whether a value exists and whether each value appears only once.

Consider a dataset of user actions in which the same user may appear several times. A set can collect the active users without requiring a separate duplicate check.

```py
events = [
    {"user": "example1", "action": "login"},
    {"user": "example2", "action": "login"},
    {"user": "example1", "action": "upload"},
    {"user": "example3", "action": "login"},
    {"user": "example2", "action": "logout"}
]

active_users = set()

for event in events:
    active_users.add(event["user"])

print(active_users) # {'example1', 'example2', 'example3'}
```

Although some users appear more than once, the set keeps only unique values. This pattern is useful when processing logs, events, or audit data because there is no need to manually check whether a user has already been added.

> **Note:** Sets do not guarantee display order. The same elements may appear in a different order when a set is printed.

Sets can also be stored inside other collections when values within each group must remain unique. For example, a dictionary can associate each role with a set of permissions.

```py
permissions = {
    "admin": {"read", "write", "delete"},
    "editor": {"read", "write"},
    "viewer": {"read"}
}

permissions["editor"].add("publish")
permissions["editor"].add("write") # Duplicate value, ignored

print(permissions["editor"]) # {'read', 'write', 'publish'}
```

Each dictionary value is a set because permissions should be unique. Adding `"publish"` creates a new element, while adding `"write"` again does not create a duplicate. This is useful in access control and role based authorization systems.

Sets are also frequently used inside lists of records. When a record contains repeated values, converting that collection to a set removes the duplicates while leaving the surrounding structure intact.

```py
users = [
    {"name": "example1", "actions": ["login", "upload", "login"]},
    {"name": "example2", "actions": ["login", "logout", "login"]}
]

for user in users:
    user["actions"] = set(user["actions"])

print(users) # [{'name': 'example1', 'actions': {'login', 'upload'}}, {'name': 'example2', 'actions': {'login', 'logout'}}]
```

Each user record remains a dictionary, but its `"actions"` value becomes a set of unique actions. This pattern appears in analytics, activity tracking, and event aggregation systems.

The `add()` method adds **one element** to a set. Choose it when values arrive individually, such as new sessions, processed IDs, or completed tasks.

```py
processed_ids = set()

incoming_batches = [
    [101, 102, 103],
    [102, 104],
    [105, 101]
]

for batch in incoming_batches:
    for record_id in batch:
        processed_ids.add(record_id)

print(processed_ids) # {101, 102, 103, 104, 105}
```

Even though the same IDs appear in multiple batches, each ID occurs only once in `processed_ids`.

When several elements should be added from an iterable, use `update()` instead. Unlike `add()`, which adds one element, `update()` can take a list, tuple, set, or another iterable and add all of its elements to the set at once.

```py
processed_ids = {101, 102}
new_batch = [102, 103, 104]

processed_ids.update(new_batch)

print(processed_ids) # {101, 102, 103, 104}
```

Here, `102` already exists, while `103` and `104` are added. `update()` modifies `processed_ids` **in place**, so the same set object remains in use while its contents change. This makes the method useful for batch data, API responses, and file imports.

The iterable supplied to `update()` can also come from a nested structure. In the following example, each dictionary value contains a batch of event IDs.

```py
event_batches = {
    "sensor_1": [201, 202, 203],
    "sensor_2": [202, 204],
    "sensor_3": [205, 201]
}

all_event_ids = set()

for batch in event_batches.values():
    all_event_ids.update(batch)

print(all_event_ids) # {201, 202, 203, 204, 205}
```

Each batch is added to the same set, and repeated IDs are automatically ignored.

Sets stored inside dictionaries can be updated in the same way when several values belong to a particular category.

```py
active_sessions = {
    "us-east": {"sess_1", "sess_2"},
    "eu-west": {"sess_3"}
}

new_sessions = ["sess_2", "sess_4", "sess_5"]

active_sessions["us-east"].update(new_sessions)

print(active_sessions["us-east"]) # {'sess_1', 'sess_2', 'sess_4', 'sess_5'}
```

The `"us-east"` set receives all values from `new_sessions`, while the duplicate `"sess_2"` remains a single element. This is useful for grouped data such as regional or sharded system state.

`update()` can also combine the contents of two sets. Because it is a mutating method, it changes the set on which it is called.

```py
validated_ids = {1, 2, 3}
processed_ids = {3, 4, 5}

validated_ids.update(processed_ids)
print(validated_ids) # {1, 2, 3, 4, 5}
```

`update()` modifies `validated_ids` in place, adding all elements from `processed_ids`. The set object remains the same, but its contents change. When the original sets should remain unchanged, use `union()` to create a new set instead.

```py
validated_ids = {1, 2, 3}
processed_ids = {3, 4, 5}

combined_ids = validated_ids.union(processed_ids)

print(combined_ids) # {1, 2, 3, 4, 5}
print(validated_ids) # {1, 2, 3}
```

`combined_ids` contains the unique elements from both sets, while `validated_ids` is unchanged. Choose `update()` when the existing set should change and `union()` when a separate combined set is needed.

Sets are often **populated** from lists of dictionaries rather than from simple values. A generator expression can select the required field while `update()` collects the unique values.

```py
records = [
    {"id": 301, "status": "ok"},
    {"id": 302, "status": "ok"},
    {"id": 301, "status": "retry"}
]

unique_ids = set()
unique_ids.update(record["id"] for record in records)

print(unique_ids) # {301, 302}
```

Only the record IDs are added, and the repeated `301` appears once. This is useful in data cleanup and report generation.

Because sets are designed around unique values, membership testing with `in` is one of their most common operations. Use it when the program needs to know whether a particular value is present.

```py
active_sessions = {"sess_101", "sess_102", "sess_103"}

if "sess_102" in active_sessions:
    print("Session is active") # Session is active
```

The expression checks membership directly without requiring positional access or a loop.

Sets also provide several ways to remove elements. Use `remove()` when a specific element is expected to exist, `discard()` when it may already be absent, `pop()` when any one element can be removed and returned, and `clear()` when every element should be removed.

The `remove(element)` method deletes a specific element. If the element does not exist, Python raises a `KeyError`, so choose this method when absence should be treated as an error.

```py
active_sessions = {"sess_101", "sess_102", "sess_103"}

active_sessions.remove("sess_102") # A user logs out

print(active_sessions) # {'sess_101', 'sess_103'}

active_sessions.remove("sess_999") # KeyError
```

The first removal is appropriate because `"sess_102"` is expected to exist. The second call demonstrates the `KeyError` raised for a missing element.

The same behavior is useful when sets are nested inside dictionaries and a required value should be present.

```py
user_permissions = {
    "admin": {"read", "write", "delete"},
    "editor": {"read", "write"},
    "viewer": {"read"}
}

user_permissions["editor"].remove("write")
print(user_permissions["editor"]) # {'read'}
```

The permission is expected to exist. Attempting to remove a missing permission would indicate corrupted data, which is useful to detect in authorization systems.

When a missing element should not be treated as an error, use `discard(element)`. It removes the element if it exists and does nothing if it is already absent.

```py
pending_jobs = {"job_1", "job_2", "job_3"}

pending_jobs.discard("job_2") # A job completes

print(pending_jobs) # {'job_1', 'job_3'}
```

This is useful when data may have expired or when an element might already be gone.

The `pop()` method removes and returns an **arbitrary element** from a set. Because sets are non-indexed, the program should not depend on which element is selected.

```py
pending_jobs = {"job_101", "job_102", "job_103"}

current_job = pending_jobs.pop()

print("Processing:", current_job) # One arbitrary job ID
print("Remaining jobs:", pending_jobs) # The other two job IDs
```

Here, one job is removed and its ID is returned. This is useful in task schedulers when any pending job can be processed next.

> **Note:** The exact value returned by `set.pop()` should not be shown as a fixed expected result because sets do not provide positional order. The important result is that one element is removed and returned.

`pop()` can also operate on a set stored inside another collection.

```py
server_connections = {
    "server_a": {"conn_1", "conn_2"},
    "server_b": {"conn_3"}
}

closed_conn = server_connections["server_a"].pop()

print("Closed connection:", closed_conn) # Either conn_1 or conn_2
print(server_connections) # server_a now contains one of its original connections
```

One connection is removed from the `"server_a"` set and returned. If a set is empty, however, `pop()` raises a `KeyError`, so check the set first when it may contain no elements.

```py
empty_set = set()
empty_set.pop() # KeyError

if pending_jobs:
    job = pending_jobs.pop()
```

The `clear()` method removes all elements while keeping the set object itself. Use it when the current contents should be discarded but the same set will continue to be used.

```py
active_users = {"user_1", "user_2", "user_3"}

active_users.clear() # System shutdown or reset

print(active_users) # set()
```

After `clear()`, `active_users` is empty but still refers to the same set object. This is useful when reusing containers or clearing stored state between phases.

Sets also support operations that compare or combine their contents without modifying the original sets. The `intersection()` method returns a new set containing only values that appear in both sets.

```py
user_permissions = {"read", "write", "delete"}
required_permissions = {"read", "execute"}

allowed = user_permissions.intersection(required_permissions)
print(allowed) # {'read'}
```

The result contains the shared permission `"read"`, while both original sets remain unchanged. This is useful when identifying values shared by two collections.

When the program needs to check whether **all** required values are available rather than only find the shared ones, `issubset()` provides a direct test.

```py
user_permissions = {"read", "write", "delete"}
required_permissions = {"read", "write"}

if required_permissions.issubset(user_permissions):
    print("All required permissions are available") # All required permissions are available
```

Here, every element in `required_permissions` exists in `user_permissions`, so `issubset()` returns `True`. This is useful for permission and capability checks.

The `difference()` method returns a new set containing values that exist in one set but not the other.

```py
expected_files = {"a.txt", "b.txt", "c.txt"}
uploaded_files = {"a.txt", "c.txt"}

missing_files = expected_files.difference(uploaded_files)
print(missing_files) # {'b.txt'}
```

`missing_files` contains `"b.txt"` because it is expected but was not uploaded. This is common during upload validation, and the original sets remain unchanged.

Sets focus on unique values and do not provide positional indexing. Strings serve a different purpose by representing ordered textual data, so we now move from unique collections to working with text.

## Strings Data Type

A **string** is an **immutable sequence of Unicode characters**. Because strings are ordered, individual characters can be accessed with indexing and slicing. Because strings are immutable, however, their characters cannot be changed in place.

Strings are used everywhere: user input, messages, file names, configuration values, and API responses. Many string methods therefore focus on normalizing, splitting, searching, validating, and transforming text while returning new strings rather than modifying the original object.

One common operation is normalizing text with `upper()` and `lower()`. Normalization converts text into a consistent form before it is compared or stored, which is useful when user input may use different capitalization.

```py
user_input = "Admin"

if user_input == "admin" or user_input == "Admin":
    pass

if user_input.lower() == "admin":
    print("Admin access granted") # Admin access granted
```

Instead of checking several capitalization variations, the second condition converts the input to lowercase before comparing it. This appears in role checks and form validation.

The same approach can normalize several values before they are stored or processed.

```py
raw_usernames = ["Example", "example", "EXAMPLE", "ExamplE"]

normalized = []

for name in raw_usernames:
    normalized.append(name.lower())

print(normalized) # ["example", "example", "example", "example"]
```

This is commonly done before storing values in databases when capitalization should not create inconsistent records. Lowercase is often useful for program logic, while uppercase can be useful for display output such as logs and alerts.

```py
status = "error"

print(status.upper()) # ERROR
```

Calling `upper()` or `lower()` does not change the original string because strings are immutable. The returned value must be assigned if the transformed text should be kept.

```py
text = "Hello"

text.upper()
print(text) # Hello

text = text.upper()
print(text) # HELLO
```

The first call creates an uppercase string but does not assign it, so `text` remains `"Hello"`. The second call assigns the returned string back to `text`, so the variable then refers to `"HELLO"`.

Strings often appear inside lists and dictionaries, where their values can be normalized before being used.

```py
users = [
    {"name": "Example1", "role": "Admin"},
    {"name": "example2", "role": "editor"},
    {"name": "EXAMPLE3", "role": "VIEWER"}
]

for user in users:
    role = user["role"].lower()
    if role == "admin":
        print("Admin user:", user["name"]) # Admin user: Example1
```

Here, each role is converted to lowercase before comparison, so the check does not depend on how the role was originally capitalized.

Because strings are ordered sequences, indexing and slicing can select particular characters or sections of text.

```py
filename = "report_2026.pdf"

extension = filename[-3:]
print(extension) # pdf

country_code = "+370-612-34567"

print(country_code[:4]) # +370
```

The first slice retrieves the final three characters for an extension check, while the second retrieves the first four characters of the phone number. String slicing also supports a step, just like other indexed sequences.

```py
text = "Python"

reversed_text = text[::-1]
print(reversed_text) # nohtyP
```

A step of `-1` reads the string from the end toward the beginning and creates a new reversed string. The original string remains unchanged.

Strings frequently contain several pieces of data that must be separated before they can be processed. By default, `split()` separates text at whitespace such as spaces, tabs, and newlines.

```py
command = "deploy production --force"

parts = command.split()
print(parts) # ['deploy', 'production', '--force']

action = parts[0]
environment = parts[1]

print(action, environment) # deploy production
```

After the command is split, each part can be processed independently. This pattern is common in command line tools.

When values are separated by a specific character such as a comma, colon, or pipe (`|`), pass that separator to `split()`.

```py
row = "101,example,admin,active"

fields = row.split(",")
print(fields) # ['101', 'example', 'admin', 'active']
```

This allows you to map values into a structured record.

```py
user = {
    "id": int(fields[0]),
    "name": fields[1],
    "role": fields[2],
    "status": fields[3]
}

print(user) # {'id': 101, 'name': 'example', 'role': 'admin', 'status': 'active'}
```

The comma separated string becomes a list whose values can be used to build a structured record. This pattern appears in CSV style input and exported reports.

A similar approach can separate a key from its value.

```py
setting = "timeout=30"

key, value = setting.split("=")
print(key, value) # timeout 30
```

This frequently appears when processing configuration values, environment style settings, or URL query data.

The natural counterpart to `split()` is `join()`. While `split()` breaks one string into separate strings, `join()` combines an iterable of strings using a chosen separator.

```py
fields = ["101", "example", "admin", "active"]

row = ",".join(fields)

print(row) # 101,example,admin,active
```

Here, the comma string acts as the separator placed between each element in `fields`. Use `join()` when separate strings need to be assembled into one string.

When working with multiline text, `splitlines()` separates the text into lines and handles different line endings more reliably than manually splitting only on `"\n"`.

```py
log_data = """INFO Server started
WARNING Low memory
ERROR Disk full"""

lines = log_data.splitlines()

for line in lines:
    print("Log entry:", line) # Prints each log line with the "Log entry:" prefix
```

This is useful when reading and processing text files, logs, and other multiline content.

Programs also frequently need to check how a string starts or ends rather than compare the entire value. The `startswith()` and `endswith()` methods provide direct checks for this purpose and are useful for file validation, URL handling, log parsing, and input filtering.

```py
filename = "report_2026.pdf"

if filename.endswith(".pdf"):
    print("Valid PDF file") # Valid PDF file
else:
    print("Invalid file type")

log_line = "ERROR Disk full"

if log_line.startswith("ERROR"):
    print("Critical issue detected") # Critical issue detected
```

The first check validates the file extension, while the second identifies a log entry by its severity prefix.

`startswith()` can also begin checking from a specified position.

```py
path = "/api/v1/users"

if path.startswith("v1", 5):
    print("Version 1 API request") # Version 1 API request
```

Starting at index `5` allows the program to check the version portion of the path without creating a separate slice.

Ending checks are also useful when a suffix identifies a particular category or format.

```py
email = "user@example.com"

if email.endswith("@example.com"):
    print("Internal company email") # Internal company email
```

When part of a string needs to be replaced, use `replace(old, new[, count])`. The `old` argument is the substring to replace, `new` is the replacement text, and the optional `count` argument limits the maximum number of replacements.

```py
message = "User password is secret123"

safe_message = message.replace("secret123", "***")
print(safe_message) # User password is ***
```

This type of replacement can be useful when preparing text for logs or other output where a particular value should not appear in plain form.

The optional `count` argument can limit how many matching occurrences are replaced.

```py
text = "ERROR: Disk error detected"

fixed = text.replace("error", "issue", 1)
print(fixed) # ERROR: Disk issue detected
```

Only the first matching lowercase `"error"` is replaced. The uppercase `"ERROR"` does not match because string replacement is case sensitive.

User input and external data often contain unwanted whitespace, including spaces, tabs, and newline characters. Python provides the `strip()` method to remove whitespace from both ends of a string.

```py
raw_input = "   admin   "

if raw_input == "admin":
    print("Access granted") # Not printed because the spaces remain

cleaned = raw_input.strip()

if cleaned == "admin":
    print("Access granted") # Access granted
```

The first comparison fails because `raw_input` contains extra spaces. After `strip()` removes the surrounding whitespace, the second comparison succeeds. This is common in form handling, command line tools, and API input validation. When whitespace should be removed from only one side, use `lstrip()` for the left side or `rstrip()` for the right side.

Programs also need to locate, count, or analyze text inside strings. Consider processing an authentication log.

```py
log = "User login failed. User login failed again."

attempts = log.count("failed")
print(attempts) # 2

first_failure = log.find("failed")
print(first_failure) # 11

snippet = log[first_failure:first_failure + 20]
print(snippet) # failed. User login
```

`count()` reports how many times the substring occurs, while `find()` returns the index of its first occurrence. That index can then be used for further processing, such as extracting surrounding context for log viewers, debugging tools, or error summaries.

When the substring might be absent, `find()` is useful because it returns `-1` instead of raising an exception. When the substring is expected to exist and its absence should be treated as an error, use `index()` instead.

```py
missing = log.find("timeout")
print(missing) # -1

separator = log.index(".")
print(separator) # 17
```

If the substring passed to `index()` is missing, Python raises a `ValueError`. This difference makes `find()` suitable when absence is an expected possibility, while `index()` is useful when a required substring should exist and an unexpected format should be detected immediately.

> **Note:** Both `find()` and `index()` return the position of the first matching substring. Their main difference is what happens when no match exists. `find()` returns `-1`, while `index()` raises `ValueError`.

Strings can also be validated before their contents are converted or otherwise processed. The `isdigit()` method returns `True` when the string is not empty and all of its characters are digits.

```py
user_input = "42"

if user_input.isdigit():
    value = int(user_input)
    print("Valid number:", value) # Valid number: 42
else:
    print("Invalid input")
```

This is useful for simple validation when input is expected to contain only digits before conversion to an integer.

> **Note:** `isdigit()` is not a universal test for every numeric format. For example, `"-5".isdigit()` and `"3.14".isdigit()` both return `False` because the minus sign and decimal point are not digits.

Strings provide ordered access to textual data while remaining immutable. Tuples share those two characteristics but are designed to group multiple values rather than represent text, which makes them the next sequence type to examine.

## Tuple Data Type

A **tuple** is an **ordered and immutable collection**. Because tuples are ordered, their values can be accessed by index. Because they are immutable, their elements cannot be added, removed, or reassigned after the tuple has been created.

Tuples are useful when a group of values represents a fixed record that should remain unchanged during program execution. This is common when working with data from external systems, APIs, databases, or configuration sources.

Consider a dataset of transaction records received from an external service.

```py
transactions = [
    (1001, "deposit", 250.00, True),
    (1002, "withdraw", 100.00, False),
    (1003, "deposit", 500.00, True),
]
```

Each tuple represents one transaction, and the meaning of each position remains consistent. Index `0` stores the transaction ID, index `1` stores the transaction type, index `2` stores the amount, and index `3` stores the approval status. Programs that process these records rely on that structure remaining stable.

Because the same processing logic is often applied to many tuples, that logic is usually placed inside a function.

```py
def print_rejected_transactions(transactions):
    for transaction in transactions:
        if not transaction[3]:
            print("Rejected transaction:", transaction[0]) # Rejected transaction: 1002

print_rejected_transactions(transactions)
```

Tuples are commonly processed with loops and conditions to read and calculate values rather than modify the records.

```py
def sum_approved_amount(transactions):
    total = 0

    for transaction in transactions:
        if transaction[3]:
            total += transaction[2]

    return total

total_approved = sum_approved_amount(transactions)

print(total_approved) # 750.0
```

Because a tuple is immutable, attempting to assign a new value to one of its positions raises a `TypeError`.

```py
transaction = (1001, "deposit", 250.00, True)

transaction[2] = 999.00 # TypeError
```

The existing tuple cannot be changed in place. When a program needs different or filtered data, it creates another structure instead of modifying the original tuple.

```py
def filter_approved(transactions):
    approved = []

    for transaction in transactions:
        if transaction[3]:
            approved.append(transaction)

    return approved

approved_transactions = filter_approved(transactions)

print(approved_transactions) # [(1001, 'deposit', 250.0, True), (1003, 'deposit', 500.0, True)]
```

The original transaction dataset remains unchanged, while the approved records are collected separately.

Although tuple values can be accessed individually by index, **tuple unpacking** provides a clearer way to assign the values of a fixed record to separate variables.

```py
transaction = (1001, "deposit", 250.00, True)

tid, ttype, amount, approved = transaction

print(tid) # 1001
print(ttype) # deposit
print(amount) # 250.0
print(approved) # True
```

Each variable receives the value from the corresponding tuple position. Unpacking is useful when the structure is known and several values from the tuple will be used.

> **Note:** Tuple unpacking requires the number of variables to match the number of values being unpacked unless extended unpacking with `*` is used. A mismatch raises a `ValueError`.

Functions can also return several related values as a tuple, which can be unpacked immediately by the caller.

```py
def get_summary(transaction):
    return transaction[0], transaction[2]

tid, amount = get_summary(transaction)

print(tid, amount) # 1001 250.0
```

The function returns the transaction ID and amount together. The returned tuple is then unpacked into `tid` and `amount`, avoiding separate function calls for related results.

Tuples are also frequently used for user records or state snapshots.

```py
users = [
    ("u100", "admin", True),
    ("u101", "editor", False),
    ("u102", "viewer", True),
]

def print_active_admins(users):
    for user in users:
        if user[2] and user[1] == "admin":
            print("Active admin:", user[0]) # Active admin: u100

print_active_admins(users)
```

The tuple structure is trusted, index based access is explicit, and the record itself cannot be modified through item assignment.

Another important use of tuples comes from their ability to serve as dictionary keys when all of their elements are hashable. This is useful when several fixed values together identify an entry.

```py
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}

print(locations[(40.7128, -74.0060)]) # New York
```

Here, each coordinate pair is a tuple used as a dictionary key. A list could not be used in the same position because lists are mutable and therefore unhashable.

> **Note:** A tuple is not automatically hashable just because it is immutable. Every element inside the tuple must also be hashable for the tuple to be used as a dictionary key or set element.

Tuples are not used when the collection itself needs to change. If elements must be added, removed, or reassigned, a list or dictionary is usually more appropriate. Tuples are most useful when the positions form a stable structure and the collection should remain unchanged.

This distinction between mutable and immutable objects becomes especially important when data is copied. The next section examines how Python handles copying, why shallow and deep copies behave differently, and how data structures can be reused without breaking the guarantees that immutability provides.

## Copy

At this point, you might be wondering if mutable collections such as lists, dictionaries, and sets can be copied so that changes to the copy do not affect the original. They can, but the result depends on whether the program creates a **shallow copy** or a **deep copy**.

The difference becomes important when a collection contains other mutable objects. A shallow copy creates a new outer container but can still share nested objects with the original. A deep copy creates independent copies of the nested objects as well.

A shallow copy of a list, dictionary, or set can be created with the corresponding built-in class constructor `list()`, `dict()`, or `set()`. These constructors were introduced in Data Types Level 2, but here their copying behavior is important.

```py
# Shallow copy of a list
original_list = [1, 2, 3]
new_list = list(original_list)

print(new_list) # [1, 2, 3]

# Shallow copy of a dictionary
original_dict = {"a": 1, "b": 2}
new_dict = dict(original_dict)

print(new_dict) # {'a': 1, 'b': 2}

# Shallow copy of a set
original_set = {4, 5, 6}
new_set = set(original_set)

print(new_set) # {4, 5, 6}
```

Each constructor creates a new outer container. We can use `id()` to verify this because `id()` identifies a particular object during its lifetime. The actual number returned by `id()` is not important. What matters is whether two expressions return the same ID.

For a flat collection containing immutable values, the copy is a separate container, so changing the copied container does not change the original.

```py
original_list = [1, 2, 3]
new_list = list(original_list)

print(id(original_list)) # ID of the original list
print(id(new_list)) # Different ID for the copied list
print(id(original_list) == id(new_list)) # False

new_list.append(4)

print(original_list) # [1, 2, 3]
print(new_list) # [1, 2, 3, 4]
```

The two `id()` values are different, and the comparison returns `False`. This confirms that `original_list` and `new_list` are two different list objects. Adding `4` to `new_list` therefore changes only the copy.

> **Note:** The numeric values returned by `id()` can differ each time the program runs. The important comparison is whether two objects have the same ID, not the numbers themselves.

The important limitation appears when the outer container contains mutable objects. A shallow copy still creates a new outer container, but it does not create new copies of the nested objects.

```py
original = [[1, 2], [3, 4]]
shallow_copy = list(original)

print(id(original) == id(shallow_copy)) # False
print(id(original[0]) == id(shallow_copy[0])) # True

shallow_copy[0].append(99)

print(original) # [[1, 2, 99], [3, 4]]
print(shallow_copy) # [[1, 2, 99], [3, 4]]
```

There are **two levels of identity** to notice here. `original` and `shallow_copy` have different IDs because they are separate outer lists. However, `original[0]` and `shallow_copy[0]` have the same ID because both outer lists contain a reference to the same inner list.

When `99` is appended through `shallow_copy[0]`, Python modifies that shared inner list. The change is therefore visible through both `original` and `shallow_copy`.

> **Note:** A shallow copy creates a new outer container, but nested mutable objects can remain shared. A deep copy is needed when those nested objects must also become independent.

Another way to create a shallow copy is with the `.copy()` method, which is available for lists, dictionaries, and sets.

```py
# Using .copy() on a list
original_list = [1, 2, 3]
copied_list = original_list.copy()

print(copied_list) # [1, 2, 3]

# Using .copy() on a dictionary
original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()

print(copied_dict) # {'a': 1, 'b': 2}

# Using .copy() on a set
original_set = {4, 5, 6}
copied_set = original_set.copy()

print(copied_set) # {4, 5, 6}
```

Like the constructors, `.copy()` creates a new outer container but does not recursively copy nested mutable objects. For lists, slicing with `[:]` is another common shallow-copy technique.

```py
original_list = [1, 2, 3]
copied_list = original_list[:]

print(copied_list) # [1, 2, 3]

print(id(original_list) == id(copied_list)) # False
```

The slice `original_list[:]` selects the entire list and creates a new list object. It is still a shallow copy, so nested mutable elements would remain shared.

When nested mutable objects must also be independent, a shallow copy is not enough. Python does not provide deep copying through the built-in `list()`, `dict()`, or `set()` constructors. For that behavior, import the `copy` module and use `copy.deepcopy()`.

The following example shows the difference between a shallow copy and a deep copy.

```py
import copy

# Example of shallow vs deep copy
original_list = [[1, 2], [3, 4]]

# Shallow copy
shallow_copy = copy.copy(original_list) # Same as original_list.copy() or original_list[:]

# Deep copy
deep_copy = copy.deepcopy(original_list)

# Modify inner list
original_list[0][0] = 99

print("Original:", original_list) # Original: [[99, 2], [3, 4]]
print("Shallow copy:", shallow_copy) # Shallow copy: [[99, 2], [3, 4]]
print("Deep copy:", deep_copy) # Deep copy: [[1, 2], [3, 4]]
```

`copy.copy()` creates a shallow copy, so `original_list` and `shallow_copy` still share their inner lists. Changing `original_list[0][0]` is therefore visible through both structures. `copy.deepcopy()` recursively copies the nested lists, so `deep_copy` remains independent.

The same issue applies to nested dictionaries and is not specific to lists.

```py
import copy

original = {
    "users": [
        {"name": "A"}
    ]
}

deep_copy = copy.deepcopy(original)
deep_copy["users"][0]["name"] = "B"

print(original) # {'users': [{'name': 'A'}]}
print(deep_copy) # {'users': [{'name': 'B'}]}
```

The nested list and dictionary inside `deep_copy` are independent copies, so changing the copied user record does not affect `original`.

> **Note:** Use a shallow copy when the collection contains only immutable values, or when sharing nested objects is acceptable. Use `copy.deepcopy()` when the collection contains nested mutable objects and those inner objects must also be independent.
