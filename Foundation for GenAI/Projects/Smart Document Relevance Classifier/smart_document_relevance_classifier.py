# Project 8 — Smart Document Relevance Classifier
# Simple Attention Mechanism Demonstration

sentence = "The dog is chasing the ball"
tokens = sentence.split()

attention_weights = {
    "The": 0.05,
    "dog": 0.25,
    "is": 0.05,
    "chasing": 0.35,
    "the": 0.05,
    "ball": 0.25
}

token_values = {
    "The": 0.2,
    "dog": 0.8,
    "is": 0.1,
    "chasing": 0.9,
    "the": 0.2,
    "ball": 0.7
}

# Validate data
if len(tokens) != len(attention_weights):
    raise ValueError("Every token must have an attention weight.")

if len(tokens) != len(token_values):
    raise ValueError("Every token must have a numerical value.")

for token in tokens:
    if token not in attention_weights:
        raise ValueError(f"Missing attention weight for token: {token}")
    if token not in token_values:
        raise ValueError(f"Missing value for token: {token}")
    if not 0 <= attention_weights[token] <= 1:
        raise ValueError(
            f"Attention weight for '{token}' must be between 0 and 1."
        )

total_attention = sum(attention_weights[token] for token in tokens)

print("=" * 65)
print("SMART DOCUMENT RELEVANCE CLASSIFIER")
print("=" * 65)
print(f"\nSentence: {sentence}")

print("\n" + "=" * 65)
print("TOKEN INFORMATION")
print("=" * 65)
print(f"{'Token':<12}{'Attention':<15}{'Value':<15}{'Contribution':<15}")
print("-" * 65)

for token in tokens:
    attention = attention_weights[token]
    value = token_values[token]
    contribution = attention * value
    print(
        f"{token:<12}{attention:<15.2f}"
        f"{value:<15.2f}{contribution:<15.4f}"
    )

print("\n" + "=" * 65)
print("ATTENTION WEIGHT VALIDATION")
print("=" * 65)
print(f"Total attention weight: {total_attention:.2f}")

if abs(total_attention - 1.0) < 1e-9:
    print("✓ Attention weights sum to 1.0")
else:
    print("✗ Attention weights do not sum to 1.0")

most_important_token = max(
    tokens, key=lambda token: attention_weights[token]
)
highest_attention = attention_weights[most_important_token]

print("\n" + "=" * 65)
print("MOST IMPORTANT TOKEN")
print("=" * 65)
print(f"Token: {most_important_token}")
print(f"Attention: {highest_attention:.2f}")

context_value = sum(
    attention_weights[token] * token_values[token]
    for token in tokens
)

print("\n" + "=" * 65)
print("WEIGHTED CONTEXT")
print("=" * 65)
print("Context = Σ(attention × value)")
print(f"\nWeighted context value: {context_value:.4f}")

print("\n" + "=" * 65)
print("FINAL SUMMARY")
print("=" * 65)
print(f"Sentence              : {sentence}")
print(f"Number of tokens      : {len(tokens)}")
print(f"Attention weight total: {total_attention:.2f}")
print(f"Most important token  : {most_important_token}")
print(f"Highest attention     : {highest_attention:.2f}")
print(f"Context value         : {context_value:.4f}")
