# Regex — Handwritten Notes

## 1. What is Regex?

**Regex (Regular Expression)** is used to find, extract, replace, or validate patterns in text.

```python
import re
```

## 2. `re.search()`

Finds the **first match** of a pattern.

```python
result = re.search(r"Python", text)

if result:
    print("Python found")
```

## 3. `re.findall()`

Finds **all matches** and returns them as a list.

```python
numbers = re.findall(r"\d+", text)
```

Example output:

```text
['4', '12']
```

## 4. Common Regex Patterns

| Pattern | Meaning |
|---|---|
| `\d` | One digit |
| `\d+` | One or more digits |
| `\w` | Word character |
| `\w+` | One or more word characters |
| `\s` | Whitespace |
| `+` | One or more |
| `*` | Zero or more |
| `^` | Start of string |
| `$` | End of string |
| `(...)` | Capture group |

## 5. `re.sub()`

Used to **replace** matching text.

```python
result = re.sub(r"difficult", "powerful", text)
```

## 6. Start and End

```python
re.search(r"^Python", text)   # starts with Python
re.search(r"Python$", text)   # ends with Python
```

Remember:

```text
^Python     → starts with Python
Python$     → ends with Python
```

## 7. Capture Groups

Parentheses create groups.

```python
result = re.search(r"Name: (\w+), Age: (\d+)", text)

print(result.group(1))
print(result.group(2))
```

For `Name: Deven, Age: 25`:

```text
Deven
25
```

## 8. Extracting Emails

```python
emails = re.findall(r"\w+@\w+\.\w+", text)
```

```text
\w+   → username
@      → @ symbol
\w+   → domain
\.     → literal dot
\w+   → extension
```

## 9. Removing Special Characters

```python
result = re.sub(r"[^\w\s]", "", text)
```

This removes characters that are not word characters or whitespace.

## 10. Decimal Numbers

```python
re.findall(r"\d+", "Score: 0.95")
```

returns:

```text
['0', '95']
```

Regex sees the digits on each side of `.` separately. For now, remember this behavior; decimal-number regex is a more advanced pattern.

## Quick Revision

```text
re.search()   → find first match
re.findall()  → find all matches
re.sub()      → replace matches

\d+          → numbers
\w+          → words
\s           → whitespace

^             → start
$             → end
(...)         → group
```

## GenAI Connection

Regex is useful for processing AI-related text, such as:

- extracting IDs
- extracting emails
- finding numbers
- cleaning generated text
- extracting structured information from documents
