import cv2


def rasterTo1DArray(filename):
    img = cv2.imread(filename)
    height, width, channels = img.shape
    oneDimArray = [None] * height * width

    n = 0
    largest = 0
    print("image: ", width, "x", height)
    for y in range(0, height):
        for x in range(0, width):
            oneDimArray[n] = img[y][x][0] + img[y][x][1] + img[y][x][2]
            if (img[y][x][0] + img[y][x][1] + img[y][x][2] > largest): largest = img[y][x][0] + img[y][x][1] + \
                                                                                 img[y][x][2]
            n += 1

    print("input sample data", oneDimArray[0:10])
    print("input sample normed data", oneDimArray[0:10] / largest)
    return oneDimArray / largest
