##
# filename: insertion_sort.py
# By: Abhay Gupta
# Date: 03-23-2020
#
# Description: Sort an array by inserting next element into sorted array
##

import numpy as np


def insertion_sort(arr):

    # transverse through the array
    for j in range(1, len(arr)):
        i = j

        # if element smaller than previous, swap elements
        while i != 0 and arr[i] < arr[i - 1]:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
            i = i-1

    print(arr)  # print sorted array


if __name__ == '__main__':

    array = np.arange(9)
    np.random.shuffle(array)
    print(array)  # print unsorted array
    insertion_sort(array)
