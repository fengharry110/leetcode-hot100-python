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
"""

from typing import List


class Solution:
    """
    二分查找解法类
    
    解题思路：
        将二维矩阵视为一维有序数组，使用二分查找
        
    算法步骤：
        1. 计算矩阵的行数和列数
        2. 初始化左指针为0，右指针为m*n-1
        3. 当左<=右时：
           - 计算中间位置mid
           - 将mid转换为二维坐标：row = mid // n, col = mid % n
           - 比较matrix[row][col]与target
           - 根据比较结果调整指针
        4. 返回是否找到
        
    时间复杂度：O(log(mn))
    空间复杂度：O(1)
    """
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        在二维矩阵中搜索目标值
        
        参数:
            matrix: 二维整数矩阵
            target: 目标值
            
        返回:
            目标值是否存在
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # 转换为二维坐标
            row = mid // n
            col = mid % n
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3")
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    solution = Solution()
    result1 = solution.searchMatrix(matrix1, target1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13")
    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target2 = 13
    solution2 = Solution()
    result2 = solution2.searchMatrix(matrix2, target2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: matrix = [[1]], target = 1")
    matrix3 = [[1]]
    target3 = 1
    solution3 = Solution()
    result3 = solution3.searchMatrix(matrix3, target3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: matrix = [[1,3]], target = 2")
    matrix4 = [[1, 3]]
    target4 = 2
    solution4 = Solution()
    result4 = solution4.searchMatrix(matrix4, target4)
    print(f"结果: {result4}")
    print(f"期望结果: False")
