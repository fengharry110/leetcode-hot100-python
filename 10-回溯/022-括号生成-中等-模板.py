"""
22. 括号生成
https://leetcode.cn/problems/generate-parentheses/description/

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

提示：
1 <= n <= 8
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def generateParenthesis(self, n: int) -> List[str]:
        """
        生成所有可能的有效括号组合
        
        参数:
            n: 括号对数
            
        返回:
            所有有效的括号组合
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: n = 3")
    n1 = 3
    print(f"结果: {solution.generateParenthesis(n1)}")
    print(f"期望结果: ['((()))','(()())','(())()','()(())','()()()']")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: n = 1")
    n2 = 1
    print(f"结果: {solution.generateParenthesis(n2)}")
    print(f"期望结果: ['()']")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: n = 2")
    n3 = 2
    print(f"结果: {solution.generateParenthesis(n3)}")
    print(f"期望结果: ['(())','()()']")
