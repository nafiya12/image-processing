#histogram equalization
import cv2
from matplotlib import pyplot as plt
from PIL import Image
image = cv2.imread('data/flower.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized_gray = cv2.equalizeHist(gray)
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(gray, cmap='gray')
axes[0].set_title('Original Grayscale')
axes[0].axis('off')
axes[1].imshow(equalized_gray, cmap='gray')
axes[1].set_title('Equalized Grayscale')
axes[1].axis('off')
plt.show()