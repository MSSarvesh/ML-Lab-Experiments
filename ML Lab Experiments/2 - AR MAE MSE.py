import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
def adjusted_r2(r2, n, p):
    return 1 - ((1 - r2) * (n - 1)) / (n - p - 1)
y_true = np.array([3, 0, 2, 7])
y_pred = np.array([2.5, 0, 2, 8])
r2 = r2_score(y_true, y_pred)
print("R-Squared Error: ",r2)
n = len(y_true)
adj_r2 = adjusted_r2(r2, n, 1)
print("Adjusted RSquared: ",adj_r2)
mae = mean_absolute_error(y_true, y_pred)
print("Mean Absolute Error: ",mae)
mse = mean_squared_error(y_true, y_pred)
print("Mean Squared Error: ",mse)
print("Reg No: 111722202049")