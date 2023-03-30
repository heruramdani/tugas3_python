#import library
import matplotlib.pyplot as plt
#%matplotib inline

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray

original = data.chelsea()
print(original.shape)
plt.imshow(original)
plt.show()

red = original[:, :, 0]
green = original[:, :, 1]
blue = original[:, :, 2]

print("red.shape : ", red.shape)
print("green.shape : ", green.shape)
print("blue.shape : ", blue.shape)

fig, axes = plt.subplots(2 , 2, figsize=(10,10))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title("Citra Imput")

ax[1].imshow(red, cmap=plt.cm.gray)
ax[1].set_title("Red Channel")

ax[2].imshow(green, cmap=plt.cm.gray)
ax[2].set_title("Green Channel")

ax[3].imshow(blue, cmap=plt.cm.gray)
ax[3].set_title("Blue Channel")

fig.tight_layout()
plt.show()

#mengubah warna
red = original.copy()
red[:,:,1]=0
red[:,:,2]=0
print("Red Shape: ",red.shape)

green = original.copy()
green[:,:,0]=0
green[:,:,2]=0
print("Green Shape:", green.shape)

blue= original.copy()
blue[:,:,0]=0
blue[:,:,1]=0
print("Blue Shape:",blue.shape)

fig,axes = plt.subplots(2 , 2,figsize=(10,10))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title("Original")

ax[1].imshow(red)
ax[1].set_title("Red channel")

ax[2].imshow(green)
ax[2].set_title("Green channel")

ax[3].imshow(blue)
ax[3].set_title("Blue channel")

fig.tight_layout()
plt.show()