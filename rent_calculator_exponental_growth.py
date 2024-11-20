import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data
quarters = np.array([1, 2, 3, 4, 5])  # 23Q1, 23Q2, 23Q3, 23Q4, 24Q1, 24Q2
values = np.array([120000, 154000, 205328, 229000, 380000])

# Define the form of the function we want to fit to our data.
def exponential_func(x, a, b, c):
    return a * np.exp(b * x) + c

# Perform curve fitting
popt, pcov = curve_fit(exponential_func, quarters, values)

# Predict the value for 24Q2 (Quarter 6)
next_quarter = 6
predicted_value = exponential_func(next_quarter, *popt)

print(f"Predicted value for 24Q2: {predicted_value:.2f}")

# Plotting the data and the regression line
plt.scatter(quarters, values, color='blue', label='Valores reales')
plt.plot(quarters, exponential_func(quarters, *popt), color='red', label='Curva de regresión')
plt.scatter(next_quarter, predicted_value, color='green', label='Valor predicho para proximo cuatrimestre')
plt.xlabel('Cuatrimestre')
plt.ylabel('Valor')
plt.legend()
plt.title(f"Predicción del alquiler para el siguiente cuatrimestre: ${predicted_value:.2f}")
plt.grid(True)
plt.show()
