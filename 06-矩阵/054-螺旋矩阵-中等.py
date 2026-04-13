# 54. 螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        result = []
        
        # 定义四个边界
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # 从左到右遍历上边界
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            
            # 从上到下遍历右边界
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # 从右到左遍历下边界（需要检查是否还有行）
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            
            # 从下到上遍历左边界（需要检查是否还有列）
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    result1 = solution.spiralOrder(matrix1)
    print(f"测试1结果: {result1}")  # 期望: [1,2,3,6,9,8,7,4,5]
    
    # 测试2
    matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    result2 = solution.spiralOrder(matrix2)
    print(f"测试2结果: {result2}")  # 期望: [1,2,3,4,8,12,11,10,9,5,6,7]
    
    # 测试3 - 单行
    matrix3 = [[1,2,3,4]]
    result3 = solution.spiralOrder(matrix3)
    print(f"测试3结果: {result3}")  # 期望: [1,2,3,4]
