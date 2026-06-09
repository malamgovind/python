# File Handling in Python

## What is File Handling?

File Handling is used to:

- Create Files
- Read Files
- Write Files
- Append Data
- Delete Files

## Why File Handling?

Data permanently store કરવા માટે.

Example:

- student.txt
- notes.txt
- data.csv
- config.json

## File Modes

| Mode | Description |
|------|-------------|
| r | Read |
| w | Write |
| a | Append |
| x | Create |
| rb | Read Binary |
| wb | Write Binary |

## Basic Syntax

```python
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
```

## Recommended Syntax

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

## Important Functions

- open()
- read()
- readline()
- readlines()
- write()
- close()
- seek()
- tell()

## Modules Used

- os
- csv
- json

