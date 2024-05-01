# 6. Exploring Logical Operations and Precedence

# Objective: The aim of this assignment is to grasp the concept of logical operations 
# and understand how operator precedence can affect the outcome of an operation.

# Task 1: Validating Calculations
# Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. 
# Compare the two results to see if they match.
x = 10
y = 100
z = 2
t = y - x * z
print(t)

# adding parentheses and compare with previous t value
t = (y-x) * z
print(t)

print("The value has changed for the first t value from 80 to 180 when parentheses was added since Parentheses have the highest precedence")



# Task 2: Mix and Match
# Combine arithmetic (+), logical (or), and comparison (>) operators in a single expression and predict the outcome. 
# Then, compute the expression to see if the prediction was correct.
x = 20
y = 40
z = 60
total = x + (y or x) + (z > x)

print("Prediction : I believe that it may return an ERROR Message.")

print("Actual Result below")

print(total)

