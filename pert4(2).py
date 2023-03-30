import matplotlib.pyplot as plt

from skimage import data
from skimage.filters import threshold_otsu
from skimage.filters import threshold_minimum
from skimage.filters import threshold_mean

image = data.camera()
treshmin = threshold_minimum(image)
print("Treshold minimum: ", treshmin)
minimumImage = image > treshmin

treshmean = threshold_mean(image)
print("Treshold mean: ", treshmean)
meanImage = image > treshmean

fig, axes = plt.subplots(3 , 2, figsize=(10,10)) #mengatur tampilan gambar(size)
ax = axes.ravel ()

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title("original")
ax[1].hist(image.ravel(), bins=256)
ax[1].set_title("Histogram image")

ax[2].imshow(minimumImage, cmap=plt.cm.gray)
ax[2].set_title("Treshold minimum")
ax[3].hist(image.ravel(), bins=256)
ax[3].set_title("Histogram image")

ax[4].imshow(meanImage, cmap=plt.cm.gray)
ax[4].set_title("Treshold Mean")
ax[5].hist(image.ravel(), bins=256)
ax[5].set_title("Histogram image")

plt.tight_layout()
plt.show()