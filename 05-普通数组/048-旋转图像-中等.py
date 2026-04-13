"""
48. 旋转图像
中等
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]

示例 2：
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

提示：
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # 方法：先转置，再翻转每一行
        # 1. 转置
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2. 翻转每一行
        for i in range(n):
            matrix[i].reverse()


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("输入: matrix = [[1,2,3],[4,5,6],[7,8,9]]")
    solution.rotate(matrix1)
    print(f"输出: {matrix1}")
    
    # 测试用例2
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print("\n输入: [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]")
    solution.rotate(matrix2)
    print(f"输出: {matrix2}")
