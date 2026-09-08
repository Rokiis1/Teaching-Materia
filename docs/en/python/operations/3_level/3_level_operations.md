# Level 3

## Table of Contents: Operations

- [Additional numeric utilities](#additional-numeric-utilities)
- [Bitwise operators](#bitwise-operators)
- [Assignment expressions](#assignment-expressions)

In **Python Operations Levels 1 and 2**, we covered arithmetic, assignment, comparison, logical, membership, and identity operators, together with the precedence rules that determine how expressions are grouped. **Python Operations Level 3** extends that foundation with practical numeric utilities, completes the main operator families with bitwise operations, and introduces assignment expressions for cases where assigning and using a value within the same expression can make code more concise.

## Additional numeric utilities

The arithmetic operators introduced in **Python Operations Level 1** handle fundamental numeric calculations directly. Python also provides **built-in numeric utility functions** for common calculations. These functions accept arguments and return values, so their results can be used wherever a value is needed in an expression.

The `abs()` function returns the **absolute value** of a number. For real numbers, this can be understood as the nonnegative distance from zero.

```py
print(abs(10)) # 10
print(abs(-10)) # 10
```

The `round()` function rounds a number. An optional second argument specifies how many decimal places to keep.

```py
print(round(3.6)) # 4
print(round(3.14159, 2)) # 3.14
```

When a value is exactly halfway between two possible rounded results, Python uses **round to nearest, ties to even**.

```py
print(round(2.5)) # 2
print(round(3.5)) # 4
```

Floating-point values require additional care because many decimal fractions cannot be represented exactly in binary. As introduced in **Python Operations Level 2**, this can make direct equality comparisons unreliable for calculated floating-point values. The `math.isclose()` function provides a practical way to compare two numbers using tolerances instead of requiring exact equality.

```py
import math

calculated_total = 0.1 + 0.2
expected_total = 0.3

print(calculated_total == expected_total) # False
print(math.isclose(calculated_total, expected_total)) # True
```

By default, `math.isclose()` uses a small relative tolerance. The optional `rel_tol` and `abs_tol` arguments can be adjusted when a problem requires different comparison rules. Rounding and closeness testing solve different problems, so `round()` should not be treated as a universal replacement for tolerant comparison.

The `min()` and `max()` functions return the smallest and largest values respectively. They can work with individual arguments or with an iterable such as a list.

```py
print(min(3, 7, 1)) # 1
print(max(3, 7, 1)) # 7

numbers = [4, 9, 2, 8]

print(min(numbers)) # 2
print(max(numbers)) # 9
```

The `sum()` function adds numeric values from an iterable. It also accepts an optional `start` value, which is added to the total.

```py
numbers = [1, 2, 3, 4]

print(sum(numbers)) # 10
print(sum(numbers, 5)) # 15
```

The `pow()` function raises a number to a power. With two arguments, it corresponds to exponentiation with `**`.

```py
print(pow(2, 3)) # 8
print(2 ** 3) # 8
```

For integers, `pow()` can also accept a third argument for modular exponentiation.

```py
base = 2
exponent = 5
modulus = 3

print(pow(base, exponent, modulus)) # 2
```

This produces the same final remainder as `(base ** exponent) % modulus`, but the three-argument form performs modular exponentiation without first constructing the potentially very large intermediate power.

The `divmod()` function combines floor division `//` and modulus `%`, which were introduced in **Python Operations Level 1**. It returns the quotient and remainder together.

```py
total_items = 17
group_size = 5

quotient, remainder = divmod(total_items, group_size)

print(quotient) # 3
print(remainder) # 2
```

This produces the same pair of results as calculating `total_items // group_size` and `total_items % group_size` separately. Together, these utilities complement Python's arithmetic operators with reusable functions for common numeric tasks.

Numeric utilities work with complete values. The next section moves to a lower-level representation by examining operators that work with the individual bits of integers.

## Bitwise operators

**Bitwise operators** work with the individual bits that make up integer values. They are useful when values are represented as binary flags, where each bit can represent an independent option or state. The `bin()` function can display an integer in binary form.

```py
permissions = 5

print(bin(permissions)) # 0b101
```

Python provides six main bitwise operators.

```py
left_value & right_value # Bitwise AND
left_value | right_value # Bitwise OR
left_value ^ right_value # Bitwise XOR
~value # Bitwise NOT
value << positions # Left shift
value >> positions # Right shift
```

The `&` operator performs **bitwise AND**. A result bit is `1` only when the corresponding bit is `1` in both operands.

```py
first_value = 6 # 0b110
second_value = 3 # 0b011

result = first_value & second_value

print(result) # 2
print(bin(result)) # 0b10
```

The `|` operator performs **bitwise OR**. A result bit is `1` when the corresponding bit is `1` in either operand.

```py
first_value = 6 # 0b110
second_value = 3 # 0b011

result = first_value | second_value

print(result) # 7
print(bin(result)) # 0b111
```

The `^` operator performs **bitwise XOR**. A result bit is `1` when the corresponding bits are different.

```py
first_value = 6 # 0b110
second_value = 3 # 0b011

result = first_value ^ second_value

print(result) # 5
print(bin(result)) # 0b101
```

The `~` operator performs **bitwise NOT**. For Python integers, the result follows the relationship `~value == -(value + 1)`.

```py
value = 5

print(~value) # -6
```

The shift operators move bits to the left or right. For nonnegative integers, shifting left by one position has the same numeric effect as multiplying by `2`, while shifting right by one position has the same effect as floor dividing by `2`.

```py
value = 5 # 0b101

print(value << 1) # 10
print(value >> 1) # 2
```

Bitwise operators also extend the precedence hierarchy introduced in the earlier levels. From higher to lower precedence, shifts `<<` and `>>` come before bitwise AND `&`, followed by bitwise XOR `^`, then bitwise OR `|`, and finally comparison operators.

!!! note "Bitwise operators and comparisons"

    Bitwise operators have higher precedence than comparison operators. For example, `value & mask == expected` is grouped as `(value & mask) == expected`. Use parentheses when you need the comparison to happen first, such as `value & (mask == expected)`.

A practical use of bitwise operators is working with **flags**. Each bit can represent a separate permission or option, allowing several states to be stored in one integer.

```py
read_permission = 1 # 0b001
write_permission = 2 # 0b010
admin_permission = 4 # 0b100

user_permissions = read_permission | write_permission

can_read = user_permissions & read_permission
can_admin = user_permissions & admin_permission

print(bool(can_read)) # True
print(bool(can_admin)) # False
```

Here, `|` combines permission flags and `&` checks whether a particular flag is present. This pattern is useful when several independent Boolean options need to be represented compactly.

Bitwise operators extend how expressions can manipulate integer values. The final section introduces a different kind of operator that combines assignment with the surrounding expression.

## Assignment expressions

The **assignment expression operator** `:=`, commonly called the **walrus operator**, assigns a value to a variable while also making that value available as part of the surrounding expression. It can avoid repeating a calculation when the result is needed both for a condition and inside the associated block.

```py
data = ["a", "b", "c", "d"]

if (item_count := len(data)) > 3:
    print(item_count) # 4
```

Without an assignment expression, the calculation and assignment would normally be written separately.

```py
data = ["a", "b", "c", "d"]

item_count = len(data)

if item_count > 3:
    print(item_count) # 4
```

The two forms produce the same result, but the assignment expression keeps the calculation close to the condition that uses it. Parentheses are commonly used around assignment expressions inside larger conditions because they make the intended assignment clear and are required in some contexts.

Assignment expressions can also be useful in loops when a value must be obtained and checked during each iteration.

```py
values = [8, 4, 0]

while values and (current_value := values.pop(0)) != 0:
    print(current_value)
```

This prints `8` and `4`. When `current_value` becomes `0`, the condition becomes false and the loop stops. The name assigned with `:=` follows Python's normal scope rules for the surrounding context. The walrus operator does not create a separate local scope, so it should be used only when combining the assignment with the expression makes the code clearer rather than harder to follow.
