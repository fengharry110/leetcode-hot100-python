# 51. N 皇后
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回所有不同的 n 皇后问题的解决方案。
#
# 示例 1：
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#
# 示例 2：
# 输入：n = 1
# 输出：[["Q"]]

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        def is_valid(row: int, col: int) -> bool:
            # 检查列
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # 检查左上对角线
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # 检查右上对角线
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        
        def backtrack(row: int):
            if row == n:
                result.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'
        
        backtrack(0)
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    result1 = solution.solveNQueens(4)
    print(f"测试1结果: {result1}")
    
    # 测试2
    result2 = solution.solveNQueens(1)
    print(f"测试2结果: {result2}")
