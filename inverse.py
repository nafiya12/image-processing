#inverse transformation
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('data/strawberry.jpg')  
if image is None:
    print("Error: Image not found. Please check the file path!")
else:
    inverted_image = 255 - image
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    axes[1].imshow(cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB))
    axes[1].set_title('Inverted Image (255 - pixel_value)')
    axes[1].axis('off')
 plt.show()