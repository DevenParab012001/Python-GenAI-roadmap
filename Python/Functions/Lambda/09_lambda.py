# Python — Lambda Functions
# Practice Solutions

# Q1
square = lambda number: number ** 2
print(square(5))

# Q2
add = lambda a, b: a + b
print(add(2, 3))

# Q3
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))
print(result)

# Q4
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

# Q5
users = [
    {"name": "Deven", "age": 25},
    {"name": "Rahul", "age": 30},
    {"name": "Amit", "age": 22}
]
users.sort(key=lambda user: user["age"])
print(users)

# Q6
products = [
    {"name": "Laptop", "price": 70000},
    {"name": "Mouse", "price": 1500},
    {"name": "Monitor", "price": 15000}
]
products.sort(key=lambda product: product["price"])
print(products)
