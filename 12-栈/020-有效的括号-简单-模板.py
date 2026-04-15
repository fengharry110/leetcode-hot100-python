"""
20. 有效的括号
https://leetcode.cn/problems/valid-parentheses/description/

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

提示：
1 <= s.length <= 10^4
s 仅由括号 '()[]{}' 组成
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def isValid(self, s: str) -> bool:
        """
        判断括号字符串是否有效
        
        参数:
            s: 只包含括号的字符串
            
        返回:
            是否有效
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: s = '()'")
    s1 = "()"
    result1 = solution.isValid(s1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: s = '()[]{}'")
    s2 = "()[]{}"
    result2 = solution.isValid(s2)
    print(f"结果: {result2}")
    print(f"期望结果: True")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = '(]'")
    s3 = "(]"
    result3 = solution.isValid(s3)
    print(f"结果: {result3}")
    print(f"期望结果: False")
