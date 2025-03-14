'''
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
https://levelup.gitconnected.com/make-way-for-the-matrix-a-complete-guide-to-solving-2d-array-coding-problems-725096d122d9
Write an efficient algorithm that searches
for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

from typing import List
Matrix = List[List[int]]


class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        n, m = len(matrix), len(matrix[0])

        if not n or not m:
            return False

        for i in range(n):
            if target < matrix[i][0] or target > matrix[i][-1]:
                i += 1

            if i >= n:
                return False

            for j in range(m):
                if matrix[i][j] == target:
                    return True

        return False


class SolutionSorted:
    '''
    Notice that the elements become smaller as we move
    left in a row and larger as we move down a column
    '''

    def searchMatrix(self, matrix, target):
        if matrix == []:
            return False
        n, m = len(matrix), len(matrix[0])

        i, j = 0, m - 1
        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:  # Move down a row
                i += 1
            elif matrix[i][j] > target:  # Move left a column
                j -= 1
        return False


class SortedSearch:
    '''
    Initialize start to 0 and end to M-1 where M= number of rows.
    Find the middle row and then apply a binary search to search
    for the target element in the row. If the target element is found,
    return True else modify the middle row as needed and continue the
    search till start ≤ end. So, the outer binary search searches
    for the row while the inner binary search searches for the
    element within a row. Here’s the walkthrough:
    '''

    def search_matrix(self, matrix: Matrix, target: int) -> bool:
        n_rows, n_cols = len(matrix), len(matrix[0])

        if not n_rows or not n_cols:
            return False

        start, end = 0, n_rows
        # outer binary search to select the row
        while start < end:
            mid_row = (start + end) // 2
            # inner binary search on the row
            found = self.helper_search(matrix[mid_row], target)
            if found:
                return True
            elif matrix[mid_row][-1] > target:
                end = mid_row - 1
            else:
                start = mid_row + 1
        return False

        # Helper function to perform binary search for the target on a row
        def helper_search(self, row, target):
            n_cols = len(row)
            start, end = 0, n_cols - 1

            while start <= end:
                mid = (start + end) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return False
