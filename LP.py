from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Define the problem
problem = LpProblem("Production_Optimization", LpMaximize)

# Define decision variables
x1 = LpVariable("Product_A", lowBound=0, cat="Continuous")  # Units of Product A
x2 = LpVariable("Product_B", lowBound=0, cat="Continuous")  # Units of Product B

# Objective function
profit = 40 * x1 + 50 * x2
problem += profit, "Total_Profit"

# Constraints
problem += 2 * x1 + x2 <= 100, "Machine_1_Time"
problem += x1 + 2 * x2 <= 80, "Machine_2_Time"

# Solve the problem
status = problem.solve()

# Results
print(f"Status: {problem.status}")
print(f"Optimal Production of Product A: {x1.varValue}")
print(f"Optimal Production of Product B: {x2.varValue}")
print(f"Maximum Profit: ${problem.objective.value()}")