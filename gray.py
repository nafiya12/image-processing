#binary and grayscale
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("data/strawberry.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
fig, axes = plt.subplots(1, 3, figsize=(20, 5))
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(gray, cmap='gray')
axes[1].set_title('Grayscale')
axes[1].axis('off')
axes[2].imshow(binary_img, cmap='gray')
axes[2].set_title('Binary')
axes[2].axis('off')
plt.show()
