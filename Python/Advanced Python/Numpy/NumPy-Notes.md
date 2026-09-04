# NumPy — Handwritten Notes

## 1. What is NumPy?

NumPy is a Python library used for working with numerical data and arrays.

```python
import numpy as np
```

---

## 2. Creating Arrays

### `np.array()`

Creates an array from a Python list.

```python
arr = np.array([10, 20, 30, 40, 50])
```

### `np.arange()`

Creates evenly spaced values using a start, stop, and step.

```python
arr = np.arange(1, 11)
```

The stop value is excluded.

### `np.linspace()`

Creates a specified number of evenly spaced values between two limits.

```python
arr = np.linspace(0, 1, 5)
```

---

## 3. Indexing and Slicing

NumPy arrays use zero-based indexing.

```python
arr[0]       # first element
arr[-1]      # last element
arr[1:4]     # elements from index 1 to 3
```

---

## 4. Reshaping Arrays

`reshape()` changes the shape of an array without changing its values.

```python
arr = np.arange(1, 7)
matrix = arr.reshape(2, 3)
```

There must be the same total number of elements before and after reshaping.

Example:

```text
6 elements → 2 × 3 = 6
```

If the sizes do not match, NumPy raises `ValueError`.

---

## 5. Vectorized Computations

NumPy allows operations directly on entire arrays.

```python
marks = np.array([70, 80, 90])

marks + 5
marks * 2
marks - 10
marks / 2
```

No explicit Python loop is required for these element-wise operations.

---

## 6. Mathematical Functions

### Sum

```python
np.sum(arr)
```

### Mean

```python
np.mean(arr)
```

### Standard Deviation

```python
np.std(arr)
```

### Dot Product

```python
np.dot(a, b)
```

### Common combination

```python
total = np.sum(arr)
average = np.mean(arr)
spread = np.std(arr)
```

---

## 7. Broadcasting

Broadcasting allows NumPy to perform operations between arrays and compatible scalar/array shapes.

Example:

```python
marks = np.array([70, 80, 90])
marks = marks + 5
```

The `5` is applied to every element:

```text
[70, 80, 90]
       ↓
[75, 85, 95]
```

Broadcasting also works with compatible multi-dimensional arrays.

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

matrix + 10
```

---

## 8. Multi-Dimensional Arrays

A 2D NumPy array can represent a matrix.

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

Indexing can use row and column positions:

```python
matrix[0, 1]
```

This accesses row `0`, column `1`.

---

## Quick Revision

| Concept | Main Function / Syntax |
|---|---|
| Create array | `np.array()` |
| Sequence | `np.arange()` |
| Evenly spaced values | `np.linspace()` |
| Index | `arr[index]` |
| Slice | `arr[start:stop]` |
| Reshape | `arr.reshape(rows, cols)` |
| Sum | `np.sum()` |
| Average | `np.mean()` |
| Standard deviation | `np.std()` |
| Dot product | `np.dot()` |
| Broadcasting | `array + scalar` |

## NumPy Roadmap Status

Completed:

- Array creation: `array`, `arange`, `linspace`
- Indexing and slicing
- Reshaping
- Vectorized computations
- Mathematical functions: `mean`, `sum`, `std`, `dot`
- Broadcasting
- Multi-dimensional data
