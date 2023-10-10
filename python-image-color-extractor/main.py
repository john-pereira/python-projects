from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

image = mpimg.imread('bg5.jpg')
w, h, d = tuple(image.shape)
pixels = np.reshape(image, (w * h, d))

n_colors = 10
model = KMeans(n_clusters=n_colors, random_state=42, n_init=10).fit(pixels)
palette = np.uint8(model.cluster_centers_)

plt.imshow([palette])
plt.show()
