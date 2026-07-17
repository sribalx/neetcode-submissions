class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # two binary searches, one for row and one for column
        n = len(matrix)
        m = len(matrix[0]) - 1
        row = self.binaryRow(0, n - 1, matrix, target)
        print (row)
        if row == - 1:
            return False
        return self.binaryColumn(0, m, matrix[row], target)
    
    def binaryRow(self, t, b, matrix, target):
        if b < t:
            return -1
        
        curr = (b + t) // 2
        if matrix[curr][0] == target:
            return curr
        if matrix[curr][0] > target:
            if curr - 1 < 0:
                return curr
            if matrix[curr - 1][0] <= target:
                return curr - 1
            else:
                return self.binaryRow(t, curr, matrix, target)
        if matrix[curr][0] < target:
            if curr + 1 > len(matrix) - 1:
                return curr
            elif matrix[curr + 1][0] == target:
                return curr + 1
            elif matrix[curr + 1][0] > target:
                return curr
            else:
                return self.binaryRow(curr+1, b, matrix, target)

    def binaryColumn(self, l, r, array: List[int], target):
        if l > r:
            return False
        
        curr = (l + r) // 2
        print (l, r, curr, array[curr])
        if array[curr] == target:
            return True
        if array[curr] > target:
            print("going down")
            return self.binaryColumn(l, curr - 1, array, target)
        if array[curr] < target:
            print("going up")
            return self.binaryColumn(curr + 1, r, array, target )
