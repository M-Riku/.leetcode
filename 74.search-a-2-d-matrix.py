#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.getRow(matrix, target)
        if row:
            return self.binarySearch(row, 0, len(row), target)
        else:
            return False
        
    def getRow(self, matrix: List[List[int]], target:int) -> List:
        for row in matrix:
            if not row:
                print("List is empty")
            else:
                if (row[0] <= target <= row[-1]):
                    return row
                
    def binarySearch(self, arr, i, j, target):
        while i <= j:
            mid = (i + j) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                i = mid + 1
            elif arr[mid] > target:
                j = mid - 1
        return False   
# @lc code=end

