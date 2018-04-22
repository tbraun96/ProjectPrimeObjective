import cv2

import numpy as np

def rasterTo1DArray(filename):
    img = cv2.imread(filename)
    height, width, channels = img.shape
    oneDimArray = [None] * height * width

    n = 0
    print("image: ", width, "x", height)
    for y in range(0, height):
        for x in range(0, width):
            oneDimArray[n] = img[y][x][0] + img[y][x][1] + img[y][x][2]
            n += 1

    return np.atleast_1d(np.linalg.norm(oneDimArray, 2, -1))
