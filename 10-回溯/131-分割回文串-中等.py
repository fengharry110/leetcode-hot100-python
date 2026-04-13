# 131. 分割回文串
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。返回 s 所有可能的分割方案。
#
# 示例 1：
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#
# 示例 2：
# 输入：s = "a"
# 输出：[["a"]]
#
# 提示：
# 1 <= s.length <= 16
# s 仅由小写英文字母组成

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start: int):
            if start == len(s):
                result.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if is_palindrome(substr):
                    path.append(substr)
                    backtrack(end)
                    path.pop()
        
        backtrack(0)
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    result1 = solution.partition("aab")
    print(f"测试1结果: {result1}")  # 期望输出: [["a","a","b"],["aa","b"]]
    
    # 测试2
    result2 = solution.partition("a")
    print(f"测试2结果: {result2}")  # 期望输出: [["a"]]
