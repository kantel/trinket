import numpy as np
import matplotlib.pyplot as plt

NUM_POINTS = 100
GRADIENT = 0.5

x = np.array(range(NUM_POINTS))
y = np.random.randn(NUM_POINTS)*10 + x*GRADIENT

fig, ax = plt.subplots(figsize = (4, 2))

colors = np.random.rand(NUM_POINTS)
size = (2 + np.random.rand(NUM_POINTS)*8)**2
ax.scatter(x, y, s = size, c = colors, alpha = 0.5)
fig.suptitle("Zufalls-Scatterplot")

plt.show()

# Leerzeile, damit der Plot nicht so am oberen Fensterrand klebt.
print("\n")
