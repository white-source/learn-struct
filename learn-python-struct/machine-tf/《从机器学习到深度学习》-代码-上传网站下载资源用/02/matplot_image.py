import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('mantis.png')
print(img)

imgplot = plt.imshow(img)

plt.show()

grey_img = img[:, :, 0]
print(grey_img)


ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3)

ax1.imshow(grey_img, cmap="binary")    # 黑白灰度图
ax2.imshow(grey_img, cmap="winter")    # 蓝绿冷色调
ax3.imshow(grey_img, cmap="Spectral")  # 彩虹谱

ax1.set_title('binary')
ax2.set_title('winter')
ax3.set_title('Spectral')

plt.show()


ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3)

ax1.hist(grey_img.ravel(), bins=8)
ax2.hist(grey_img.ravel(), bins=24)
ax3.hist(grey_img.ravel(), bins=256)

ax1.set_title('bins=8')
ax2.set_title('bins=24')
ax3.set_title('bins=256')

plt.show()



thumb = mpimg.imread('mantis_thumb.png')

ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3)


ax1.imshow(thumb, interpolation="nearest") 
ax2.imshow(thumb, interpolation="bicubic")
ax3.imshow(thumb, interpolation="sinc")

ax1.set_title('nearest')
ax2.set_title('bicubic')
ax3.set_title('sinc')

plt.show()
