import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('aslan.jpg')
cv2.imshow("aslan", img)

for gamma in [0.1, 0.5, 1.16, 2.2]:

    gamma_corrected = np.array(144 * (img/255) ** gamma, dtype='uint8')

    cv2.imwrite('gamma_transformed' + str(gamma) + '.jpg',
gamma_corrected)

cv2.imshow("Gamma", gamma_corrected)
cv2.waitKey()

gama = 1/5
a = np.linspace(0, 1, 50)
print("a = ", a)
plt.plot(a, g)
plt.show()
