import numpy as np
from scipy.optimize import linprog

# Define the piecewise linear function
def piecewise_linear(x, breakpoints, slopes, intercepts):
    return np.piecewise(x, [x < breakpoints[0], x >= breakpoints[-1]],
                        [lambda x: slopes[0]*x + intercepts[0]] +
                        [lambda x, i=i: (slopes[i]-slopes[i-1])*x + (intercepts[i]-intercepts[i-1]) + slopes[i-1]*breakpoints[i] for i in range(1, len(breakpoints))] +
                        [lambda x: slopes[-1]*x + intercepts[-1]])

# Define the breakpoints, slopes, and intercepts for the piecewise linear function
breakpoints = np.array([2, 5, 7])
slopes = np.array([1, 2, 3, 4])
intercepts = np.array([0, 1, 3, 6])

# Define the coefficients of the linear objective function
c = np.array([2, 3, 4])

# Define the bounds for the decision variables
bounds = [(0, None)] * len(c)

# Define the inequality constraints
A = np.array([[1, 1, 1],
              [-1, 2, 0]])
b = np.array([10, 2])

# Solve the piecewise linear program
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds)

# Extract the optimal solution
x_opt = result.x
optimal_value = result.fun

print("Optimal Solution:", x_opt)
print("Optimal Value:", optimal_value)
