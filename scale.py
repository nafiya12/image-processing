import cv2
import matplotlib.pyplot as plt
img = cv2.imread("data/strawberry.jpg")
newImg = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
fig, axes = plt.subplots(1, 2, figsize=(6, 3))
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('on')
axes[1].imshow(cv2.cvtColor(newImg, cv2.COLOR_BGR2RGB))
axes[1].set_title('Scaled Image')
axes[1].axis('on')
plt.show()
