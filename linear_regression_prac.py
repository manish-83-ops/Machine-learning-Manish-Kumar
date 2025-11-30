import numpy as np


x = np.array([1, 2, 3], dtype=float)
y = np.array([2, 4, 6], dtype=float)

m = 0
c = 0
lr = 0.1


for i in range(1000):
    y_pred = m * x + c
    m = m - lr * np.mean((y_pred - y) * x)
    c = c - lr * np.mean(y_pred - y)

print("m =", m)
print("c =", c)