import cv2
from normalize_easy import normv


def rasterTo1DArray(filename):
    img = cv2.imread(filename)
    height, width, channels = img.shape
    oneDimArray = []
    n = 0
    for y in range(0, height):
        for x in range(0, width):
            oneDimArray[n] = img[x][y][0] + img[x][y][1] + img[x][y][2]
            n += 1

    return normv(oneDimArray)
