# 🎬 Movie Night Recommender

> **Python Roadmap — Project 3**

A console-based movie recommendation program that recommends movies based on a user's selected genre.

The roadmap describes this project as a simple rule-based recommender using genre preferences, filtering logic, and user input handling.

## 🎯 Roadmap Requirement

The SDE Master Program PDF specifies:

- Recommend movies based on genre preferences.
- Use simple rule-based logic and conditional checks.
- Practice data types, filtering logic, and user input handling.

## 🧱 Movie Data

The program stores movies in a dictionary:

```python
movies = {
    "Action": ["John Wick", "The Dark Knight", "Mad Max: Fury Road"],
    "Comedy": ["The Hangover", "Superbad", "3 Idiots"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"],
    "Horror": ["The Conjuring", "Get Out", "A Quiet Place"]
}
```

The genre is the key and the movie list is the value.

## 🔎 Genre Selection

The program displays the available genres and lets the user select one by number.

```python
genres = list(movies.keys())
```

`enumerate()` is used to display numbered choices.

The selected number is converted to the corresponding genre:

```python
return genres[choice - 1]
```

## 🎬 Movie Recommendation

Once a genre is selected, its movie list is retrieved:

```python
recommended_movies = movies[genre]
```

The movies are then displayed to the user.

## 🎲 Extra: Random Recommendation

An additional feature was added using Python's `random` module:

```python
movie = random.choice(movies[genre])
```

This randomly selects one movie from the chosen genre.

**This random recommendation is an extra implementation feature, not a separate roadmap requirement.**

## 🔁 Extra: Repeat Recommendations

The program allows the user to request another recommendation.

```text
Would you like another recommendation? (yes/no):
```

The program continues when the user enters `yes` or `y` and exits when the user enters `no` or `n`.

## 🛡️ Input Validation

The implementation also validates:

- Whether the genre choice is a number.
- Whether the number is within the available range.
- Whether the repeat choice is `yes`/`y` or `no`/`n`.

These are implementation extras that make the console experience more robust.

## 🧠 Concepts Used

- Dictionary
- Lists
- `input()`
- String `.strip()`
- String `.lower()`
- `if / elif / else`
- `while` loops
- `for` loops
- `enumerate()`
- Functions
- `return`
- List indexing
- `random.choice()`

## 🔄 Program Flow

```text
Start
  ↓
Display genres
  ↓
User selects genre
  ↓
Validate selection
  ↓
Display movies
  ↓
Select random movie
  ↓
Ask whether to continue
  ↓
Yes → Show genres again
No  → Exit
```

## 🧪 Example

```text
========== MOVIE NIGHT RECOMMENDER ==========

Available genres:
1. Action
2. Comedy
3. Sci-Fi
4. Horror

Enter your choice: 3

🎬 Recommended Sci-Fi Movies
---------------------------------------------
1. Interstellar
2. Inception
3. The Matrix

🎲 Tonight's Random Pick
---------------------------------------------
🎬 Inception
```

## ✅ Completion Checklist

- [x] Store movies by genre
- [x] Accept user genre selection
- [x] Validate user input
- [x] Recommend movies for selected genre
- [x] Use conditional logic
- [x] Display recommendations
- [x] Random recommendation — extra
- [x] Repeat recommendation flow — extra

## 📌 Core Idea

```text
Genre Preference
       ↓
Dictionary Lookup
       ↓
Matching Movie List
       ↓
Recommendation
```
