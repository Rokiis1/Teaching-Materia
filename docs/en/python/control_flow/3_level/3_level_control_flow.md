# Level 3

## Table of Contents: Control Flow

- [Match-Case Statement](#match-case-statement)
- [Nested If Statements](#nested-if-statements)
- [Conditional Expressions (Ternary Operator)](#conditional-expressions-ternary-operator)
- [Nested Loops](#nested-loops)
- [List Comprehension](#list-comprehension)

So far, we have used `if`, `elif`, and `else` to make decisions and loops to repeat actions. As programs grow, these basic tools are often combined or written in more expressive forms to keep complex logic readable. In this **Python Control Flow Level 3**, we will learn how `match-case` organizes decisions around known values, how nested `if` statements handle dependent conditions, how conditional expressions shorten simple two-value choices, how nested loops process multi-level data, and how list comprehensions build new lists concisely from iterable data. We will begin with `match-case`, which provides a structured way to handle several possible values of the same expression.

## Match-Case Statement

The `match-case` statement compares one value against several possible patterns and runs the block belonging to the first matching case. It serves a similar purpose to a long `if-elif-else` chain, but it can be clearer when the decision is based on known, discrete values. A `match-case` statement begins with `match`, followed by the value being examined, and each possible outcome is introduced with `case`.

```py
match value:
    case "option_1:
        pass # Add code for option_1
    case "option_2:
        pass # Add code for option_2
    case _:
        pass # Handle any unmatched value
```

The underscore (`_`) acts as a default case, similar to `else`, and is used when none of the other patterns match.

!!! info "Python Version and Scope"

    The `match-case` statement is available in Python 3.10 and later. Python supports more advanced structural patterns, but this level focuses on matching simple literal values such as strings and numbers.

Here is a simple example that replaces a multi-branch conditional with `match-case`.

```py
command = "start"

match command:
    case "start":
        print("Program started") # Program started
    case "stop":
        print("Program stopped") # Not printed
    case "pause":
        print("Program paused") # Not printed
    case _:
        print("Unknown command") # Not printed
```

Here, `"start"` matches the first case, so Python prints the corresponding message. This pattern is most useful when one controlling value has a known set of possible choices, such as commands, modes, roles, or status values.

A case can also contain additional decision logic when a matched value has its own rules. In the following example, `match-case` first selects the user's role, and an `if` statement inside the matching case then checks whether that account is active.

```py
role = "editor"
active = True

def get_dashboard(role, active):
    match role:
        case "admin":
            if not active:
                return "Admin account inactive"
            return "Admin dashboard"
        case "editor":
            if not active:
                return "Editor account inactive"
            return "Editor dashboard"
        case "viewer":
            return "Viewer dashboard"
        case _:
            return "Unknown role"

dashboard = get_dashboard(role, active)

print(dashboard) # Editor dashboard
```

The example keeps the two decisions at different levels. `match-case` selects the user's role from a known set of values, while the nested `if` checks an additional condition only after `"admin"` or `"editor"` has matched. This makes `match-case` responsible for choosing the category and `if` responsible for checking a condition within that category.

!!! tip "Choosing a Decision Structure"

    Use `match-case` when one value is being compared against several known possibilities. When a decision mainly depends on relationships between multiple conditions, such as `role == "admin" and active`, a normal `if` statement is usually clearer.

Another important consideration is what happens when none of the cases match. The default `_` case provides a fallback for values that were not handled by an earlier case. If a function does not include this fallback, it may reach the end without returning an explicit value.

```py
def handle_command(command):
    match command:
        case "start":
            return "Program started"
        case "stop":
            return "Program stopped"

result = handle_command("restart")

print(result) # None
```

Here, `"restart"` matches neither `"start"` nor `"stop"`, so the function reaches the end and returns `None` implicitly. Adding a default `_` case would allow the function to return an explicit response for unexpected commands.

When there are only one or two simple branches, an `if` or `if-else` statement is often easier to read.

`match-case` is therefore most useful when one controlling value determines which of several known branches should run. Some decisions, however, have a different structure: one condition must succeed before another condition should even be checked. That kind of dependent decision-making leads naturally to nested `if` statements.

## Nested If Statements

Nested `if` statements are useful when one condition should be checked only after another condition has already been satisfied. This creates step-by-step decision logic in which one branch can lead to another check. The basic structure looks like this.

```py
if condition_1:
    if condition_2:
        pass # code executed if both conditions are True
```

Here, `condition_2` is evaluated only if `condition_1` is `True`. This structure is useful when rules depend on one another, such as checking whether a user is logged in before checking the user's role.

```py
user_logged_in = True
user_role = "editor"

if user_logged_in:
    if user_role == "admin":
        print("Admin dashboard loaded") # Not printed
    elif user_role == "editor":
        print("Editor tools loaded") # Editor tools loaded
    else:
        print("Viewer access only") # Not printed
else:
    print("Please log in") # Not printed
```

The outer `if` first checks whether the user is logged in. Only when that condition is `True` does the program evaluate the role inside the nested block. Keeping dependent checks in the correct scope is important because checking a role without first confirming login status can produce incorrect behavior. Nested `if` statements are useful for dependent rules such as checking authentication before permissions, validating one step before continuing to another, or applying additional rules only after an earlier requirement has been satisfied.

!!! tip "When to Nest Conditions"

    Nest a condition only when the inner check genuinely depends on the outer one. If two conditions can be evaluated independently, they usually do not need to be nested.

Nested `if` statements become harder to read when too many dependent checks are placed inside one another. The following example works, but each additional level increases indentation and makes the path through the logic more difficult to trace.

```py
user_logged_in = True
account_active = True
has_subscription = True
is_admin = False

if user_logged_in:
    if account_active:
        if has_subscription:
            if is_admin:
                print("Admin dashboard loaded") # Not printed
            else:
                print("User dashboard loaded") # User dashboard loaded
        else:
            print("Subscription required") # Not printed
    else:
        print("Account inactive") # Not printed
else:
    print("Please log in") # Not printed
```

Although the result is correct, several levels of indentation must be followed before the final action becomes clear. As more rules are added, this style becomes harder to maintain and easier to break. One common way to simplify deeply nested logic inside a function is to handle failure conditions early and return immediately.

```py
user_logged_in = True
account_active = True
has_subscription = True
is_admin = False

def load_dashboard(user_logged_in, account_active, has_subscription, is_admin):
    if not user_logged_in:
        return "Please log in"
    if not account_active:
        return "Account inactive"
    if not has_subscription:
        return "Subscription required"
    if is_admin:
        return "Admin dashboard loaded"

    return "User dashboard loaded"

dashboard = load_dashboard(
    user_logged_in,
    account_active,
    has_subscription,
    is_admin,
)

print(dashboard) # User dashboard loaded
```

These early returns are often called **guard clauses**. Each invalid or failure condition is handled immediately, so the main successful path no longer needs to remain buried inside several nested blocks. This approach is especially useful in functions because `return` stops the function as soon as a condition has been handled.

Another way to reduce nesting is to combine conditions that truly represent one requirement. If several checks must all be `True` before the program can continue, they can sometimes be written in the same condition.

```py
user_logged_in = True
account_active = True
has_subscription = True
is_admin = False

if user_logged_in and account_active and has_subscription:
    if is_admin:
        print("Admin dashboard loaded") # Not printed
    else:
        print("User dashboard loaded") # User dashboard loaded
else:
    print("Access conditions not met") # Not printed
```

This version reduces indentation because the first three checks form one combined access requirement. However, combining too many conditions can make the rule itself difficult to inspect, so nested checks, guard clauses, and combined conditions should be chosen according to which structure makes the dependency clearest.

When the program only needs to choose one of two values from a simple condition, a full `if-else` block may be more verbose than necessary. Python provides a compact alternative for that situation called a conditional expression, also known as the ternary operator.

## Conditional Expressions (Ternary Operator)

A conditional expression chooses between two values in a single expression. It is most useful when the decision is simple enough to remain immediately readable. The expression places the value for the `True` result first, followed by the condition and then the value for the `False` result.

```py
value_if_true if condition else value_if_false
```

Python evaluates the condition first. If it is `True`, the expression produces `value_if_true`; otherwise, it produces `value_if_false`. The following example uses this structure to choose a message from the user's login state.

```py
user_logged_in = True

message = "Welcome back" if user_logged_in else "Please log in"

print(message) # Welcome back
```

Here, `user_logged_in` is `True`, so the expression produces `"Welcome back"` and assigns it to `message`. The same decision could be written with a traditional `if-else` block, but the conditional expression is concise because the program is only choosing between two simple values.

!!! tip "Choosing a Conditional Expression"

    Use a conditional expression when one simple condition chooses between two values. Use a normal `if-else` statement when each branch needs to perform several actions or when writing the logic on one line would make it harder to understand.

Conditional expressions can also be useful when a function needs to return one of two simple values. In the following example, the function evaluates the login state and returns the appropriate greeting directly.

```py
user_logged_in = False

def get_greeting(user_logged_in):
    return "Welcome back" if user_logged_in else "Please log in"

result = get_greeting(user_logged_in)

print(result) # Please log in
```

The function does not need a separate variable or a full `if-else` block because each outcome is a single return value. This keeps the function concise without hiding the decision being made.

Conditional expressions become less suitable when the data has more than two meaningful states. For example, treating every status other than `"online"` as `"Service unavailable"` loses the distinction between states such as `"maintenance"` and `"offline"`.

```py
status = "maintenance"

message = "Service available" if status == "online" else "Service unavailable"

print(message) # Service unavailable
```

The output is technically consistent with the expression, but the logic does not represent all of the meaningful states in the data. A developer might try to add another conditional expression to handle the missing state, but nesting conditional expressions quickly makes the decision harder to read.

```py
status = "maintenance"

message = (
    "Service available"
    if status == "online"
    else "Maintenance mode"
    if status == "maintenance"
    else "Service unavailable"
)

print(message) # Maintenance mode
```

The parentheses allow the expression to span multiple lines, but they do not simplify its logic. You still have to trace multiple conditions inside one expression. When several outcomes must be handled, a traditional `if-elif-else` statement makes the branches more explicit.

```py
status = "maintenance"

if status == "online":
    message = "Service available"
elif status == "maintenance":
    message = "Maintenance mode"
else:
    message = "Service unavailable"

print(message) # Maintenance mode
```

This version is longer, but each possible status and its result are easy to identify. For several branches or multiple actions, standard conditional statements usually provide clearer control flow.

So far, the decisions in this level have selected which code or value should be used. Some problems add another dimension by organizing data into multiple levels, such as rows containing seats, roles containing permissions, or users containing actions. Processing those structures requires repetition inside repetition, which leads to nested loops.

## Nested Loops

A nested loop places one loop inside another. This structure is useful when data naturally has multiple levels, such as rows containing seats, roles containing permissions, sessions containing attendees, or users containing actions.

```py
for outer_item in outer_collection:
    for inner_item in inner_collection:
        # code executed for each inner_item
```

The outer loop selects one group at a time, and the inner loop processes the items inside that group before the outer loop moves to the next one. For example, cinema seats can be organized into rows, with each row containing several seats.

```py
cinema_seats = [
    ["A1", "A2", "A3", "A4"],
    ["B1", "B2", "B3", "B4"],
    ["C1", "C2", "C3", "C4"]
]

for row in cinema_seats:
    for seat in row:
        print("Checking seat:", seat) # A1, A2, A3, A4, then B1 ... C4
```

The same pattern can be used with other grouped structures, including dictionaries whose values contain collections of related items.

```py
role_permissions = {
    "admin": ["read", "write", "delete"],
    "editor": ["read", "write"],
    "viewer": ["read"]
}

for role, permissions in role_permissions.items():
    for permission in permissions:
        print(role, "can", permission) # Prints each role-permission pair
```

This pattern is useful for grouped records such as departments and employees, categories and products, or users and actions.

!!! note "Inner Iterables"

    The inner collection does not have to be a list. It can be another iterable such as a tuple or set. Sets are unordered and do not support positional indexing, so nested loops can process their values, but code should not depend on a particular set iteration order.

Nested loops can also use `range()` when repetition is based on fixed counts rather than stored data. For example, a program may perform several retry checks for each attempt.

```py
max_attempts = 3
retries_per_attempt = 2

for attempt in range(max_attempts):
    for retry in range(retries_per_attempt):
        print("Attempt:", attempt, "Retry:", retry) # Prints each attempt-retry pair
```

The outer loop runs three attempts, and each attempt runs two retries. When the loop variable itself is not needed, `_` can show that the value produced by `range()` is intentionally ignored.

```py
for _ in range(3):
    for _ in range(2):
        print("Sending heartbeat") # Printed 6 times
```

Control-flow statements inside nested loops affect the loop in which they appear. The following example shows how `break` stops an inner loop without stopping the outer loop.

```py
max_attempts = 3
retries_per_attempt = 2

for attempt in range(max_attempts):
    for retry in range(retries_per_attempt):
        if retry == 1:
            break

    print("Attempt finished:", attempt) # Attempt finished: 0, then 1, then 2
```

When `retry` becomes `1`, `break` exits the inner retry loop. The outer attempt loop continues, which is why `"Attempt finished"` is printed for all three attempts. By contrast, `continue` keeps the inner loop running but skips selected iterations.

```py
rows = [
    ["A1", "taken", "A3"],
    ["B1", "B2", "taken"]
]

for row in rows:
    for seat in row:
        if seat == "taken":
            continue

        print("Available seat:", seat) # A1, A3, B1, then B2
```

When the inner loop reaches `"taken"`, `continue` skips the `print()` statement for that seat and moves directly to the next seat in the same row. After the inner loop finishes, the outer loop continues with the next row. This is useful when certain inner items should be ignored without stopping the rest of the group from being processed.

A practical example makes the difference between stopping one loop and stopping an entire function clearer. Suppose each user contains a list of actions and the program needs to identify users whose actions contain an error.

```py
users = [
    {"name": "Example1", "actions": ["login", "view", "logout"]},
    {"name": "Example2", "actions": ["login", "error", "retry", "logout"]},
    {"name": "Example3", "actions": ["login", "view", "purchase", "logout"]}
]

def find_error_users(users):
    for user in users:
        for action in user["actions"]:
            if action == "error":
                print("Error found for user:", user["name"]) # Error found for user: Example2
                break

find_error_users(users)
```

The outer loop processes users, while the inner loop checks each user's actions. Once `"error"` is found, `break` stops checking additional actions for that user, but the outer loop continues to later users. This is appropriate when the goal is to report every user that contains an error without continuing to scan that user's remaining actions after a match has already been found.

If the goal changes to finding only the first user with an error, `return` is more appropriate because it exits the entire function rather than only the inner loop.

```py
users = [
    {"name": "Example1", "actions": ["login", "view", "logout"]},
    {"name": "Example2", "actions": ["login", "error", "retry", "logout"]},
    {"name": "Example3", "actions": ["login", "error", "logout"]}
]


def find_first_error_user(users):
    for user in users:
        for action in user["actions"]:
            if action == "error":
                return user["name"]

    return None


result = find_first_error_user(users)

print(result) # Example2
```

Here, `return` immediately ends the function when the first error is found, so later users are not checked. The placement of `return None` is also important. It belongs after both loops because the function should return `None` only after every user has been checked without finding an error.

!!! note "Nested Loop Control"

    In nested loops, `break` exits only the current loop, `continue` skips the rest of the current iteration of that loop, and `return` exits the entire function. Choose the statement according to how much execution should be skipped or stopped.

Nested loops are most useful when the data or repetition genuinely has multiple levels, such as processing every item within each group. However, unnecessary nesting can make code harder to read and can increase the amount of work performed. When the goal is simply to transform, filter, or collect values into a new list using a straightforward pattern, writing full loop blocks may be more verbose than necessary. Python provides a compact alternative for those cases called a list comprehension.

## List Comprehension

A list comprehension creates a new list from an iterable using a compact expression. It is most useful when the program needs to transform items, filter items, or do both while producing a new list.

```py
[expression for item in iterable]
```

The expression describes the value that will be added to the new list, while the `for` clause supplies each item from the iterable. This is a syntax pattern rather than a standalone program. A simple transformation shows how it works with actual values.

```py
numbers = [1, 2, 3, 4]

doubled = [number * 2 for number in numbers]

print(doubled) # [2, 4, 6, 8]
```

For each `number`, Python evaluates `number * 2` and adds the result to the new list. This pattern is useful when every item should be transformed in the same straightforward way.

A condition can be added when only certain items should be included. The following syntax pattern shows where the condition belongs.

```py
[expression for item in iterable if condition]
```

For example, a program can create a new list containing only even numbers.

```py
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers) # [2, 4, 6]
```

Here, `number` is added to the new list only when `number % 2 == 0` is `True`. List comprehensions are therefore useful for simple transformations and filtering when the result should be a new list.

!!! tip "Choosing a Regular Loop"

    A list comprehension creates a new list. Use a regular loop when the main goal is to perform actions such as printing, updating several values, or handling multiple control-flow steps rather than building a list.

List comprehensions are also useful with structured records. The expression can extract one value from each matching record instead of keeping the entire record.

```py
orders = [
    {"id": "ORD-1001", "status": "shipped"},
    {"id": "ORD-1002", "status": "pending"},
    {"id": "ORD-1003", "status": "shipped"}
]

shipped_order_ids = [
    order["id"]
    for order in orders
    if order["status"] == "shipped"
]

print(shipped_order_ids) # ['ORD-1001', 'ORD-1003']
```

The condition keeps only shipped orders, while `order["id"]` determines what is added to the result. This pattern is useful when a program needs a smaller list containing selected values from a larger dataset, such as identifiers for reporting or further processing.

The same task can be written with a regular loop. Comparing the two forms once makes the relationship clear.

```py
shipped_order_ids = []

for order in orders:
    if order["status"] == "shipped":
        shipped_order_ids.append(order["id"])

print(shipped_order_ids) # ['ORD-1001', 'ORD-1003']
```

Both versions produce the same result. The regular loop separates each step, while the comprehension combines the transformation, iteration, and optional filtering into one expression. The comprehension is usually clearer when those steps remain simple.

List comprehensions can also be returned directly from functions when the function's purpose is to build a new list from existing data.

```py
users = [
    {"name": "Example1", "role": "admin"},
    {"name": "Example2", "role": "editor"},
    {"name": "Example3", "role": "admin"}
]


def get_admin_names(users):
    return [user["name"] for user in users if user["role"] == "admin"]


admins = get_admin_names(users)

print(admins) # ['Example1', 'Example3']
```

The function filters the records by role and extracts only the names that are needed. Because the operation has one clear result and one simple condition, the comprehension keeps the function concise without hiding its purpose.

Comprehensions should become more explicit when the logic grows difficult to scan. Multiple conditions are valid, but compressing several decision steps into one expression can make the code harder to inspect, debug, and extend.

```py
users = [
    {"name": "Example1", "active": True, "role": "admin", "last_login": 45},
    {"name": "Example2", "active": False, "role": "editor", "last_login": 10},
    {"name": "Example3", "active": True, "role": "user", "last_login": 60}
]

result = [
    user["name"]
    for user in users
    if user["active"] and user["role"] == "admin" and user["last_login"] > 30
]

print(result) # ['Example1']
```

Although this comprehension is valid, several requirements are packed into one condition. When those requirements need separate explanations, additional actions, or more complex control flow, a regular loop can make the decisions easier to follow.

```py
result = []

for user in users:
    if not user["active"]:
        continue

    if user["role"] != "admin":
        continue

    if user["last_login"] <= 30:
        continue

    result.append(user["name"])

print(result) # ['Example1']
```

This version is longer, but each filtering rule is visible on its own. The choice between a comprehension and a regular loop should therefore be based on readability rather than simply using the shortest form.

The same comprehension idea can create other collection types. A **dictionary comprehension** builds a dictionary by producing a key-value pair for each included item.

```py
users = [
    {"id": 101, "name": "Example1"},
    {"id": 102, "name": "Example2"},
    {"id": 103, "name": "Example3"}
]

users_by_id = {user["id"]: user["name"] for user in users}

print(users_by_id) # {101: 'Example1', 102: 'Example2', 103: 'Example3'}
```

Here, each user ID becomes a dictionary key and each name becomes its value. Dictionary comprehensions are useful when iterable data needs to be reorganized into key-value relationships for lookup or further processing.

A **set comprehension** follows the same pattern but creates a set, which automatically keeps only unique values.

```py
orders = [
    {"id": "ORD-1001", "status": "shipped"},
    {"id": "ORD-1002", "status": "pending"},
    {"id": "ORD-1003", "status": "shipped"},
    {"id": "ORD-1004", "status": "cancelled"}
]

statuses = {order["status"] for order in orders}

print(statuses) # Order may vary: {'shipped', 'pending', 'cancelled'}
```

The comprehension extracts each status, and the set removes duplicate values automatically. This is useful when the result should contain unique values and their order is not important.

!!! note "Comprehension Result Types"

    List comprehensions use square brackets `[ ]`, dictionary comprehensions use braces with a key-value pair `{key: value}`, and set comprehensions use braces with a single expression `{value}`. Although their result types differ, all three use the same basic pattern of iterating over data and optionally filtering it.

Choose a comprehension when its transformation or filtering rule remains easy to read. For more involved control flow, a regular loop makes the individual steps easier to inspect and maintain.

With **Control Flow Level 3**, you have several ways to express more complex control flow while keeping code readable. `match-case` organizes decisions around known values, nested `if` statements handle dependent checks, and conditional expressions provide a compact choice between two values when the logic is simple. Nested loops process multi-level data, while comprehensions provide concise ways to build new collections from iterable data. Choose the structure that makes your program's decisions and repetition easiest to follow.
