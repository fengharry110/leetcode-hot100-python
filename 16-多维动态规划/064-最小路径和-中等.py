# 64. 最小路径和
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。


class Solution:
    def minPathSum(self, grid):
        """
        计算从左上角到右下角的最小路径和
        方法：动态规划
        时间复杂度：O(m * n)，其中m和n分别是网格的行数和列数
        空间复杂度：O(m * n)，使用二维数组存储中间结果
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        # 创建dp数组，dp[i][j]表示从左上角到(i,j)的最小路径和
        dp = [[0] * n for _ in range(m)]
        
        # 初始化左上角
        dp[0][0] = grid[0][0]
        
        # 初始化第一行
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # 初始化第一列
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # 填充dp数组
        for i in range(1, m):
            for j in range(1, n):
                # 从上方或左方选择路径和较小的一个
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]
    
    def minPathSumOptimized(self, grid):
        """
        计算从左上角到右下角的最小路径和
        方法：动态规划（空间优化）
        时间复杂度：O(m * n)，其中m和n分别是网格的行数和列数
        空间复杂度：O(n)，使用一维数组存储中间结果
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        # 创建一维dp数组，dp[j]表示当前行第j列的最小路径和
        dp = [0] * n
        
        # 初始化第一个元素
        dp[0] = grid[0][0]
        
        # 初始化第一行
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        
        # 填充dp数组
        for i in range(1, m):
            # 更新当前行的第一个元素
            dp[0] += grid[i][0]
            for j in range(1, n):
                # 从上方或左方选择路径和较小的一个
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    grid1 = [[1,3,1],[1,5,1],[4,2,1]]
    print("测试用例1:")
    print("输入:", grid1)
    print("动态规划:", solution.minPathSum(grid1))
    print("空间优化:", solution.minPathSumOptimized(grid1))
    print()
    
    # 测试用例2
    grid2 = [[1,2,3],[4,5,6]]
    print("测试用例2:")
    print("输入:", grid2)
    print("动态规划:", solution.minPathSum(grid2))
    print("空间优化:", solution.minPathSumOptimized(grid2))
    print()
    
    # 测试用例3
    grid3 = [[1]]
    print("测试用例3:")
    print("输入:", grid3)
    print("动态规划:", solution.minPathSum(grid3))
    print("空间优化:", solution.minPathSumOptimized(grid3))
    print()
    
    # 测试用例4
    grid4 = [[1,2],[1,1]]
    print("测试用例4:")
    print("输入:", grid4)
    print("动态规划:", solution.minPathSum(grid4))
    print("空间优化:", solution.minPathSumOptimized(grid4))