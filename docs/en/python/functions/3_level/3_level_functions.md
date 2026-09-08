# Level 3

## Table of Contents: Functions

- [First-class functions](#first-class-functions)
- [Higher-order functions](#higher-order-functions)
- [Lambda functions](#lambda-functions)
- [Built-in higher-order functions](#built-in-higher-order-functions)

In Python, functions are more than blocks of code that run when they are called. Functions are **objects**, which means they can be treated as values. They can be assigned to variables, stored in data structures, and passed as arguments to other functions.

This **Python Functions Level 3** explores how treating functions as values allows programs to separate **what should happen** from **how that behavior is used**. We begin with **first-class functions**, then use them to understand **higher-order functions**, **callbacks**, **lambda functions**, and built-in tools that accept functions as arguments.

## First-class functions

In Python, functions are **first-class objects**, which means they can be treated like other values in a program. A function can be assigned to a variable, stored in a collection, passed to another function, and used later.

Consider two simple validation functions.

```py
def validate_length(value):
    return len(value) >= 5

def validate_digits(value):
    return value.isdigit()

print(validate_length("hello")) # True
print(validate_length("hi")) # False
print(validate_digits("12345")) # True
print(validate_digits("Jonas")) # False
```

Both functions return Boolean values based on different validation rules. Normally, we call a function by adding parentheses, but we can also refer to the function itself without calling it. This allows a variable to store a function reference and later use that variable to call the function.

```py
validator = validate_length # Reference to the function

print(validator("hello")) # True

validator = validate_digits # Change the function reference

print(validator("12345")) # True
print(validator("Jonas")) # False
```

The line `validator = validate_length` stores a reference to `validate_length` without executing it, while `validator("hello")` calls the referenced function. The same variable can later refer to `validate_digits`, changing which function is executed when `validator()` is called.

Function references can also be stored in a collection and processed together.

```py
validators = [
    validate_length,
    validate_digits
]

value = "12345"

for check in validators:
    print(check(value))

# True
# True
```

Each item in `validators` refers to a function. During each loop iteration, `check` refers to one of those functions, and `check(value)` calls it with the same value.

The next step uses this idea more directly. Instead of selecting a function before an operation begins, we can **pass a function to another function** and let that function decide when to use it.

## Higher-order functions

A **higher-order function** is a function that accepts another function as an argument, returns a function, or both. In this level, we focus on passing functions as arguments.

Passing a function as an argument allows one function to provide the general process while another function provides the specific behavior. Consider a function that receives a value together with the operation that should be applied to it.

```py
def process_value(value, action):
    return action(value)

def to_upper(text):
    return text.upper()

def add_prefix(text):
    return "USER_" + text

print(process_value("jonas", to_upper)) # JONAS
print(process_value("jonas", add_prefix)) # USER_jonas
```

The `process_value()` function does not decide how the value should be changed. The `action` parameter receives a function, and `action(value)` calls it with the supplied value. The functions `to_upper` and `add_prefix` are passed without parentheses because we are passing the function objects rather than calling them immediately.

The same pattern can process a collection when the overall loop stays the same but the behavior applied to each value may change.

```py
names = ["Jonas", "Ieva", "Mantas"]

def apply_rule(values, rule):
    results = []

    for value in values:
        results.append(rule(value))

    return results

def make_upper(text):
    return text.upper()

result = apply_rule(names, make_upper)

print(result) # ['JONAS', 'IEVA', 'MANTAS']
```

Here, `apply_rule()` controls how the collection is processed, while `make_upper()` defines what happens to each element. A different function can be passed as `rule` without changing the loop inside `apply_rule()`.

Another common use of higher-order functions is a **callback**, which is a function passed to another function so that it can be called when a particular part of an operation is reached.

```py
def complete_task(task_name, on_complete):
    print(f"Completed {task_name}")
    on_complete(task_name)

def show_confirmation(task_name):
    print(f"Confirmation sent for {task_name}")

complete_task("Backup", show_confirmation)

# Completed Backup
# Confirmation sent for Backup
```

The `show_confirmation` function is passed to `complete_task()` without being called immediately. Inside `complete_task()`, the callback runs through `on_complete(task_name)` after the task completion message is printed. This allows `complete_task()` to control **when** the additional behavior runs while the caller controls **what** that behavior does.

Named functions are useful when the supplied behavior is reused or requires several statements. When the behavior is short and needed only once, Python provides a more compact form with a **lambda function**.

## Lambda functions

A **lambda function** is a small anonymous function written as a single expression. It can accept arguments, returns the result of its expression automatically, and is most useful when a short function is needed only once. Unlike a regular function created with `def`, a lambda does not have a function name in its syntax and does not use an explicit `return` statement.

The general syntax is as follows.

```py
lambda parameters: expression
```

The `parameters` are the values the lambda receives, just like parameters in a regular function. The `expression` is evaluated when the lambda is called, and its result is returned automatically. A lambda can contain only one expression, which is why it is intended for short behavior rather than multi-step logic.

To see the difference clearly, first consider a regular function that doubles a number.

```py
def double(number):
    return number * 2

print(double(5)) # 10
```

The same calculation can be written as a lambda.

```py
double = lambda number: number * 2

print(double(5)) # 10
```

Both versions return the same result. The regular function uses `def` and an explicit `return`, while the lambda places its parameter and expression on one line. Assigning a lambda to a variable is useful here for comparison, but a regular `def` function is usually clearer when the behavior will be reused. Lambdas are most useful when they are passed directly to another function.

For example, a short discount rule can be passed directly to a function that applies a supplied rule to every value.

```py
prices = [20, 50, 100]

def apply_rule(values, rule):
    results = []

    for value in values:
        results.append(rule(value))

    return results

discounted_prices = apply_rule(
    prices,
    lambda price: price * 0.9
)

print(discounted_prices) # [18.0, 45.0, 90.0]
```

In `lambda price: price * 0.9`, `price` is the parameter and `price * 0.9` is the expression whose result is returned automatically. The `apply_rule()` function controls how the collection is processed, while the lambda defines what happens to each price. This is a practical use of a lambda because the rule is short and needed only for this operation.

A lambda can also accept more than one parameter. For example, a short pricing rule can calculate a total from a price and quantity.

```py
calculate_total = lambda price, quantity: price * quantity

print(calculate_total(12, 3)) # 36
```

Here, `price, quantity` are the parameters, and `price * quantity` is the single expression whose value is returned.

Lambdas can also be passed directly to another function when a small transformation is needed for one value. For example, `process_value()` can receive a function that determines how the supplied value should be transformed.

```py
def process_value(value, action):
    return action(value)

formatted_name = process_value(
    "ieva",
    lambda name: name.capitalize()
)

print(formatted_name) # Ieva
```

Here, `process_value()` controls when the transformation is applied, while the lambda defines the transformation itself. Because the behavior is short and needed only for this call, defining it inline avoids creating a separate named function.

A lambda should remain simple. If the behavior requires several steps or will be reused, a regular `def` function is clearer. For example, cleaning and formatting user input involves more than one operation.

```py
def format_user(name):
    cleaned = name.strip()
    return cleaned.capitalize()

print(format_user("  jonas  ")) # Jonas
```

Trying to force several processing steps into a lambda would make the intention harder to read. In practice, lambdas are especially useful when another function needs one short rule, such as selecting records, transforming values, or choosing a value for sorting. Use a lambda for **short, one time behavior passed to another function**, and use `def` when the behavior is **more complex or reusable**.

This makes lambdas especially useful with the built-in higher-order functions explored next.

## Built-in higher-order functions

When programs work with collections, the same operations appear frequently. We may need to select values, transform them, order them according to a rule, or combine them into one result. Python provides tools such as `filter()`, `map()`, `sorted()`, and `reduce()` that accept functions to control these operations. We will use one shared dataset so that each example builds on the same data.

```py
requests = [
    {"id": 101, "user": "Jonas", "status": "ok", "priority": 2, "cost": 10},
    {"id": 102, "user": "Ieva", "status": "failed", "priority": 1, "cost": 20},
    {"id": 103, "user": "Mantas", "status": "ok", "priority": 3, "cost": 5},
    {"id": 104, "user": "Austėja", "status": "ok", "priority": 1, "cost": 15}
]
```

We begin with `filter()`. It receives a function and an iterable, then keeps only the values for which the supplied function returns a truthy result.

```py
filter(function, iterable)
```

The `function` is called once for each item and decides whether that item should remain, while the `iterable` provides the values to check. `filter()` returns an iterator containing only the accepted values.

```py
valid_requests = list(
    filter(lambda req: req["status"] == "ok", requests)
)

print([req["user"] for req in valid_requests]) # ['Jonas', 'Mantas', 'Austėja']
```

In this call, `lambda req: req["status"] == "ok"` is the `function`, and `requests` is the `iterable`. The lambda receives one request at a time and returns `True` when its status is `"ok"`. `filter()` controls the iteration, while the lambda controls which values remain.

An important detail is that `filter()` returns an **iterator**, not a list. If we print the result directly, Python displays the iterator object rather than the filtered values.

```py
valid_requests = filter(
    lambda req: req["status"] == "ok",
    requests
)

print(valid_requests) # <filter object at 0x...>
```

The exact memory address varies between runs. An iterator is consumed as its values are read, so it cannot restart automatically after it has been exhausted.

```py
valid_requests = filter(
    lambda req: req["status"] == "ok",
    requests
)

print([req["user"] for req in valid_requests]) # ['Jonas', 'Mantas', 'Austėja']
print(list(valid_requests)) # []
```

The second result is empty because the first iteration already consumed the iterator. When filtered values will be reused, converting the iterator to a list once keeps the result available, which is why the earlier `valid_requests` variable stores `list(filter(...))`.

After selecting the valid requests, we can transform them with `map()`. It applies a supplied function to each value and produces one transformed result for each input value.

```py
map(function, iterable)
```

The `function` defines how each item should be transformed, while the `iterable` provides the input values. `map()` returns an iterator containing the transformed results.

```py
costs = list(
    map(lambda req: req["cost"], valid_requests)
)

print(costs) # [10, 5, 15]
```

Here, `lambda req: req["cost"]` is the `function`, and `valid_requests` is the `iterable`. For each request, the lambda returns its `"cost"` value. `map()` handles the iteration, while the lambda defines the transformation. Like `filter()`, `map()` returns an iterator and is consumed as its values are read.

```py
mapped_costs = map(lambda req: req["cost"], valid_requests)

print(mapped_costs) # <map object at 0x...>
print(list(mapped_costs)) # [10, 5, 15]
print(list(mapped_costs)) # []
```

Another common operation is sorting. The `.sort()` list method was already introduced in **Python Data Types Level 3**, so here the focus is on how a function can control sorting through the `key` parameter. The built-in `sorted()` function accepts an iterable and returns a new sorted list.

```py
sorted(iterable, key=None, reverse=False)
```

The `iterable` provides the values to sort. The optional `key` argument receives a function that returns the value Python should use for ordering each item, while `reverse` controls the direction with `False` for ascending order and `True` for descending order.

```py
ordered_requests = sorted(
    valid_requests,
    key=lambda req: req["cost"]
)

print([(req["user"], req["cost"]) for req in ordered_requests]) # [('Mantas', 5), ('Jonas', 10), ('Austėja', 15)]

print([(req["user"], req["cost"]) for req in valid_requests]) # [('Jonas', 10), ('Mantas', 5), ('Austėja', 15)]
```

In this call, `valid_requests` is the `iterable`, and `lambda req: req["cost"]` is the `key` function. The lambda does **not** perform the sorting. Python performs the sorting and calls the key function for each request to obtain the value that should determine its position. The returned key values are `10`, `5`, and `15`, so the requests are ordered by cost. The second print shows that `sorted()` leaves the original `valid_requests` list unchanged.

Changing the function passed to `key` changes the sorting rule without changing the sorting operation itself.

```py
ordered_by_priority = sorted(
    valid_requests,
    key=lambda req: req["priority"]
)

print([(req["user"], req["priority"]) for req in ordered_by_priority]) # [('Austėja', 1), ('Jonas', 2), ('Mantas', 3)]
```

The same key concept can be combined with `reverse=True` when the result should use descending order.

```py
highest_cost_first = sorted(
    valid_requests,
    key=lambda req: req["cost"],
    reverse=True
)

print([(req["user"], req["cost"]) for req in highest_cost_first]) # [('Austėja', 15), ('Jonas', 10), ('Mantas', 5)]
```

> **Note:** `.sort()` accepts the same `key` and `reverse` arguments, but it modifies the existing list in place and returns `None`. Its basic behavior was covered in **Python Data Types Level 3**. Here, the new idea is that a function passed through `key` controls which value Python uses for ordering.

Finally, we may need to combine many values into one result. The `reduce()` function from the `functools` module repeatedly calls a supplied function to combine the accumulated result with the next item.

```py
reduce(function, iterable, initializer)
```

The `function` receives two values and returns their combined result, the `iterable` provides the values being processed, and the optional `initializer` supplies the starting accumulator value. Unlike `filter()` and `map()`, `reduce()` returns one final accumulated value rather than an iterator.

```py
from functools import reduce

total_cost = reduce(
    lambda acc, req: acc + req["cost"],
    valid_requests,
    0
)

print(total_cost) # 30
```

In this call, `lambda acc, req: acc + req["cost"]` is the combining `function`, `valid_requests` is the `iterable`, and `0` is the `initializer`. The accumulator begins at `0`, then changes to `10`, `15`, and finally `30` as each request is processed. The lambda defines how each request contributes to the accumulated result, while `reduce()` controls the repeated combination.

For this calculation, `sum()` is clearer because Python already provides a built-in operation for totals.

```py
total_cost = sum(costs)

print(total_cost) # 30
```

Use `reduce()` when the values need to be combined through a custom operation that is not already expressed more clearly by a simpler built-in function.

The individual tools can also be combined when a program needs several processing steps. For example, the same request data can be filtered to keep successful requests, sorted by priority, transformed into costs, and then totaled.

```py
valid_requests = list(
    filter(lambda req: req["status"] == "ok", requests)
)

ordered_requests = sorted(
    valid_requests,
    key=lambda req: req["priority"]
)

costs = list(
    map(lambda req: req["cost"], ordered_requests)
)

total_cost = sum(costs)

print([req["user"] for req in ordered_requests]) # ['Austėja', 'Jonas', 'Mantas']
print(costs) # [15, 10, 5]
print(total_cost) # 30
```

This example shows how these tools can work together in practice. Each operation has one clear responsibility. `filter()` selects the records that should remain, `sorted()` orders them according to a supplied rule, and `map()` extracts the values needed for the final calculation. The lambdas keep these short rules close to the operations that use them, while `sum()` expresses the final total more clearly than `reduce()` would in this case.

So far, we have used functions as values that we pass into other functions. In the next **Python Functions Level 4**, we will see how functions can also create and return other functions, call themselves, and wrap existing functions.
