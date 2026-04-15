"""
17. 电话号码的字母组合
https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]

提示：
0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def letterCombinations(self, digits: str) -> List[str]:
        """
        返回电话号码的所有字母组合
        
        参数:
            digits: 数字字符串
            
        返回:
            所有字母组合
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: digits = '23'")
    digits1 = "23"
    print(f"结果: {solution.letterCombinations(digits1)}")
    print(f"期望结果: ['ad','ae','af','bd','be','bf','cd','ce','cf']")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: digits = ''")
    digits2 = ""
    print(f"结果: {solution.letterCombinations(digits2)}")
    print(f"期望结果: []")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: digits = '2'")
    digits3 = "2"
    print(f"结果: {solution.letterCombinations(digits3)}")
    print(f"期望结果: ['a','b','c']")
