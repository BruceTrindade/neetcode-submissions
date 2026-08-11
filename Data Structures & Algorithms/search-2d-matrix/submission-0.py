class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, down = 0, len(matrix) - 1
        size = len(matrix) - 1
        
        while top <= down:
            mid = (top + down) // 2
            if target >= matrix[mid][0]:
                left, right = 0, len(matrix[mid]) - 1
                if target <= matrix[mid][right]:
                    while left <= right:
                        row_mid = (left + right) // 2
                        if matrix[mid][row_mid] > target:
                            right = row_mid - 1
                        elif matrix[mid][row_mid] < target:
                            left = row_mid + 1
                        else:
                            return True
                    return False        
                else:
                    top = mid + 1                
            else:
                down = mid - 1
        return False           
