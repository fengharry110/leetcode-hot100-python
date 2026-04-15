"""
64. 最小路径和
https://leetcode.cn/problems/minimum-path-sum/description/

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12

提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        找出从左上角到右下角的最小路径和
        
        参数:
            grid: 网格数组
            
        返回:
            最小路径和
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: grid = [[1,3,1],[1,5,1],[4,2,1]]")
    grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result1 = solution.minPathSum(grid1)
    print(f"结果: {result1}")
    print(f"期望结果: 7")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: grid = [[1,2,3],[4,5,6]]")
    grid2 = [[1, 2, 3], [4, 5, 6]]
    result2 = solution.minPathSum(grid2)
    print(f"结果: {result2}")
    print(f"期望结果: 12")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: grid = [[1]]")
    grid3 = [[1]]
    result3 = solution.minPathSum(grid3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
