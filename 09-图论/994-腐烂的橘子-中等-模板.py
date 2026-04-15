"""
994. 腐烂的橘子
https://leetcode.cn/problems/rotting-oranges/description/

在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子周围 4 个方向上相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

示例 1：
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4

示例 2：
输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1

示例 3：
输入：grid = [[0,2]]
输出：0

提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] 仅为 0、1 或 2
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        计算直到没有新鲜橘子为止所必须经过的最小分钟数
        
        参数:
            grid: 网格，0=空，1=新鲜橘子，2=腐烂橘子
            
        返回:
            最小分钟数，如果不可能返回 -1
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    print("=" * 50)
    print("测试1: grid = [[2,1,1],[1,1,0],[0,1,1]]")
    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    print(f"结果: {solution.orangesRotting(grid1)}")
    print(f"期望结果: 4")
    
    # 测试2
    print("\n" + "=" * 50)
    print("测试2: grid = [[2,1,1],[0,1,1],[1,0,1]]")
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    print(f"结果: {solution.orangesRotting(grid2)}")
    print(f"期望结果: -1")
    
    # 测试3
    print("\n" + "=" * 50)
    print("测试3: grid = [[0,2]]")
    grid3 = [[0,2]]
    print(f"结果: {solution.orangesRotting(grid3)}")
    print(f"期望结果: 0")
