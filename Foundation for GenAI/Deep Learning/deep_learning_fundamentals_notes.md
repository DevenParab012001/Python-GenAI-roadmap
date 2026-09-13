# Deep Learning Fundamentals — Perceptron & Backpropagation

## Roadmap scope
- Perceptron
- Backpropagation and Optimization

## Perceptron
A perceptron is a simple model that makes a decision from inputs.

Weighted sum:
`z = sum(w_i * x_i) + b`

- `x` = input
- `w` = weight
- `b` = bias
- `z` = weighted sum

Threshold:
- If `z >= threshold` → output `1`
- If `z < threshold` → output `0`

A larger weight gives an input more influence.

Bias is added to the weighted sum and shifts the result before the threshold decision.

Flow:
Input → Weights → Weighted Sum + Bias → Threshold → Output

## Backpropagation
When a neural network makes an error, backpropagation works backward through the network to determine how the error relates to the weights and how they should change.

## Optimization
Optimization improves the model's weights with the goal of reducing error.

A common approach is gradient descent.

`w_new = w_old - learning_rate * gradient`

- Learning rate controls the size of the update.
- Very small learning rate → learning can be slow.
- Very large learning rate → large steps can overshoot and may prevent convergence.

## Learning loop
1. Make a prediction.
2. Calculate the error.
3. Use backpropagation to determine how the error relates to the weights.
4. Obtain the gradient.
5. Use optimization such as gradient descent.
6. Update the weights.
7. Repeat.

**Summary:** Backpropagation determines how the error affects the weights; optimization uses that information to update the weights and reduce error.
