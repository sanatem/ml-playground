import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# We create a matrix X with 6 rows and 2 columns
# Each row represents a data point
# Each column represents a feature
# The first column is the x coordinate
# The second column is the y coordinate


X = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])

# Plotting the data points
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.title('Data Points')

# The first 3 rows are labeled 0
# The last 3 rows are labeled 1
y = np.array([0, 0, 0, 1, 1, 1])

lr_model = LogisticRegression()
lr_model.fit(X, y)

# We can now use the model to predict the label of a new data point
y_pred = lr_model.predict(X)

# Plotting the predicted labels
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.title('Predicted Labels')

plt.show()

