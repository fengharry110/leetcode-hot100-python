# 221. 最大正方形
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。


class Solution:
    def maximalSquare(self, matrix):
        """
        找到只包含 '1' 的最大正方形
        方法：动态规划
        时间复杂度：O(m * n)，其中m和n分别是矩阵的行数和列数
        空间复杂度：O(m * n)，使用二维数组存储中间结果
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        # 创建dp数组，dp[i][j]表示以(i,j)为右下角的最大正方形的边长
        dp = [[0] * n for _ in range(m)]
        max_side = 0
        
        # 初始化第一行和第一列
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
            max_side = max(max_side, dp[i][0])
        
        for j in range(n):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
            max_side = max(max_side, dp[0][j])
        
        # 填充dp数组
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    # 以(i,j)为右下角的最大正方形的边长等于左上角、上方、左方三个位置的最小边长加1
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return max_side * max_side
    
    def maximalSquareOptimized(self, matrix):
        """
        找到只包含 '1' 的最大正方形
        方法：动态规划（空间优化）
        时间复杂度：O(m * n)，其中m和n分别是矩阵的行数和列数
        空间复杂度：O(n)，使用一维数组存储中间结果
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        # 创建一维dp数组，dp[j]表示当前行第j列的最大正方形的边长
        dp = [0] * n
        max_side = 0
        prev = 0  # 保存左上角的值
        
        for i in range(m):
            for j in range(n):
                temp = dp[j]
                if i == 0 or j == 0:
                    dp[j] = 1 if matrix[i][j] == '1' else 0
                elif matrix[i][j] == '1':
                    # 以(i,j)为右下角的最大正方形的边长等于左上角、上方、左方三个位置的最小边长加1
                    dp[j] = min(prev, dp[j], dp[j-1]) + 1
                else:
                    dp[j] = 0
                max_side = max(max_side, dp[j])
                prev = temp
        
        return max_side * max_side


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    matrix1 = [
        ['1','0','1','0','0'],
        ['1','0','1','1','1'],
        ['1','1','1','1','1'],
        ['1','0','0','1','0']
    ]
    print("测试用例1:")
    print("输入:")
    for row in matrix1:
        print(row)
    print("动态规划:", solution.maximalSquare(matrix1))
    print("空间优化:", solution.maximalSquareOptimized(matrix1))
    print()
    
    # 测试用例2
    matrix2 = [
        ['0','1'],
        ['1','0']
    ]
    print("测试用例2:")
    print("输入:")
    for row in matrix2:
        print(row)
    print("动态规划:", solution.maximalSquare(matrix2))
    print("空间优化:", solution.maximalSquareOptimized(matrix2))
    print()
    
    # 测试用例3
    matrix3 = [['0']]
    print("测试用例3:")
    print("输入:")
    for row in matrix3:
        print(row)
    print("动态规划:", solution.maximalSquare(matrix3))
    print("空间优化:", solution.maximalSquareOptimized(matrix3))
    print()
    
    # 测试用例4
    matrix4 = [
        ['1','1','1','1'],
        ['1','1','1','1'],
        ['1','1','1','1'],
        ['1','1','1','1']
    ]
    print("测试用例4:")
    print("输入:")
    for row in matrix4:
        print(row)
    print("动态规划:", solution.maximalSquare(matrix4))
    print("空间优化:", solution.maximalSquareOptimized(matrix4))