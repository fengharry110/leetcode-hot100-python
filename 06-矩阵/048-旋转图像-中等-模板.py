"""
48. 旋转图像
https://leetcode.cn/problems/rotate-image/description/

给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]

示例 2：
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

提示：
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        将图像顺时针旋转 90 度
        
        参数:
            matrix: n × n 的二维矩阵
            
        返回:
            None（原地修改矩阵）
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [[1,2,3],[4,5,6],[7,8,9]]")
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    solution.rotate(matrix1)
    print(f"结果: {matrix1}")
    print(f"期望结果: [[7,4,1],[8,5,2],[9,6,3]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]")
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(matrix2)
    print(f"结果: {matrix2}")
    print(f"期望结果: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [[1]]")
    matrix3 = [[1]]
    solution.rotate(matrix3)
    print(f"结果: {matrix3}")
    print(f"期望结果: [[1]]")
