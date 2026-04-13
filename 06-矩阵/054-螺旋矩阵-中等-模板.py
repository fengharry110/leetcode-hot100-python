"""
54. 螺旋矩阵
https://leetcode.cn/problems/spiral-matrix/description/

给你一个 m 行 n 列的矩阵 matrix，请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

提示：
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        按照顺时针螺旋顺序返回矩阵中的所有元素
        
        参数:
            matrix: m 行 n 列的矩阵
            
        返回:
            螺旋顺序的元素列表
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [[1,2,3],[4,5,6],[7,8,9]]")
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    result1 = solution.spiralOrder(matrix1)
    print(f"结果: {result1}")
    print(f"期望结果: [1,2,3,6,9,8,7,4,5]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [[1,2,3,4],[5,6,7,8],[9,10,11,12]]")
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result2 = solution.spiralOrder(matrix2)
    print(f"结果: {result2}")
    print(f"期望结果: [1,2,3,4,8,12,11,10,9,5,6,7]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [[1,2,3,4]]")
    matrix3 = [[1, 2, 3, 4]]
    result3 = solution.spiralOrder(matrix3)
    print(f"结果: {result3}")
    print(f"期望结果: [1,2,3,4]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [[1],[2],[3]]")
    matrix4 = [[1], [2], [3]]
    result4 = solution.spiralOrder(matrix4)
    print(f"结果: {result4}")
    print(f"期望结果: [1,2,3]")
