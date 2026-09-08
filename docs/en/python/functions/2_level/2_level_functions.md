# Level 2

## Table of Contents: Functions

- [Default Parameter Values](#default-parameter-values)
- [Keyword Arguments](#keyword-arguments)
- [Arbitrary Positional Arguments (`*args`)](#arbitrary-positional-arguments-args)
- [Arbitrary Keyword Arguments (`**kwargs`)](#arbitrary-keyword-arguments-kwargs)

**Python Functions Level 2** explores more flexible ways to define function parameters and supply arguments. We begin with **default parameter values**, which allow parameters to use predefined values when arguments are omitted, and **keyword arguments**, which allow arguments to be matched to parameters by name. We then introduce `*args` and `**kwargs`, which allow functions to accept an arbitrary number of positional or keyword arguments.

## Default Parameter Values

A parameter can be assigned a **default value** directly in the function definition. If the caller does not provide an argument for that parameter, Python uses the default value. This is useful when a function has common behavior that should remain available without requiring every argument to be supplied.

```py
def greet(name, language="en"):
    if language == "en":
        return f"Hello, {name}"
    return f"Hi, {name}"

print(greet("Jonas")) # Hello, Jonas
print(greet("Jonas", "lt")) # Hi, Jonas
```

Here, `name` must be supplied, while `language` is optional because it has the default value `"en"`. The first call uses that default, while the second supplies `"lt"` and overrides it.

Default values are also useful for configuration and fallback values.

```py
def connect(host="localhost"):
    return f"Connecting to {host}"

print(connect()) # Connecting to localhost
print(connect("192.168.1.1")) # Connecting to 192.168.1.1
```

When a function contains parameters with and without default values, parameters without defaults must appear before parameters with defaults.

```py
def add(a, b=2):
    return a + b
```

Writing a required parameter after a default parameter produces a `SyntaxError`.

```py
# Invalid
def add(a=1, b):
    return a + b
```

Default values require additional care when they are **mutable objects** such as lists or dictionaries. It may seem natural to use an empty list directly as a default value.

```py
def add_item(item, items=[]):
    items.append(item)
    return items # Return the result

print(add_item(1)) # [1]
print(add_item(2)) # [1, 2]
```

The second call may look as though it should return `[2]`, but it returns `[1, 2]`. The default list is created once when the function is defined, so the same list is reused when later calls omit the `items` argument. The first call adds `1` to that list, and the second call adds `2` to the same list.

To avoid sharing a mutable default object between calls, use `None` as the default value and create a new list inside the function when no list is supplied.

```py
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items # Return the result

print(add_item(1)) # [1]
print(add_item(2)) # [2]
```

Each call that omits `items` creates a new list, so changes made during one call do not appear in another call.

> **Note:** The behavior of mutable default values comes from when Python evaluates default arguments and how objects are referenced. The underlying object model is explored more deeply in **Python Under the Hood Level 2**.

Default parameters make arguments optional, but callers can also identify arguments explicitly by parameter name. This leads to keyword arguments.

## Keyword Arguments

A **keyword argument** supplies a value by writing the parameter name in the function call. This makes the purpose of an argument more explicit and also allows keyword arguments to be supplied in a different order from the parameter definition. Keyword arguments are especially useful with optional parameters or when several values would be difficult to understand from their position alone.

```py
def greet(name, city="Zarasai"):
    print(f"Hello {name} from {city}")

greet(name="Jonas", city="Vilnius") # Hello Jonas from Vilnius
greet(city="Kaunas", name="Ieva") # Hello Ieva from Kaunas
```

Both calls identify each value by parameter name. The second call also shows that keyword arguments do not have to follow the order used in the function definition.

The benefit becomes clearer in a practical example. Consider a function that creates a message for a user account.

```py
def create_user_message(name, active, admin):
    print(name, active, admin)

create_user_message("Mantas", True, False)
```

The call is valid, but the two Boolean values do not clearly communicate what they represent without checking the function definition. Using keyword arguments makes their meaning visible directly in the call.

```py
create_user_message(
    name="Mantas",
    active=True,
    admin=False
)
```

Now it is immediately clear that the user is active but is not an administrator. Keyword arguments therefore improve readability and can reduce mistakes when several values are supplied. They are also commonly combined with default parameter values so that callers can override only the options they need.

So far, every function has required us to know the parameter names in advance. Sometimes, however, a function needs to accept any number of values without knowing how many will be passed. For this, Python provides `*args`.

## Arbitrary Positional Arguments (`*args`)

**Arbitrary positional arguments** allow a function to accept additional positional arguments beyond its fixed parameters. Placing `*` before a parameter collects those additional values into a tuple. By convention, this parameter is usually named `args`, which gives the familiar form `*args`.

```py
def example_function(a, b, *args):
    print("a:", a) # a: 1
    print("b:", b) # b: 2
    print("args:", args) # args: (3, 4, 5)
    print("args type:", type(args)) # args type: <class 'tuple'>

example_function(1, 2, 3, 4, 5)
```

The arguments `1` and `2` are assigned to the fixed parameters `a` and `b`, while the remaining values are collected in `args` as the tuple `(3, 4, 5)`. If there are no additional positional arguments, `args` is an empty tuple. This makes `*args` useful when a function needs to process a variable number of values.

```py
def sum_all(*args):
    total = 0

    for number in args:
        total += number

    return total

print(sum_all(1, 2)) # 3
print(sum_all(5, 10, 15, 20)) # 50
print(sum_all()) # 0
```

The loop processes every value collected in the `args` tuple.

> **Note:** The name `args` is a convention rather than special syntax. The `*` performs the collection, so a more descriptive name such as `*numbers` can also be used.

The `*` operator can also work in the opposite direction when calling a function. Instead of collecting separate arguments into a tuple, placing `*` before an iterable **unpacks** its elements into separate positional arguments.

```py
def calculate_total(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = calculate_total(*numbers)

print(result) # 6
```

The call `calculate_total(*numbers)` behaves like `calculate_total(1, 2, 3)`. The list contains three elements, so those elements are supplied to `a`, `b`, and `c` as three separate positional arguments. Tuples and other suitable iterables can be unpacked in the same way.

`*args` is a good choice when a function performs the same operation on a variable number of similar values. Common examples include calculating a total from any number of numbers, combining several values, or collecting additional items when the caller may supply one, several, or none. It is also useful when a function has some required parameters followed by an unknown number of additional positional values.

```py
def create_order(customer, *items):
    print("Customer:", customer)
    print("Items:", items)

create_order("Jonas", "Keyboard", "Mouse", "Monitor")

# Customer: Jonas
# Items: ('Keyboard', 'Mouse', 'Monitor')
```

Here, `customer` is always required, while the number of ordered items can vary. This is a suitable use of `*args` because every additional positional argument represents another item of the same kind.

Do not use `*args` when a function requires a known set of values with different meanings. Explicit parameter names communicate those requirements more clearly.

```py
def calculate_area(length, width):
    return length * width
```

For this function, `calculate_area(length, width)` is clearer than `calculate_area(*args)` because the required inputs are known and have specific meanings.

Python provides a corresponding mechanism for accepting an unknown number of named values with `**kwargs`.

## Arbitrary Keyword Arguments (`**kwargs`)

**Arbitrary keyword arguments** allow a function to accept keyword arguments whose names are not fixed in advance. Placing `**` before a parameter collects those arguments into a dictionary. By convention, this parameter is usually named `kwargs`, which gives the familiar form `**kwargs`.

```py
def create_user_profile(**kwargs):
    return kwargs

user = create_user_profile(
    name="Mantas",
    age=30,
    city="Vilnius"
)

print(user) # {'name': 'Mantas', 'age': 30, 'city': 'Vilnius'}
```

Inside the function, `kwargs` is a dictionary whose keys are the argument names and whose values are the supplied values.

```py
def show_user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_user_profile(
    name="Austėja",
    city="Kaunas",
    active=True
)

# name: Austėja
# city: Kaunas
# active: True
```

Here, the keyword arguments are collected into `kwargs`, and the loop processes each key and value in the resulting dictionary.

The `**` operator can also work in the opposite direction when calling a function. Instead of collecting keyword arguments into a dictionary, placing `**` before a dictionary **unpacks** its **key-value** pairs into separate keyword arguments.

```py
user = {
    "name": "Ieva",
    "age": 25,
    "city": "Zarasai"
}

def create_profile(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

create_profile(**user) # Ieva is 25 years old and lives in Zarasai
```

The call `create_profile(**user)` behaves like `create_profile(name="Ieva", age=25, city="Zarasai")`. Each dictionary key becomes a parameter name and its corresponding dictionary value becomes the argument value, so the keys must match parameter names that the function can accept.

`**kwargs` is a good choice when a function needs to accept a flexible set of named options and the exact option names may vary between calls. Common examples include optional configuration settings, metadata, profile attributes, and additional named properties that are not all required for every call.

```py
def save_file(filename, **options):
    print("Filename:", filename)
    print("Options:", options)

save_file(
    "report.txt",
    encoding="utf-8",
    backup=True
)
```

Here, `filename` is a known required value, while the additional options can vary. This is a suitable use of `**kwargs` because the extra values are naturally represented as named options rather than positional values.

Do not use `**kwargs` when a function always expects the same named values. In that situation, explicit parameters make the available inputs visible in the function signature and make the function easier to understand.

The two arbitrary argument forms can also be combined when a function genuinely needs both a variable number of positional values and a variable number of keyword values.

```py
def create_order(customer, *items, **details):
    print("Customer:", customer)
    print("Items:", items)
    print("Details:", details)

create_order(
    "Jonas",
    "Keyboard",
    "Mouse",
    delivery="Express",
    paid=True
)

# Customer: Jonas
# Items: ('Keyboard', 'Mouse')
# Details: {'delivery': 'Express', 'paid': True}
```

Here, `customer` receives the fixed argument `"Jonas"`, `items` collects `"Keyboard"` and `"Mouse"` into a tuple, and `details` collects `delivery` and `paid` into a dictionary. This demonstrates when `*args` and `**kwargs` can be useful together. A function can have a known required value, an unknown number of additional positional values, and an unknown number of additional named options.

> **Note:** Default parameters and keyword arguments are useful when the parameter names are known but flexibility is needed in how the function is called. `*args` is appropriate when the number of positional values can vary, while `**kwargs` is appropriate when the number or names of optional keyword values can vary. Together, these tools cover the common function parameter patterns introduced in this **Python Functions Level 2**.
