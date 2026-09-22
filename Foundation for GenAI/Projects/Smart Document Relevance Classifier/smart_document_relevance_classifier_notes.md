# Project 8 — Smart Document Relevance Classifier

## Purpose

The SDE Master Program PDF defines Project 8 as:

> Compute attention weights on simple sentences to understand token importance during context interpretation.

This project is a simple attention-mechanism demonstration.

## Input

Sentence:

```text
The dog is chasing the ball
```

The sentence is split into tokens using `split()`.

## Attention Weights

| Token | Attention |
|---|---:|
| The | 0.05 |
| dog | 0.25 |
| is | 0.05 |
| chasing | 0.35 |
| the | 0.05 |
| ball | 0.25 |

The weights add up to `1.00`.

Higher attention means greater focus in this demonstration.

## Token Values

| Token | Value |
|---|---:|
| The | 0.2 |
| dog | 0.8 |
| is | 0.1 |
| chasing | 0.9 |
| the | 0.2 |
| ball | 0.7 |

These are simple numerical values used only for the project demonstration.

## Most Important Token

The program finds the token with the highest attention weight.

```text
chasing → 0.35
```

## Weighted Context

The project uses the simplified formula:

```text
Context = Σ(attention_i × value_i)
```

For each token:

```text
contribution = attention × value
```

The contributions are then summed.

Calculation:

```text
(0.05 × 0.2) +
(0.25 × 0.8) +
(0.05 × 0.1) +
(0.35 × 0.9) +
(0.05 × 0.2) +
(0.25 × 0.7)

= 0.7150
```

Therefore:

```text
Weighted context value = 0.7150
```

## Validation

The program checks:

- Number of tokens matches attention weights.
- Number of tokens matches token values.
- Every token has an attention weight.
- Every token has a numerical value.
- Every attention weight is between 0 and 1.
- Total attention weight equals 1.0.

## Python Concepts Used

- Variables
- Strings
- Lists
- Dictionaries
- `split()`
- `for` loops
- `sum()`
- `max()`
- Lambda function
- `if/else`
- `ValueError`
- Basic arithmetic
- Formatted strings

## Output

The program displays:

- Input sentence
- Token information
- Attention weights
- Token values
- Individual contributions
- Attention-weight validation
- Most important token
- Weighted context value
- Final summary

## Scope

This is a simplified Project 8 demonstration based on the PDF. It does not implement a production Transformer attention layer or train a neural network.
