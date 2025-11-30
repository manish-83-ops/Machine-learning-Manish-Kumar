import numpy as np
import matplotlib.pyplot as plt 

x = np.array([1, 2, 3,6,89,45,67], dtype=float)
y = np.array([2, 4, 6,9,10,53,76], dtype=float)
x=x.reshape(-1,1)
x_bias = np.c_[np.ones((x.shape[0], 1)), x]
XtX = x_bias.T.dot(x_bias)
theta = np.linalg.inv(XtX).dot(x_bias.T).dot(y)
print(theta)
c = theta[0]
m = theta[1]
 
plt.plot(x,y,'o',label='Data points')
x_line = np.linspace(min(x), max(x), 100)
y_line = m * x_line + c

# Plot
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_line, y_line, color='red', label=f'Line: y = {m:.2f}x + {c:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.legend()
plt.grid(True)
plt.show()