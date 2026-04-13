# 994. 腐烂的橘子
# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
# 值 0 代表空单元格；值 1 代表新鲜橘子；值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子周围 4 个方向上相邻的新鲜橘子都会腐烂。
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
#
# 示例 1：
# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#
# 示例 2：
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
#
# 示例 3：
# 输入：grid = [[0,2]]
# 输出：0

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # 找到所有腐烂的橘子，统计新鲜橘子数量
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue and fresh > 0:
            minutes += 1
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
        
        return -1 if fresh > 0 else minutes


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    print(f"测试1结果: {solution.orangesRotting(grid1)}")  # 期望输出: 4
    
    # 测试2
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    print(f"测试2结果: {solution.orangesRotting(grid2)}")  # 期望输出: -1
    
    # 测试3
    grid3 = [[0,2]]
    print(f"测试3结果: {solution.orangesRotting(grid3)}")  # 期望输出: 0
