import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
imgd= ''
image = mpimg.imread(imgd)
print(plt.imread(imgd).shape)
pts = np.array([[0,0],[775,336],[775+254,336+2270]])

plt.imshow(image)
#plt.plot(640, 570, "og", markersize=10)  # og:shorthand for green circle
plt.scatter(pts[:, 0], pts[:, 1], marker="x", color="red", s=200)
plt.show()

