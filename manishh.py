# ============================================
# California Housing Price Prediction from Scratch
# ============================================

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
 
# ================================
# 1. Load Dataset
# ================================
data = fetch_california_housing()
X = data.data
y = data.target.reshape(-1, 1)

print("Data shape:", X.shape)
print("Target shape:", y.shape)

# ================================
# 2. Train-Test Split (80/20)
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ================================
# 3. Feature Scaling (Manual Standardization)
# ================================
X_mean = X_train.mean(axis=0)
X_std = X_train.std(axis=0)

X_train_scaled = (X_train - X_mean) / X_std
X_test_scaled = (X_test - X_mean) / X_std

# Add bias column (1s)
X_train_scaled = np.c_[np.ones((X_train_scaled.shape[0], 1)), X_train_scaled]
X_test_scaled = np.c_[np.ones((X_test_scaled.shape[0], 1)), X_test_scaled]

# ================================
# 4. Initialize Parameters
# ================================
n_features = X_train_scaled.shape[1]
weights = np.random.randn(n_features, 1) * 0.01  # small random values

# ================================
# 5. Define Core Functions
# ================================
def predict(X, weights):
    return np.dot(X, weights)

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def gradient(X, y_true, y_pred):
    return (-2 / X.shape[0]) * np.dot(X.T, (y_true - y_pred))

# ================================
# 6. Training (Gradient Descent)
# ================================
learning_rate = 0.01
epochs = 1000

train_errors = []

for i in range(epochs):
    y_pred = predict(X_train_scaled, weights)
    grad = gradient(X_train_scaled, y_train, y_pred)
    weights -= learning_rate * grad

    error = mse(y_train, y_pred)
    train_errors.append(error)

    if i % 100 == 0:
        print(f"Epoch {i:4d} | MSE: {error:.4f}")

# ================================
# 7. Evaluation
# ================================
y_test_pred = predict(X_test_scaled, weights)

def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1 - (ss_res / ss_tot)

mse_test = mse(y_test, y_test_pred)
r2 = r2_score(y_test, y_test_pred)

print("\nFinal Evaluation on Test Set:")
print(f"MSE: {mse_test:.4f}")
print(f"R² Score: {r2:.4f}")

# ================================
# 8. Visualization: Loss Curve
# ================================
plt.plot(range(epochs), train_errors, color='purple')
plt.title("Training Loss Curve (MSE over Epochs)")
plt.xlabel("Epochs")
plt.ylabel("Mean Squared Error")
plt.grid(True)
plt.show()

# ================================
# 9. Bonus: Relationship Plot (MedInc vs House Value)
# ================================
plt.figure(figsize=(8,6))
plt.scatter(X_train[:, 0], y_train, alpha=0.3, label="Actual Data")
plt.xlabel("Median Income (MedInc)")
plt.ylabel("Median House Value")
plt.title("Median Income vs Median House Value")
plt.legend()
plt.show() 
