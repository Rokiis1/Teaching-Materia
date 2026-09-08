# Summary

This summary brings together the most important concepts from the **Control Flow** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships and differences need to be explained clearly.

## Table of Contents: Control Flow

- [Level 1](#level-1)
- [Level 2](#level-2)
- [Level 3](#level-3)

## Level 1

Level 1 establishes the foundations of **conditional statements, loops, `enumerate()` and `range()`**. The main goal is to understand how Python selects execution paths and repeats work according to conditions or iterable values.

**Sequential execution** means statements normally run in order. A **conditional statement** changes that flow by executing a block only when its condition is true. Python uses indentation to identify the statements belonging to a block.

The **`if` statement** executes its block when a condition evaluates to `True`. If the condition is false, Python skips that block and continues after it.

```py
temperature = 25

if temperature > 20:
    print("Warm weather")  # Warm weather

print("Check complete")  # Check complete
```

An **`if-else` statement** selects between two branches. The `if` block runs when the condition is true, and the `else` block runs otherwise. Exactly one of the two branches executes.

```py
temperature = 15

if temperature > 20:
    print("Warm weather")
else:
    print("Cool weather")  # Cool weather
```

An **`if-elif-else` statement** supports several alternatives. Python checks conditions from top to bottom and executes the first matching branch. Once a branch is selected, the remaining branches are skipped. The final `else` is optional and provides a fallback when no earlier condition matches.

```py
temperature = 15

if temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
elif temperature > 10:
    print("Cool")  # Cool
else:
    print("Cold")
```

The order of conditions matters because an earlier broad condition can prevent a later, more specific condition from being reached. Conditions can also be combined with `and`, `or` and `not` when a decision depends on more than one Boolean expression.

A **loop** repeats a block of code. Python's two foundational loop types are `for` and `while`. A `for` loop processes values from an iterable, while a `while` loop repeats as long as its condition remains true.

A **`for` loop** retrieves one item at a time from an iterable, assigns it to the loop variable, and executes the loop body. After the final item, execution continues after the loop. Strings, lists, tuples, dictionaries and other iterable objects can be processed this way.

```py
names = ["Ana", "Ben", "Cara"]

for name in names:
    print(name)  # Ana, then Ben, then Cara
```

A loop can contain conditional statements, allowing each item to be processed differently. Nested data can also be handled by accessing the relevant values inside the loop.

```py
users = [
    {"name": "Ana", "active": True},
    {"name": "Ben", "active": False},
]

for user in users:
    if user["active"]:
        print(user["name"])  # Ana
```

When iterating over a dictionary directly, Python provides its keys. The `.values()` method provides values, while `.items()` provides key-value pairs. Tuple unpacking can assign the two parts of each pair to separate names.

```py
scores = {"Ana": 90, "Ben": 85}

for name, score in scores.items():
    print(name, score)  # Ana 90, then Ben 85
```

The **`enumerate()` function** provides an index together with each item from an iterable. By default, indexing begins at zero, and the `start` argument can change the initial number. It is useful when both an item's position and its value are needed.

```py
names = ["Ana", "Ben"]

for position, name in enumerate(names, start=1):
    print(position, name)  # 1 Ana, then 2 Ben
```

The **`range()` function** represents a sequence of integers and is commonly used to control numeric iteration. `range(stop)` begins at zero and excludes `stop`. The forms `range(start, stop)` and `range(start, stop, step)` provide additional control. The stop value is always excluded, and the step cannot be zero.

```py
for number in range(1, 4):
    print(number)  # 1, then 2, then 3

for number in range(5, 0, -2):
    print(number)  # 5, then 3, then 1
```

The conventional name `_` can be used when the loop variable is intentionally not needed. It remains a normal Python name and does not change how the loop executes.

```py
for _ in range(3):
    print("Hello")  # Hello, three times
```

A **`while` loop** checks its condition before every iteration. If the condition is true, the body executes and the condition is checked again. If it is false, execution continues after the loop. A condition that is false initially prevents the body from running at all.

```py
count = 0

while count < 3:
    print(count)  # 0, then 1, then 2
    count += 1

print("Finished")  # Finished
```

A `while` loop is useful when repetition depends on a changing condition rather than simply processing a known iterable. The loop must have an appropriate way to reach its stopping condition when termination is intended. A `while True` loop is intentionally unbounded unless another control-flow statement exits it.

The important distinction is that **`for` processes iterable values**, while **`while` repeats according to a condition**. Both can contain decisions and other statements, and both continue with the next statement after normal completion.

After reviewing Level 1, you should be able to explain **sequential execution and conditional branching**, distinguish **`if`, `if-else` and `if-elif-else`**, describe why condition order matters, explain how **`for` and `while` loops** execute and terminate, use **`enumerate()`** to track positions, use **`range()`** to control numeric repetition, and recognize how indentation defines the blocks belonging to each control-flow structure.

## Level 2

Level 2 develops direct control over loop execution through **`break`, `continue`, `pass`, loop `else` clauses and `return`**. The main goal is to understand how these statements affect the current iteration, the entire loop, or the function containing the loop.

The **`break` statement** exits the nearest enclosing loop immediately. Python skips the remaining statements in that loop body and continues after the loop. It is useful when a search succeeds, a stopping condition is reached, or further iteration is unnecessary.

```py
for number in range(10):
    if number == 5:
        break
    print(number)  # 0, then 1, then 2, then 3, then 4

print("Loop finished")  # Loop finished
```

A `break` statement exits only the loop in which it appears. If loops are nested, an inner `break` does not automatically exit the outer loop.

A **loop `else` clause** runs when a `for` or `while` loop finishes normally, without executing `break`. It does not mean that the loop body was skipped, and it is not a branch selected by a Boolean condition in the same way as an `if-else` statement.

```py
orders = ["A101", "A102", "A103"]
target = "A102"

for order in orders:
    if order == target:
        print("Order found")  # Order found
        break
else:
    print("Order not found")
```

The `else` block is skipped because the search exits through `break`. If no order matches, the loop finishes normally and the `else` block runs. A `while-else` statement follows the same rule.

The **`continue` statement** skips the remaining statements in the current iteration and proceeds to the next iteration of the nearest enclosing loop. Unlike `break`, it does not exit the loop.

```py
for number in range(6):
    if number % 2 == 0:
        continue
    print(number)  # 1, then 3, then 5
```

`continue` is useful when certain items should be ignored while the remaining items are processed normally. In a `while` loop, any state update needed for termination must still occur on paths that execute `continue`, otherwise the loop may repeat indefinitely.

```py
count = 0

while count < 5:
    count += 1
    if count % 2 == 0:
        continue
    print(count)  # 1, then 3, then 5
```

The **`pass` statement** performs no action. It is a syntactically valid placeholder for a block that intentionally contains no behavior. It does not skip an iteration, exit a loop, or terminate a function.

```py
def unfinished_feature():
    pass

class FutureFeature:
    pass

if True:
    pass

print("Program continues")  # Program continues
```

The distinction between the three statements is important. **`break` exits the current loop**, **`continue` skips the remainder of the current iteration**, and **`pass` does nothing while normal execution continues**. Their effects depend on where they are placed, and they are not interchangeable.

The **`return` statement** exits a function and optionally provides a value to its caller. When a loop is inside a function, `return` exits the function rather than merely exiting the loop. This makes it useful when a search result should be returned immediately.

```py
def find_order(orders, target):
    for order in orders:
        if order == target:
            return order
    return None

orders = ["A101", "A102", "A103"]

print(find_order(orders, "A102"))  # A102
print(find_order(orders, "A999"))  # None
```

In this example, the first `return` ends the function as soon as the order is found. If the loop finishes without finding a match, the final `return None` provides an explicit not-found result. A function without an executed return statement also returns `None` implicitly.

The important distinction is that **`break` controls loop execution**, while **`return` controls function execution**. A loop `else` clause provides a way to distinguish normal completion from an early exit through `break`, while `continue` and `pass` have different effects on the remaining work.

After reviewing Level 2, you should be able to explain **when and why to use `break`, `continue` and `pass`**, trace how each affects execution, distinguish **normal loop completion from early termination**, explain when a **loop `else` clause** runs, recognize the risk of skipping a necessary `while` state update, and distinguish **`return` from `break`** when a loop is placed inside a function.

## Level 3

Level 3 introduces more expressive control-flow structures through **`match-case`, nested `if` statements, conditional expressions, nested loops and comprehensions**. The main goal is to organize dependent decisions, process multi-level data, and express transformations and filtering rules clearly.

The **`match-case` statement**, available in Python 3.10 and later, selects a branch by matching a subject against patterns. For simple literal patterns, it provides a readable way to organize decisions around known values. Python checks cases in order and executes the first matching case. The wildcard pattern `_` provides a fallback.

```py
command = "start"

match command:
    case "start":
        print("Program started")  # Program started
    case "stop":
        print("Program stopped")
    case _:
        print("Unknown command")
```

A case can include a guard using `if`, allowing a pattern to match only when an additional condition is true. This is useful when a known value must also satisfy a related requirement.

```py
role = "editor"
active = True

match role:
    case "admin" if active:
        print("Admin dashboard")
    case "editor" if active:
        print("Editor dashboard")  # Editor dashboard
    case "viewer":
        print("Viewer dashboard")
    case _:
        print("Access unavailable")
```

A `match` statement does not require a wildcard case. If no case matches and no fallback is provided, execution continues after the statement. When a function reaches its end without returning a value, it returns `None` implicitly.

**Nested `if` statements** place one conditional statement inside another. They are useful when a later decision should be evaluated only after an earlier requirement has been satisfied.

```py
logged_in = True
role = "admin"

if logged_in:
    if role == "admin":
        print("Admin dashboard")  # Admin dashboard
    else:
        print("User dashboard")
else:
    print("Please log in")
```

The inner condition is evaluated only when the outer condition is true. This makes the dependency explicit, but excessive nesting can make code harder to follow. Related conditions can sometimes be combined, while functions can use early returns to handle invalid or exceptional cases before the main logic.

```py
def load_dashboard(logged_in, active, role):
    if not logged_in:
        return "Please log in"
    if not active:
        return "Account inactive"
    if role == "admin":
        return "Admin dashboard"
    return "User dashboard"

print(load_dashboard(True, True, "admin"))  # Admin dashboard
```

A **conditional expression**, sometimes called a ternary expression, selects one of two values using a condition. Its form is `value_if_true if condition else value_if_false`. It is useful for a short, readable choice that produces a value.

```py
logged_in = True

message = "Welcome back" if logged_in else "Please log in"

print(message)  # Welcome back
```

A conditional expression differs from an `if-else` statement because it is an expression that produces a value. It should not replace a longer conditional structure when doing so makes the logic difficult to read. Nested conditional expressions are possible, but ordinary `if-elif-else` statements are often clearer for several alternatives.

**Nested loops** place one loop inside another. For each iteration of the outer loop, the inner loop runs through its iterable. They are useful for processing grouped or multi-level data, such as rows and seats, users and permissions, or records containing collections.

```py
rows = [
    ["A1", "A2"],
    ["B1", "B2"],
]

for row in rows:
    for seat in row:
        print(seat)  # A1, A2, B1, B2
```

The outer loop selects a row, and the inner loop processes its seats before the next row is selected. The inner iterable can be any suitable iterable, and its type does not have to match the outer iterable's type.

Nested loops can also contain `break` and `continue`. A `break` inside the inner loop exits only that inner loop, while `continue` skips the remainder of the current inner iteration. When nested search logic is placed inside a function, `return` can exit the function immediately after a result is found.

```py
def find_first_error_user(users):
    for user in users:
        for status in user["statuses"]:
            if status == "error":
                return user["name"]
    return None

users = [
    {"name": "Ana", "statuses": ["ok", "ok"]},
    {"name": "Ben", "statuses": ["ok", "error"]},
]

print(find_first_error_user(users))  # Ben
```

The first matching error causes the function to return immediately. If every status is checked without finding an error, the function returns `None`.

A **list comprehension** creates a new list by expressing iteration, transformation and optional filtering in a compact form. It is useful when a straightforward loop builds a collection from an iterable.

```py
numbers = [1, 2, 3, 4]

doubled = [number * 2 for number in numbers]
evens = [number for number in numbers if number % 2 == 0]

print(doubled)  # [2, 4, 6, 8]
print(evens)  # [2, 4]
```

The first comprehension transforms every number, while the second filters the input. A comprehension can also combine filtering and transformation.

```py
orders = [
    {"id": "A101", "status": "shipped"},
    {"id": "A102", "status": "pending"},
    {"id": "A103", "status": "shipped"},
]

shipped_ids = [
    order["id"]
    for order in orders
    if order["status"] == "shipped"
]

print(shipped_ids)  # ['A101', 'A103']
```

The same result can be built with a regular loop and `.append()`. Comprehensions are appropriate when they make the transformation easier to understand, while a regular loop is often clearer when the logic involves several steps, complex conditions, or side effects.

**Dictionary comprehensions** build dictionaries from key-value expressions, while **set comprehensions** build sets of unique values. They follow the same general idea of iteration with optional filtering, but the resulting collection has different properties.

```py
users = [
    {"id": 1, "name": "Ana"},
    {"id": 2, "name": "Ben"},
]

user_lookup = {user["id"]: user["name"] for user in users}

print(user_lookup)  # {1: 'Ana', 2: 'Ben'}

statuses = ["pending", "shipped", "pending"]

unique_statuses = {status for status in statuses}

print(unique_statuses == {"pending", "shipped"})  # True
```

Dictionary keys must be unique, so later values replace earlier values when a comprehension produces the same key more than once. Sets also contain unique elements and do not guarantee iteration order. A list comprehension preserves the order in which its results are produced.

The important distinction is that **`match-case` organizes pattern-based decisions**, **nested `if` statements express dependent conditions**, **conditional expressions produce one of two values**, **nested loops process multiple levels of iteration**, and **comprehensions build collections through concise transformation and filtering rules**. The most appropriate structure is the one that communicates the intended behavior clearly.

After reviewing Level 3, you should be able to explain **how `match-case` selects branches and uses guards**, distinguish it from ordinary conditional statements, describe when **nested `if` statements and early returns** improve decision logic, use **conditional expressions** for readable two-value choices, trace **nested loops** and their control statements, and distinguish **list, dictionary and set comprehensions** while recognizing when a regular loop is clearer.
