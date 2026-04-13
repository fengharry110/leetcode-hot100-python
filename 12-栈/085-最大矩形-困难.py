"""
85. 最大矩形
困难
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。

示例 2：
输入：matrix = [["0"]]
输出：0

示例 3：
输入：matrix = [["1"]]
输出：1

提示：
rows == matrix.length
cols == matrix[i].length
1 <= rows, cols <= 200
matrix[i][j] 为 '0' 或 '1'
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        # heights[i] 表示第i列的高度
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            # 更新高度数组
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            
            # 计算当前行的最大矩形面积（单调栈）
            stack = []
            for i in range(cols + 1):
                h = heights[i] if i < cols else 0
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
        
        return max_area


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    matrix1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print("输入: matrix = [['1','0','1','0','0'],...]")
    print(f"输出: {solution.maximalRectangle(matrix1)}")
    
    # 测试用例2
    matrix2 = [["0"]]
    print(f"\n输入: matrix = [['0']]")
    print(f"输出: {solution.maximalRectangle(matrix2)}")
    
    # 测试用例3
    matrix3 = [["1"]]
    print(f"\n输入: matrix = [['1']]")
    print(f"输出: {solution.maximalRectangle(matrix3)}")
