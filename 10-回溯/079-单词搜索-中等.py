"""
79. 单词搜索
https://leetcode.cn/problems/word-search/description/

给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

示例 3：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
"""

from typing import List


class Solution:
    """
    单词搜索解法类
    
    解题思路：
        使用回溯算法，从每个单元格开始搜索，尝试匹配单词
        
    算法步骤：
        1. 遍历网格的每个单元格
        2. 对于每个单元格，调用回溯函数：
           - 如果当前位置超出边界或字符不匹配，返回False
           - 如果已经匹配完所有字符，返回True
           - 标记当前位置为已访问
           - 向四个方向递归搜索
           - 恢复当前位置为未访问
        3. 返回是否找到单词
        
    时间复杂度：O(m*n*4^L)
    空间复杂度：O(L)
    """
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        搜索单词是否存在于网格中
        
        参数:
            board: 二维字符网格
            word: 目标单词
            
        返回:
            是否存在
        """
        m, n = len(board), len(board[0])
        L = len(word)
        
        def backtrack(i, j, k):
            """
            回溯搜索
            
            参数:
                i, j: 当前位置
                k: 当前匹配的单词长度
                
            返回:
                是否找到
            """
            # 边界条件
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            # 匹配完成
            if k == L - 1:
                return True
            
            # 标记当前位置为已访问
            temp = board[i][j]
            board[i][j] = '#'
            
            # 向四个方向搜索
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                if backtrack(i + dx, j + dy, k + 1):
                    return True
            
            # 恢复当前位置
            board[i][j] = temp
            return False
        
        # 遍历每个单元格
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        
        return False


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"ABCCED\"")
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word1 = "ABCCED"
    solution = Solution()
    result1 = solution.exist(board1, word1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"SEE\"")
    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word2 = "SEE"
    solution2 = Solution()
    result2 = solution2.exist(board2, word2)
    print(f"结果: {result2}")
    print(f"期望结果: True")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"ABCB\"")
    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word3 = "ABCB"
    solution3 = Solution()
    result3 = solution3.exist(board3, word3)
    print(f"结果: {result3}")
    print(f"期望结果: False")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: board = [[\"A\"]], word = \"A\"")
    board4 = [["A"]]
    word4 = "A"
    solution4 = Solution()
    result4 = solution4.exist(board4, word4)
    print(f"结果: {result4}")
    print(f"期望结果: True")
