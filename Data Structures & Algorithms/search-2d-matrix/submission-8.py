class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        d = len(matrix) - 1
        print(t, d)
        l = 0
        r = len(matrix[0]) - 1
        # early validation
        if target < matrix[0][0] or target > matrix[d][r]:
            return False
        while t <= d:
            if t == d:
                chosen_row = t
                break
            mid = t + (d-t)//2
            if target >= matrix[mid][0] and target < matrix[mid + 1][0]:
                chosen_row = mid
                break
            elif target < matrix[mid][0]:
                d = mid - 1
            elif target >= matrix[mid + 1][0]:
                t = mid + 1
        
        while l <= r:
            mid = l + (r-l)//2
            if target == matrix[chosen_row][mid]:
                return True
            elif target < matrix[chosen_row][mid]:
                r = mid - 1
            elif target > matrix[chosen_row][mid]:
                l = mid + 1
        
        return False


