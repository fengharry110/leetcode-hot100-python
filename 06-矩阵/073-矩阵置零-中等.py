# 73. 矩阵置零
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
#
# 示例 1：
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
#
# 示例 2：
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
# 提示：
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        # 使用第一行和第一列来标记是否需要置零
        # 需要先记录第一行和第一列是否原本就有0
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # 遍历矩阵，用第一行和第一列标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # 根据标记置零
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # 处理第一行和第一列
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
    
    def setZeroes_v2(self, matrix: List[List[int]]) -> None:
        """
        使用额外空间的版本，更容易理解
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        
        # 记录所有需要置零的行和列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        # 置零
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    solution.setZeroes(matrix1)
    print(f"测试1结果: {matrix1}")  # 期望: [[1,0,1],[0,0,0],[1,0,1]]
    
    # 测试2
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution.setZeroes(matrix2)
    print(f"测试2结果: {matrix2}")  # 期望: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
