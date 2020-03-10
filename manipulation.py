a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def rotate_right(image):
    n = len(image) - 1
    for i in range(0, len(image) - 1):
        for j in range(0, (len(image) - i) - 1):
            image[n - j][n - i], image[i][j] = image[i][j], image[n - j][n - i]

    for i in range(0, len(image) // 2):
        for j in range(0, len(image)):
            image[n - i][j], image[i][j] = image[i][j], image[n - i][j]

    return image


def rotate_left(image):
    n = len(image) - 1
    for i in range(0, len(image) - 1):
        for j in range(0, (len(image) - i) - 1):
            image[i][n - j], image[n - j][i] = image[n - j][i], image[i][n - j]

    for i in range(0, len(image) // 2):
        for j in range(0, len(image)):
            image[n - i][j], image[i][j] = image[i][j], image[n - i][j]

    return image


d = [[(155, 100, 15), (10, 10, 10), (100, 100, 90)], [(200, 15, 115), (140, 130, 120), (50, 60, 70)],
     [(100, 155, 15), (30, 120, 150), (45, 15, 90)]]
h = [[(100, 155, 15)]]


def invert(image):
    inverted_image = []
    i = 0
    for row in image:
        for r, g, b in row:
            current_pixel = (255 - r, 255 - g, 255 - b)
            if len(inverted_image) <= i:
                inverted_image.append([current_pixel])
            else:
                inverted_image[i].append(current_pixel)
        i += 1
    return inverted_image


def fun_lighten(pixel, num):
    new_pixel = tuple()
    pixel = list(pixel)
    for i in range(len(pixel)):
        pixel[i] = pixel[i] + int(num * (255 - pixel[i]))
        new_pixel += (pixel[i]),
    return new_pixel


def lighten(image, num):
    return [[fun_lighten(pixel, num) for pixel in row] for row in image]


def fun_darken(pixel, num):
    new_pixel = tuple()
    pixel = list(pixel)
    for i in range(len(pixel)):
        pixel[i] = pixel[i] - int(num * (pixel[i] - 0))
        new_pixel += (pixel[i]),
    return new_pixel


def darken(image, num):
    return [[fun_darken(pixel, num) for pixel in row] for row in image]
