# Import PuLP
from pulp import *

# Create the optimization problem
model = LpProblem("Profit_Maximization", LpMaximize)

# Decision variables
x = LpVariable('Product_A', lowBound=0)
y = LpVariable('Product_B', lowBound=0)

# Objective function
model += 40 * x + 30 * y, "Total_Profit"

# Constraints
model += 2 * x + 1 * y <= 100, "Machine_Hours_Constraint"

# Solve the model
model.solve()

# Results
print("Status:", LpStatus[model.status])
print("Units of Product A:", x.varValue)
print("Units of Product B:", y.varValue)
print("Maximum Profit:", value(model.objective))
