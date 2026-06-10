# Data types 

- Number : 123 , 4543

- int	: 10	(Integer numbers)
- float :	3.14	(Decimal numbers)
- complex	: 2 + 3j	(Complex numbers)
- str	: "Hello"	(Text/String)
- bool :	True, False	(Boolean values)
- list :	[1, 2, 3]	(Ordered, mutable collection)
- tuple :	(1, 2, 3)	(Ordered, immutable collection)
- set :	{1, 2, 3}	(Unordered unique items)
- dictionary :	{"name": "Ali"}	(Key-value pairs)
- NoneType :	None	(Represents no value)



# Mutable Data Types
-- A mutable object can be changed after it is created.
* `list`
* `dict`
* `set`
* `bytearray`


# Immutable Data Types
-- An immutable object cannot be changed after creation. 
* `int`
* `float`
* `complex`
* `str`
* `tuple`
* `bool`
* `frozenset`
* `bytes`
* `NoneType`

```
#python code
from numpy import np
print("Hello Govind")
```

| Data Type             | Properties                                                                              |
| --------------------- | --------------------------------------------------------------------------------------- |
| **int**               | Immutable, Numeric Type, Supports Arithmetic Operations, Unlimited Size                 |
| **float**             | Immutable, Numeric Type, Stores Decimal Values, Supports Arithmetic Operations          |
| **complex**           | Immutable, Numeric Type, Contains Real and Imaginary Parts (`a+bj`)                     |
| **bool**              | Immutable, Only `True` and `False`, Subclass of `int`                                   |
| **str**               | Immutable, Ordered, Indexed, Slicable, Iterable, Duplicate Characters Allowed           |
| **list**              | Mutable, Ordered, Indexed, Slicable, Iterable, Duplicates Allowed, Heterogeneous        |
| **tuple**             | Immutable, Ordered, Indexed, Slicable, Iterable, Duplicates Allowed, Heterogeneous      |
| **set**               | Mutable, Unordered, Unindexed, No Slicing, Unique Elements Only, Iterable, Fast Lookup  |
| **frozenset**         | Immutable, Unordered, Unindexed, No Slicing, Unique Elements Only, Hashable             |
| **dict**              | Mutable, Ordered (Python 3.7+), Key-Value Pair, Keys Must Be Unique, Fast Lookup by Key |
| **bytes**             | Immutable, Ordered, Indexed, Slicable, Stores Binary Data (0–255)                       |
| **bytearray**         | Mutable, Ordered, Indexed, Slicable, Stores Binary Data (0–255)                         |
| **range**             | Immutable, Ordered, Indexed, Iterable, Generates Sequence of Numbers Lazily             |
| **NoneType (`None`)** | Immutable, Represents Absence of Value, Singleton Object                                |



| Data Type    | Category | Mutable | Ordered  | Indexed | Duplicate Allowed | Hashable | Iterable | Size Fixed | Example              |
| ------------ | -------- | ------- | -------- | ------- | ----------------- | -------- | -------- | ---------- | -------------------- |
| `int`        | Numeric  | ❌       | ❌        | ❌       | N/A               | ✅        | ❌        | ❌          | `10`                 |
| `float`      | Numeric  | ❌       | ❌        | ❌       | N/A               | ✅        | ❌        | ❌          | `10.5`               |
| `complex`    | Numeric  | ❌       | ❌        | ❌       | N/A               | ✅        | ❌        | ❌          | `3+4j`               |
| `bool`       | Boolean  | ❌       | ❌        | ❌       | N/A               | ✅        | ❌        | ✅          | `True`               |
| `str`        | Sequence | ❌       | ✅        | ✅       | ✅                 | ✅        | ✅        | ❌          | `"Python"`           |
| `list`       | Sequence | ✅       | ✅        | ✅       | ✅                 | ❌        | ✅        | ❌          | `[1,2,3]`            |
| `tuple`      | Sequence | ❌       | ✅        | ✅       | ✅                 | ✅*       | ✅        | ✅          | `(1,2,3)`            |
| `range`      | Sequence | ❌       | ✅        | ✅       | ❌                 | ✅        | ✅        | ✅          | `range(5)`           |
| `set`        | Set      | ✅       | ❌        | ❌       | ❌                 | ❌        | ✅        | ❌          | `{1,2,3}`            |
| `frozenset`  | Set      | ❌       | ❌        | ❌       | ❌                 | ✅        | ✅        | ✅          | `frozenset({1,2,3})` |
| `dict`       | Mapping  | ✅       | ✅ (3.7+) | ❌       | Keys ❌ Values ✅   | ❌        | ✅        | ❌          | `{"a":1}`            |
| `bytes`      | Binary   | ❌       | ✅        | ✅       | ✅                 | ✅        | ✅        | ✅          | `b"abc"`             |
| `bytearray`  | Binary   | ✅       | ✅        | ✅       | ✅                 | ❌        | ✅        | ❌          | `bytearray(b"abc")`  |
| `memoryview` | Binary   | Depends | ✅        | ✅       | ✅                 | ❌        | ✅        | ❌          | `memoryview(b"abc")` |
| `NoneType`   | Special  | ❌       | ❌        | ❌       | N/A               | ✅        | ❌        | ✅          | `None`               |
