import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

x = np.arange(1, 51, 5)
y = x + rng.random(10) * 10

x_avg = np.mean(x)
y_avg = np.mean(y)
sigma_x = np.mean(x**2) - x_avg**2
sigma_y = np.mean(y**2) - y_avg**2
Rxy = np.mean(x*y) - x_avg*y_avg
a = Rxy / sigma_x
b = y_avg - a*x_avg
y_approx = a*x + b

plt.scatter(x, y, color='black')
plt.plot(x, y_approx, color='gray')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
