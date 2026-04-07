"""
200. 岛屿数量
https://leetcode.cn/problems/number-of-islands/description/

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
"""

from typing import List


class Solution:
    """
    岛屿数量解法类
    
    解题思路：
        深度优先搜索，遍历每个陆地格子，标记已访问
        
    算法步骤：
        1. 遍历网格的每个格子
        2. 如果是陆地且未访问，进行深度优先搜索
        3. 标记所有相邻的陆地为已访问
        4. 增加岛屿计数
        
    时间复杂度：O(mn)
    空间复杂度：O(mn)
    """
    
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        计算岛屿数量
        
        参数:
            grid: 二维网格
            
        返回:
            岛屿数量
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        def dfs(i, j):
            """
            深度优先搜索
            
            参数:
                i, j: 当前位置
            """
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            
            # 标记为已访问
            grid[i][j] = '#'
            
            # 向四个方向搜索
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                dfs(i + dx, j + dy)
        
        # 遍历每个格子
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count


class SolutionBFS:
    """
    广度优先搜索解法类
    """
    
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        计算岛屿数量（广度优先搜索版本）
        
        参数:
            grid: 二维网格
            
        返回:
            岛屿数量
        """
        if not grid or not grid[0]:
            return 0
        
        from collections import deque
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    queue = deque([(i, j)])
                    grid[i][j] = '#'
                    
                    while queue:
                        x, y = queue.popleft()
                        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                queue.append((nx, ny))
                                grid[nx][ny] = '#'
        
        return count


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1:")
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    solution = Solution()
    result1 = solution.numIslands(grid1)
    print(f"结果: {result1}")
    print(f"期望结果: 1")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2:")
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    solution2 = SolutionBFS()
    result2 = solution2.numIslands(grid2)
    print(f"结果: {result2}")
    print(f"期望结果: 3")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: []")
    grid3 = []
    solution3 = Solution()
    result3 = solution3.numIslands(grid3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [[]]")
    grid4 = [[]]
    solution4 = SolutionBFS()
    result4 = solution4.numIslands(grid4)
    print(f"结果: {result4}")
    print(f"期望结果: 0")
