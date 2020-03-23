##
#
# filename: bubble_sort.py
# By: Abhay Gupta
# Date: 03-23-20
#
# Desc: transverse through array and swap element if larger
##


import numpy as np


def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)


if __name__ == "__main__":
    array = np.arange(9)
    np.random.shuffle(array)
    print(array)

    bubble_sort(array)