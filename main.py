import matplotlib.pyplot as plt
import pygame as pg
import numpy as np
import time


def n_neighbors(arr: np.ndarray, y, x) -> int:
    neighbors = [1, 0, -1]
    neigh = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # print(('%2i %2i') % (x + i, y + j))
            if not(i == 0 and j == 0) and (y + i) < len(arr) and (x + j) < len(arr) and \
                    (y + i) > 0 and (x + j) > 0 and arr[y + i][x + j] == 1:
                neigh += 1
    # print('-----')
    return neigh


def frame(arr: np.ndarray) -> np.ndarray:
    for y in range(len(arr2)):
        for x in range(len(arr2)):
            neigh = n_neighbors(arr, y, x)
            if arr2[y][x]:
                if neigh < 2:
                    arr2[y][x] = 0
                if neigh > 3:
                    arr2[y][x] = 0
            elif neigh == 3:
                arr2[y][x] = 1
    return arr2


if __name__ == '__main__':
    plt.ion()
    plt.figure()
    plt.show()

    fig, ax = plt.subplots()
    ax.axis('equal')
    # arr = np.array([
    #     1, 1, 1,  # 8 8 5
    #     1, 1, 1,  # 8 8 5
    #     1, 1, 1,  # 5 5 3
    # ])

    # arr = np.array([
    #     0, 0, 0, 0, 0,  # 0 0 0 0 0 | 0 0 0 0 0
    #     0, 1, 1, 1, 0,  # 1 2 3 2 1 | 1 2 3 2 1
    #     0, 1, 0, 1, 0,  # 1 1 2 1 1 | 1 1 2 1 1
    #     0, 1, 1, 1, 0,  # 1 2 3 2 1 | 1 2 3 2 1
    #     0, 0, 0, 0, 0,  # 0 0 0 0 0 | 0 0 0 0 0
    # ])

    arr = np.array([0] * 100)

    s = int(np.sqrt(arr.size))
    arr = arr.reshape(s, s)
    img = plt.matshow(arr, cmap=plt.get_cmap('gray_r'))
    while True:
        y = int(input('y >>> '))
        x = int(input('x >>> '))
        if x == -1:
            break
        arr[y][x] = 1
    arr2 = arr.copy()
    while True:
        img.set_data(arr)
        arr2 = frame(arr)
        arr = arr2.copy()
        plt.pause(.00001)
        time.sleep(1)
