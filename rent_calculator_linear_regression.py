import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Given data
quarters = np.array([1, 2, 3, 4, 5])  # 23Q1, 23Q2, 23Q3, 23Q4, 24Q1
values = np.array([120000, 154000, 205328, 229000, 380000])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(quarters, values)

# Predict the value for 24Q2 (Quarter 6)
next_quarter = 6
predicted_value = slope * next_quarter + intercept

print(f"Predicted value for 24Q2: {predicted_value:.2f}")

# Plotting the data and the regression line
plt.scatter(quarters, values, color='blue', label='Actual values')
plt.plot(quarters, slope * quarters + intercept, color='red', label='Regression line')
plt.scatter(next_quarter, predicted_value, color='green', label='Predicted value for 24Q2')
plt.xlabel('Quarter')
plt.ylabel('Value')
plt.legend()
plt.title('Linear Regression Prediction')
plt.grid(True)
plt.show()

