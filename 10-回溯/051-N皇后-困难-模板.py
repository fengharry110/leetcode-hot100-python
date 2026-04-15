"""
51. N皇后
https://leetcode.cn/problems/n-queens/description/

按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释: 如下图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]

提示：
1 <= n <= 9
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        返回所有不同的N皇后问题的解决方案
        
        参数:
            n: 棋盘大小和皇后数量
            
        返回:
            所有有效的棋子放置方案
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: n = 4")
    n1 = 4
    result1 = solution.solveNQueens(n1)
    print(f"结果: {result1}")
    print(f"期望结果: [[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"],[\"..Q.\",\"Q...\",\"...Q\",\".Q..\"]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: n = 1")
    n2 = 1
    result2 = solution.solveNQueens(n2)
    print(f"结果: {result2}")
    print(f"期望结果: [[\"Q\"]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: n = 2")
    n3 = 2
    result3 = solution.solveNQueens(n3)
    print(f"结果: {result3}")
    print(f"期望结果: []")
