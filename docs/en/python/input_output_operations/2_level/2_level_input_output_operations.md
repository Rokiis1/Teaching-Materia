# Level 2

## Table of Contents: Inputs and Outputs Operations

- [Format Specifiers](#format-specifiers)
- [Padding and Alignment](#padding-and-alignment)
- [Width and Precision](#width-and-precision)
- [Numeric Formatting](#numeric-formatting)

In this **Inputs and Outputs Operations Level 2**, we will learn how to control the appearance of displayed values using **format specifiers** in f-strings. We will begin with format specifier syntax, then explore **padding and alignment**, control **width and precision**, and apply **numeric formatting** to display large numbers and percentages clearly and consistently.

## Format Specifiers

A **format specifier** controls how a value or expression is displayed inside an f-string. It is written after a colon within the curly braces, following the general syntax `{value:format}`. The part before the colon contains the **value or expression** being formatted, while the part after the colon contains the **formatting instructions**. These instructions control how the result is displayed without changing the original value.

Format specifiers support several formatting options, including **padding, alignment, width, precision, and numeric formatting**. We will begin with padding and alignment, which control how values are positioned within the available space.

## Padding and Alignment

**Padding** adds extra characters to fill a specified width, while **alignment** determines where a value appears within that space. Spaces are used for padding by default, helping values of different lengths line up in repeated output.

!!! note "Width Is a Minimum"

    A format width specifies the **minimum number of characters** used to display a value, not a maximum. Python adds padding when the formatted value is shorter than the width, but does not truncate longer values. For example, `"Vardenis"` contains eight characters, so a width of `8` adds no padding and a width of `9` adds one space.

Within a format specifier, `<` aligns content to the left, `>` aligns it to the right, and `^` centers it. The alignment symbol is followed by the minimum width. Vertical bars in the following examples make the spaces visible.

```py
text = "Example"
print(f"|{text:<10}|") # |Example   |
print(f"|{text:>10}|") # |   Example|
print(f"|{text:^10}|") # | Example  |
```

The seven-character string receives three spaces in each case. Left alignment places them after the text, right alignment places them before it, and center alignment distributes them around the text. When the padding cannot be divided evenly, the extra space appears on the right for centered text.

```py
name = "Vardenis"
print(f"|{name:>10}|") # |  Vardenis|
print(f"|{name:>6}|") # |Vardenis|
```

The first call adds two leading spaces. The second displays the complete name despite the smaller requested width. Numbers can also be padded with leading zeros when a fixed number of digits is useful.

```py
number = 7
print(f"{number:03}") # 007
```

The specifier `03` fills unused positions with zeros until the displayed number occupies at least three characters. Alignment determines where values appear, while precision provides additional control over how numbers are displayed.

## Width and Precision

For numeric values, **width** reserves a minimum amount of space, and numbers are right-aligned by default. This makes it possible to align numbers of different lengths in a column.

```py
number = 42
print(f"|{number:5}|") # |   42|
```

**Precision** controls the number of digits displayed in a particular numeric format. With the `f` format type, `.2f` displays two digits after the decimal point. Python rounds the displayed result as needed without changing the stored value.

```py
value = 3.1415926
print(f"{value:.2f}") # 3.14
```

Width and precision can also be combined in one format specifier. The width includes the digits, decimal point, and padding, while precision determines the number of decimal places.

```py
value = 3.1415926
print(f"|{value:8.2f}|") # |    3.14|
```

The formatted number `3.14` occupies four characters, so Python adds four leading spaces to meet the minimum width of eight. Beyond spacing and decimal precision, numeric formatting also provides ways to display large numbers and percentages more clearly.

## Numeric Formatting

**Numeric formatting** allows large numbers to be grouped into thousands and ratios to be displayed as percentages, making numerical output easier to read. These options can also be combined with precision for greater control over how values appear. For example, a comma in a format specifier separates digits into groups of thousands.

```py
value = 1234567
print(f"{value:,}") # 1,234,567
```

The comma can also be combined with decimal precision to group the integer part while displaying a consistent number of decimal places.

```py
value = 1234567.8912
print(f"{value:,.2f}") # 1,234,567.89
```

The `%` format type multiplies the value by 100 and adds a percent sign. Its precision determines how many decimal places appear in the displayed percentage.

```py
ratio = 0.75
print(f"{ratio:.0%}") # 75%
print(f"{ratio:.1%}") # 75.0%
```

!!! note "Formatting with `.2f` and Rounding with `round()`"

    Formatting a number with `.2f` produces a **string** with exactly two digits after the decimal point, while `round(value, 2)` returns a **numeric value** rounded to two decimal places. The numeric result does not retain trailing zeros for display, and neither operation changes the original variable unless its result is assigned back to it.

    ```py
    value = 3.5
    print(f"{value:.2f}") # 3.50
    print(round(value, 2)) # 3.5
    print(type(f"{value:.2f}")) # <class 'str'>
    print(type(round(value, 2))) # <class 'float'>
    ```

    Use `.2f` when a consistent displayed format is needed. Use `round()` when a rounded numeric result is needed for further calculations. Both operations follow Python's floating-point rounding behavior, so some values may produce results that differ from everyday decimal rounding expectations.

The important distinction is that **width and alignment control the space used by a displayed value**, **precision controls its displayed decimal detail**, and **numeric format types control its representation**. These options can be combined to produce consistent and readable output.

In **Inputs and Outputs Operations Level 3**, we will move beyond console input and output to explore **file operations**, including opening, reading, writing, and closing files. This will allow Python programs to work with information stored in files rather than relying only on values entered or displayed through the console.
