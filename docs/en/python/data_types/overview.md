# Overview

Python data types determine what kind of values a program can store and how those values can be used. Choosing an appropriate type makes it possible to represent information accurately, organize related values, and perform the operations a program requires. Understanding data types also helps prevent unexpected behavior when values are modified, shared between variables, or copied.

Imagine a small application that manages user accounts and transactions. It might store a user's name as a string, an account balance as a number, and an approval status as a Boolean. A list can hold several transaction records, a dictionary can organize a user's details by meaningful keys, and a set can collect unique permissions. A tuple can represent a fixed transaction record, while `None` can indicate that an optional value is absent. As the application grows, choosing the right types becomes important for keeping its data organized and ensuring that changes behave as intended.

The following diagram shows the main data type families covered in this module.

```mermaid
flowchart TD
    A[Python Data Types]

    A --> B[Numeric Types]
    B --> B1[int]
    B --> B2[float]
    B --> B3[complex]

    A --> C[Sequence Types]
    C --> C1[str]
    C --> C2[list]
    C --> C3[tuple]
    C --> C4["array.array"]

    A --> D[Mapping Types]
    D --> D1[dict]

    A --> E[Set Types]
    E --> E1[set]
    E --> E2[frozenset]

    A --> F[Boolean Type]
    F --> F1[bool]

    A --> G[None Type]
    G --> G1[NoneType]
```

The **Data Types** module develops from recognizing Python's fundamental types to creating collections and working with their contents. It then examines how objects behave when they are accessed, modified, and copied. Each level builds on the previous one, moving from basic representation of values toward more practical and predictable data handling.

**Level 1** introduces the foundations of Python data types. It covers **numeric types**, including `int`, `float`, and `complex`, along with **strings**, **Booleans**, and **None**. It also introduces **lists**, **tuples**, **dictionaries**, and **sets**, explaining their basic characteristics, including ordering and mutability. These foundations help learners recognize what different values represent and understand why some objects can be changed while others cannot.

**Level 2** develops the creation and conversion of collection types. It covers **sequence types**, **mapping types**, and **set types**, including the syntax used to create lists, tuples, dictionaries, and sets. It also introduces **collection type casting** through constructors such as `list()`, `tuple()`, `dict()`, and `set()`. This level helps learners choose suitable collection structures and convert data between compatible forms when a program requires a different representation.

**Level 3** develops practical skills for accessing, modifying, and copying data. It covers **indexing and slicing**, **dictionary key access**, **nested access and assignment**, and the behavior of **mutable and immutable objects**. The main sections examine the methods and common operations of **lists**, **dictionaries**, **sets**, **strings**, and **tuples**, including their important limitations. The level concludes with **shallow and deep copying**, showing how separate outer collections can still share nested objects and when independent copies are needed.

Together, these concepts provide a foundation for writing programs that handle data accurately and predictably. They help learners select appropriate types, work with structured information, and understand the consequences of changing or copying objects as programs become more complex.