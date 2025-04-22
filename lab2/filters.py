import numpy as np
import cv2

img = cv2.imread('artur.jpg')

# mean_3x3 = (1/9) * np.array([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ])

kernel = (1/16) * np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])

mean_5x5 = (1/25) * np.ones((5, 5))

mean_7x7 = (1/49) * np.ones((7, 7))

gauss_5x5 = (1/273) * np.array([
    [1,  4,  7,  4, 1],
    [4, 16, 26, 16, 4],
    [7, 26, 41, 26, 7],
    [4, 16, 26, 16, 4],
    [1,  4,  7,  4, 1]
])

gauss_7x7 = (1/1003) * np.array([
    [0,   0,   1,   2,   1,  0,  0],
    [0,   3,  13,  22,  13,  3,  0],
    [1,  13,  59,  97,  59, 13,  1],
    [2,  22,  97, 159,  97, 22,  2],
    [1,  13,  59,  97,  59, 13,  1],
    [0,   3,  13,  22,  13,  3,  0],
    [0,   0,   1,   2,   1,  0,  0]
])

kernel_sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])


kernel_sobel_y = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])


kernel_roberts_x = np.array([
    [1, 0], [0, -1]
])

kernel_roberts_y = np.array([
    [0, -1], [1, 0]
])


lap_a = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

lap_b = np.array([
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]
])

lap_c = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
])

lap_d = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1,-1, -1]
])


filtered = cv2.filter2D(img, -1, lap_d)

cv2.imwrite('filtered.jpg', filtered)