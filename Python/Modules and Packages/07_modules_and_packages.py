# Python — Modules & Packages
# Practice Solutions

# Q1 — Standard Library
import math
print(math.sqrt(144))
print(math.pow(5, 3))
print(math.ceil(4.2))
print(math.floor(4.8))

# Q2 — Specific Imports
from math import sqrt, ceil, floor
print(sqrt(144))
print(ceil(4.2))
print(floor(4.8))

# Q3-Q7 — These exercises require separate files/modules.
# See Modules-and-Packages.md for the required structures and solutions.

# Q8 — Why imports?
# Importing a function allows us to write the code once and reuse it
# wherever we need it. If we change the function later, we only need
# to update it in one place instead of updating copied versions.
