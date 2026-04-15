"""
74. 搜索二维矩阵
https://leetcode.cn/problems/search-a-2d-matrix/description/

给你一个满足下述两条属性的 m x n 整数矩阵：
每行中的整数从左到右按非递减顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        在二维矩阵中搜索目标值
        
        参数:
            matrix: 二维矩阵
            target: 目标值
            
        返回:
            是否存在
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: target = 3")
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target1 = 3
    result1 = solution.searchMatrix(matrix1, target1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: target = 13")
    matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target2 = 13
    result2 = solution.searchMatrix(matrix2, target2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: target = 1")
    matrix3 = [[1]]
    target3 = 1
    result3 = solution.searchMatrix(matrix3, target3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
