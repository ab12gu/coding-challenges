##
#
# filename: selection_sort.py
# by: Abhay Gupta
# date: 03-23-20
#
# desc: finds minimum of unsorted array and puts it at front of array
##


import numpy as np


def selection_sort(array):

    for i in range(len(array)):
        small = i
        for j in range(i+1, len(array)):
            if array[small] > array[j]:
                small = j;

        temp = array[small]
        array[small] = array[i]
        array[i] = temp

    print(array)


if __name__ == "__main__":

    array = np.arange(9)
    np.random.shuffle(array)

    print(array)
    selection_sort(array)
