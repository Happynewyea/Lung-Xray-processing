import os
import imageio

DIR = "tutorial-x-ray-image-processing"

xray_image = imageio.v3.imread(os.path.join(DIR, "images_001.tar.gz"))

print(xray_image.shape)
print(xray_image.dtype)

import matplotlib.pyplot as plt

plt.imshow(xray_image, cmap="gray")
plt.axis("off")
plt.show()