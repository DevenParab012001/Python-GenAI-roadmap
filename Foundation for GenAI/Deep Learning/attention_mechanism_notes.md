# Attention Mechanism — Notes

## Roadmap scope

Attention Mechanism is part of Deep Learning Fundamentals.

Covered:
- Attention and token importance
- Attention weights
- Query (Q)
- Key (K)
- Value (V)
- Attention-weighted Values
- Context representation

## 1. What is Attention?

Attention allows a model to focus more on parts of the input that are relevant when interpreting a particular token.

Instead of treating every token as equally important, different tokens can receive different levels of attention.

Example:
"The student studied hard because she had an exam."

When processing "she", the model may give more attention to "student" because it provides relevant context.

## 2. Attention Weight

An attention weight represents how much focus is given to a token for the current context.

Example:
- student → 0.6
- exam → 0.3
- because → 0.1

Total:
0.6 + 0.3 + 0.1 = 1.0

Higher weight means more attention is given to that token.

An attention weight tells us where the model is focusing; it does not by itself prove the final meaning or conclusion.

## 3. Query, Key, and Value

**Query (Q):** What the model is currently looking for.

**Key (K):** Information used to determine how relevant a token is to the Query.

**Value (V):** The information associated with the token that can contribute to the resulting context.

Simple flow:

Query
→ compare with Keys
→ determine attention weights
→ weight the Values
→ combine them
→ context representation

## 4. Attention-Weighted Values

In our simplified examples:

Context = sum(attention weight × Value)

Example:
- student → attention 0.8, Value 10
- exam → attention 0.2, Value 5

Context = (0.8 × 10) + (0.2 × 5)
Context = 8 + 1
Context = 9

A Value with a larger attention weight contributes more strongly.

## 5. End-to-End Example

For the token "she":
- student → attention = 0.7, Value = 8
- exam → attention = 0.3, Value = 4

Total attention = 1.0
Highest attention = student

Context:
(0.7 × 8) + (0.3 × 4) = 5.6 + 1.2 = 6.8

## One-line summary

Attention determines how much focus each token receives; those weights are used to combine Values into a context representation.
