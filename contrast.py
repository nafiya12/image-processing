#contrast stretching
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('data/strawberry.jpg')  
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(image_rgb)
def contrast_stretch(channel):
    min_pixel = np.min(channel)
    max_pixel = np.max(channel)
    return ((channel - min_pixel) * (255.0 / (max_pixel - min_pixel))).astype(np.uint8)
r_stretched = contrast_stretch(r)
g_stretched = contrast_stretch(g)
b_stretched = contrast_stretch(b)
stretched_image = cv2.merge([r_stretched, g_stretched, b_stretched])
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
axes[0].imshow(image_rgb)
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(stretched_image)
axes[1].set_title('Contrast-Stretched Image')
axes[1].axis('off')
plt.show()