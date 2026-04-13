"""
17. 电话号码的字母组合
中等
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
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # 数字到字母的映射
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, path: str):
            if index == len(digits):
                result.append(path)
                return
            
            for letter in phone_map[digits[index]]:
                backtrack(index + 1, path + letter)
        
        backtrack(0, "")
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    digits1 = "23"
    print(f"输入: digits = '{digits1}'")
    print(f"输出: {solution.letterCombinations(digits1)}")
    
    # 测试用例2
    digits2 = ""
    print(f"\n输入: digits = '{digits2}'")
    print(f"输出: {solution.letterCombinations(digits2)}")
    
    # 测试用例3
    digits3 = "2"
    print(f"\n输入: digits = '{digits3}'")
    print(f"输出: {solution.letterCombinations(digits3)}")
