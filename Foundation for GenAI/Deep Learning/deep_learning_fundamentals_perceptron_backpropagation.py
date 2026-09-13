# Deep Learning Fundamentals practice
# Perceptron, Backpropagation and Optimization

# Perceptron
x1, x2 = 0.8, 0.6
w1, w2 = 0.7, 0.3
bias = -0.2
threshold = 0.5

z = (x1 * w1) + (x2 * w2) + bias
output = 1 if z >= threshold else 0

print("Perceptron")
print("Weighted sum:", z)
print("Output:", output)

# Simple weight adjustment
old_weight = 0.7
adjustment = -0.1
new_weight = old_weight + adjustment
print("\nWeight update:", new_weight)

# Gradient descent
old_weight = 0.8
gradient = 0.5
learning_rate = 0.1
new_weight = old_weight - (learning_rate * gradient)
print("Gradient descent update:", new_weight)

# Learning-rate example
old_weight = 1.0
gradient = 0.4
learning_rate = 0.2
new_weight = old_weight - (learning_rate * gradient)
print("Learning-rate example:", new_weight)

# Learning loop:
# Prediction -> Error -> Backpropagation -> Gradient
# -> Optimization -> Weight Update
