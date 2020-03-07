a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def rotate_right(image):
    n = len(image) - 1
    changed_items = []
    for i in range(0, len(image) - 1):
        for j in range(0, len(image) - 1):
            if image[n - j][n - i] not in changed_items:
                image[n - j][n - i], image[i][j] = image[i][j], image[n - j][n - i]
                changed_items.append(image[i][j])

    for i in range(0, len(image) // 2):
        for j in range(0, len(image)):
            image[n - i][j], image[i][j] = image[i][j], image[n - i][j]

    return image


def rotate_left(image):
    n = len(image) - 1
    changed_items = []
    for i in range(0, len(image) - 1):
        for j in range(0, len(image) - 1):
            if image[i][n-j] not in changed_items:
                image[i][n - j], image[n - j][i] = image[n - j][i], image[i][n - j]
                changed_items.append(image[n-j][i])

    for i in range(0, len(image) // 2):
        for j in range(0, len(image)):
            image[n - i][j], image[i][j] = image[i][j], image[n - i][j]

    return image


