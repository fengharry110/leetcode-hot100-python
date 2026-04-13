"""
22. 括号生成
中等
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
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # 当括号数量达到2n时，添加到结果
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # 如果左括号数量小于n，可以添加左括号
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # 如果右括号数量小于左括号数量，可以添加右括号
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    n1 = 3
    print(f"输入: n = {n1}")
    print(f"输出: {solution.generateParenthesis(n1)}")
    
    # 测试用例2
    n2 = 1
    print(f"\n输入: n = {n2}")
    print(f"输出: {solution.generateParenthesis(n2)}")
    
    # 测试用例3
    n3 = 2
    print(f"\n输入: n = {n3}")
    print(f"输出: {solution.generateParenthesis(n3)}")
