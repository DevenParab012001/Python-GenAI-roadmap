# Attention Mechanism - Practice

# Attention weights
weights = {"student": 0.6, "exam": 0.3, "because": 0.1}
print("Total attention:", sum(weights.values()))
print("Highest attention:", max(weights, key=weights.get))

# Attention-weighted Values
attention = {"student": 0.8, "exam": 0.2}
values = {"student": 10, "exam": 5}
context = sum(attention[token] * values[token] for token in attention)
print("Attention-weighted context:", context)

# Second example
attention = {"Token A": 0.3, "Token B": 0.7}
values = {"Token A": 4, "Token B": 8}
context = sum(attention[token] * values[token] for token in attention)
print("Second context:", context)

# End-to-end example
attention = {"student": 0.7, "exam": 0.3}
values = {"student": 8, "exam": 4}
print("Total attention:", sum(attention.values()))
print("Most attended token:", max(attention, key=attention.get))
context = sum(attention[token] * values[token] for token in attention)
print("Final context:", context)
