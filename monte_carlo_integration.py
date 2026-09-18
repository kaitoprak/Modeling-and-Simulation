import random
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Task 1: Numerical Solution
# ==========================================

# Initialize PRNG
random.seed(2)

# Define the function
def f(x):
    return x**2

# Integration limits
a = 0.0
b = 3.0

# Number of steps
num_steps = 1_000_000

# Generate x-values for plotting
x_values = np.linspace(a, b, num_steps)

# Calculate function values
y_values = f(x_values)

print("Function: f(x) = x^2")
print("Lower limit (a):", a)
print("Upper limit (b):", b)
print("Number of steps:", num_steps)


# ==========================================
# Task 2: Min-Max Detection
# ==========================================

# Initialize ymin and ymax
ymin = f(x_values[0])
ymax = f(x_values[0])

# Iterate through x-values
for x in x_values:
    y = f(x)

    if y < ymin:
        ymin = y

    if y > ymax:
        ymax = y

print("\nMin-Max Detection")
print("ymin:", ymin)
print("ymax:", ymax)


# ==========================================
# Task 3: Monte Carlo Method
# ==========================================

# Calculate the area of the bounding rectangle
area = (b - a) * (ymax - ymin)

# Monte Carlo parameters
N = 1_000_000
M = 0

# Lists to store random points
x_random = []
y_random = []

# Generate random points
for _ in range(N):
    x = random.uniform(a, b)
    y = random.uniform(ymin, ymax)

    x_random.append(x)
    y_random.append(y)

    # Check if the point is under the curve
    if y <= f(x):
        M += 1

# Calculate numerical integral
numerical_integral = (M / N) * area

print("\nMonte Carlo Method")
print("Bounding area:", area)
print("Total random points (N):", N)
print("Points under the curve (M):", M)
print("Numerical integral:", numerical_integral)


# ==========================================
# Task 4: Visualization
# ==========================================

# Separate points under and outside the curve
x_under = []
y_under = []

x_outside = []
y_outside = []

for x, y in zip(x_random, y_random):
    if y <= f(x):
        x_under.append(x)
        y_under.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot function curve
plt.plot(
    x_values,
    y_values,
    color='red',
    label='f(x) = x²'
)

# Plot points under the curve
plt.scatter(
    x_under,
    y_under,
    color='blue',
    s=1,
    label='Under the curve'
)

# Plot points outside the curve
plt.scatter(
    x_outside,
    y_outside,
    color='yellow',
    s=1,
    label='Outside the curve'
)

# Labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Monte Carlo Simulation for Numerical Integration')

# Legend and grid
plt.legend()
plt.grid(True)

# Display plot
plt.show()