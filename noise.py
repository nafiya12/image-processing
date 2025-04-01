#noise removal
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("./data/a.jpg")  
img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(img_ycrcb)
y_denoised = cv2.GaussianBlur(y, (5, 5), 0)
img_denoised = cv2.merge((y_denoised, cr, cb))
img_denoised = cv2.cvtColor(img_denoised, cv2.COLOR_YCrCb2BGR)
fig, axes = plt.subplots(1, 2, figsize=(20, 5))
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(cv2.cvtColor(img_denoised, cv2.COLOR_BGR2RGB))
axes[1].set_title('Noise Removed')
axes[1].axis('off')
plt.show()