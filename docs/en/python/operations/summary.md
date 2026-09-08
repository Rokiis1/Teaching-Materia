# Summary

This summary brings together the most important concepts from the **Operations** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships and differences need to be explained clearly.

## Table of Contents: Operations

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **operators and operands, arithmetic operations, assignment and augmented assignment, and operator precedence**. The main goal is to understand how Python produces values from expressions, how variables can be updated, and how grouping rules determine the meaning of arithmetic expressions.

An **operator** is a symbol that tells Python to perform an operation. The values, variables or expressions that an operator acts on are called **operands**. A **unary operator** acts on one operand, while a **binary operator** acts on two. Unary minus produces the negated value of its operand.

```py
number = 20
negative_number = -number

print(negative_number) # -20
```

Python's main **arithmetic operators** are `+` for addition, `-` for subtraction, `*` for multiplication, `/` for division, `//` for floor division, `%` for modulus and `**` for exponentiation. The same variables can be used to demonstrate how each operation produces a different result.

```py
first_number = 10
second_number = 3

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
floor_division = first_number // second_number
remainder = first_number % second_number
power = first_number ** second_number

print(addition) # 13
print(subtraction) # 7
print(multiplication) # 30
print(division) # 3.3333333333333335
print(floor_division) # 3
print(remainder) # 1
print(power) # 1000
```

The `/` operator produces a floating-point result for ordinary integer division. **Floor division** with `//` rounds the mathematical quotient down toward negative infinity, not toward zero. The `%` operator produces the remainder, while `**` raises a value to a power.

```py
print(10 / 2) # 5.0
print(10 // 3) # 3
print(-10 // 3) # -4
print(10 % 3) # 1
print(2 ** 3) # 8
```

The important distinction is that **division produces a quotient**, **floor division rounds the quotient down**, and **modulus produces the remainder**. For example, `divmod()` is introduced later as a utility that combines floor division and modulus.

The behavior of an operator also depends on the **types of its operands**. Python can combine compatible numeric types, such as an integer and a floating-point number, and the result of their addition is a floating-point value.

```py
result = 10 + 2.5

print(result) # 12.5
```

Not every combination of types is compatible with every operator. Adding an integer and a string directly raises a `TypeError` because Python does not automatically interpret the string as a number.

```py
number = 10
text = "hello"

result = number + text # TypeError
```

Some arithmetic operators also have useful meanings for strings. Multiplying a string by an integer repeats the string rather than performing numeric multiplication.

```py
text = "Hi " * 3

print(text) # Hi Hi Hi
```

The **assignment operator** `=` assigns a value to a variable. An **augmented assignment operator** combines an operation with assignment, allowing an existing value to be updated using a shorter expression. For numeric values, `score += 5` produces the same resulting value as `score = score + 5`.

```py
score = 10
score += 5

print(score) # 15
```

The arithmetic augmented assignment forms are `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, and `**=`. Each applies the corresponding operation and assigns the resulting value to the target.

```py
value = 10
value += 5 # value = value + 5

total = 20
total -= 4 # total = total - 4

quantity = 3
quantity *= 3 # quantity = quantity * 3

amount = 40
amount /= 4 # amount = amount / 4

items = 17
items //= 5 # items = items // 5

remainder = 17
remainder %= 5 # remainder = remainder % 5

base = 2
base **= 3 # base = base ** 3
```

Augmented assignment can also change the type of the value associated with a variable. In the example above, `amount` starts as the integer `40`, but `amount /= 4` assigns the floating-point value `10.0` because ordinary integer division with `/` produces a float.

For numbers, augmented assignment demonstrates the same resulting values as the corresponding expanded assignments. With some **mutable objects**, however, augmented assignment can modify an existing object in place rather than create a new one. This distinction is explored later when working with collections and object identity.

Division by zero is not allowed with `/`, `//`, or `%`. Python raises a `ZeroDivisionError` while evaluating the operation, so an assignment containing that operation is not completed.

```py
result = 10 / 0 # ZeroDivisionError
```

**Operator precedence** determines how operations are grouped when an expression contains several operators. Parentheses `()` explicitly group parts of an expression and can override the default precedence rules. They are not arithmetic operators, but they make the intended grouping clear.

```py
grouped_result = (2 + 3) * 4
normal_result = 2 + 3 * 4

print(grouped_result) # 20
print(normal_result) # 14
```

The arithmetic precedence rules covered in Level 1 can be summarized from higher to lower precedence as follows.

1. Parentheses `()` explicitly group expressions.
2. Exponentiation `**`.
3. Multiplication `*`, division `/`, floor division `//`, and modulus `%`.
4. Addition `+` and subtraction `-`.

**Exponentiation** has higher precedence than multiplication and addition. Consecutive exponentiation operations group from right to left, so `2 ** 3 ** 2` means `2 ** (3 ** 2)`.

```py
result = 2 ** 3 ** 2

print(result) # 512
```

Unary minus has an important relationship with exponentiation. Exponentiation is evaluated before a unary minus written to its left, so `-2 ** 2` means `-(2 ** 2)`. Parentheses are needed when the negative value itself should be the base.

```py
negative_result = -2 ** 2
grouped_result = (-2) ** 2

print(negative_result) # -4
print(grouped_result) # 4
```

Multiplication, division, floor division and modulus share the same precedence level and group from left to right. Addition and subtraction share a lower precedence level and also group from left to right. This is why operations at the same level should not be assumed to follow a different order merely because one operator appears more familiar.

```py
multiplication_result = 10 / 2 * 5
addition_result = 10 - 3 + 2

print(multiplication_result) # 25.0
print(addition_result) # 9
```

The first expression groups as `(10 / 2) * 5`, while the second groups as `(10 - 3) + 2`. Parentheses are useful even when the default precedence would produce a valid expression because they can communicate the intended mathematical formula.

```py
speed = 60
time = 2
delay = 1

distance = speed * (time + delay)

print(distance) # 180
```

The parentheses make `time + delay` one quantity before multiplication by `speed`. Without them, Python would group the expression as `(speed * time) + delay`, which represents a different formula.

The important distinction is that **precedence determines how operators are grouped**, while **associativity determines grouping among operators at the same precedence level when their rules allow repeated operations**. Parentheses provide an explicit way to communicate the intended grouping. **Python Operations Level 2** extends these rules to comparison, logical, membership and identity operators.

After reviewing Level 1, you should be able to explain **what operators and operands are**, distinguish **unary and binary operators**, describe the results of the main **arithmetic operators**, explain the differences between **division, floor division and modulus**, recognize how **operand types** affect operations, distinguish valid string repetition from invalid integer-and-string addition, use **assignment and augmented assignment** to update variables, explain why `/=` can produce a floating-point value, recognize **division by zero**, and apply **precedence, associativity and parentheses** to predict how arithmetic expressions are grouped.
