from typing import List

'''
BUbble Sort:
It compares the adjacent elements and
swaps their positions if they are not in the
intended order iteratively until they are sorted.

Worst: O(n2) -> sort in ascending order but the array is in descending.
Best: O(n) -> rray is already sorted,.
Average: O(n2) -> elements of the array are in jumbled order.

Space: O(1) -> extra variable temp for swapping.
'''


def bubbleSort(A: List) -> List:
    n = len(A)
    unsorted_until_index = n - 1

    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, unsorted_until_index):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True

        unsorted_until_index -= 1

        # if there is not swapping in the last swap,
        # then the array is already sorted.
        if not swapped:
            break


def sortArray(A):
    i = 0

    while i < len(A):
        j = 0

        while j + 1 < len(A):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            j += 1
        i += 1


data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print(data)
assert data == [-9, -2, 0, 11, 45]
