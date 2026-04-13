# 74. 搜索二维矩阵
# 给你一个满足下述两条属性的 m x n 整数矩阵：
# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
#
# 示例 1：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#
# 示例 2：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // n][mid % n]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(f"测试1结果: {solution.searchMatrix(matrix1, 3)}")  # 期望输出: True
    
    # 测试2
    matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(f"测试2结果: {solution.searchMatrix(matrix2, 13)}")  # 期望输出: False
