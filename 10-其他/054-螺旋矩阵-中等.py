"""
54. 螺旋矩阵
https://leetcode.cn/problems/spiral-matrix/description/

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


class Solution:
    """
    螺旋矩阵解法类
    
    解题思路：
        模拟螺旋遍历，使用四个边界控制遍历方向
        
    算法步骤：
        1. 初始化四个边界：上、下、左、右
        2. 按照右、下、左、上的顺序遍历
        3. 每次遍历后更新对应的边界
        4. 直到所有元素都被遍历
        
    时间复杂度：O(mn)
    空间复杂度：O(1)
    """
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        螺旋遍历矩阵
        
        参数:
            matrix: 二维矩阵
            
        返回:
            螺旋遍历的结果
        """
        if not matrix or not matrix[0]:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 从左到右
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # 从上到下
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # 从右到左
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # 从下到上
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [[1,2,3],[4,5,6],[7,8,9]]")
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    result1 = solution.spiralOrder(matrix1)
    print(f"结果: {result1}")
    print(f"期望结果: [1,2,3,6,9,8,7,4,5]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [[1,2,3,4],[5,6,7,8],[9,10,11,12]]")
    matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    solution2 = Solution()
    result2 = solution2.spiralOrder(matrix2)
    print(f"结果: {result2}")
    print(f"期望结果: [1,2,3,4,8,12,11,10,9,5,6,7]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [[1]]")
    matrix3 = [[1]]
    solution3 = Solution()
    result3 = solution3.spiralOrder(matrix3)
    print(f"结果: {result3}")
    print(f"期望结果: [1]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [[1,2],[3,4]]")
    matrix4 = [[1,2],[3,4]]
    solution4 = Solution()
    result4 = solution4.spiralOrder(matrix4)
    print(f"结果: {result4}")
    print(f"期望结果: [1,2,4,3]")
