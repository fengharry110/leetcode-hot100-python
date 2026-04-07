"""
5. 最长回文子串
https://leetcode.cn/problems/longest-palindromic-substring/description/

给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
"""

class Solution:
    """
    最长回文子串解法类
    
    解题思路：
        中心扩展法，遍历每个字符作为中心，向两边扩展
        
    算法步骤：
        1. 遍历字符串中的每个字符
        2. 以当前字符为中心，向两边扩展，寻找最长回文子串
        3. 考虑奇数和偶数长度的回文
        4. 记录最长回文子串的起始位置和长度
        5. 返回最长回文子串
        
    时间复杂度：O(n²)
    空间复杂度：O(1)
    """
    
    def longestPalindrome(self, s: str) -> str:
        """
        寻找最长回文子串
        
        参数:
            s: 输入字符串
            
        返回:
            最长回文子串
        """
        if not s:
            return ""
        
        n = len(s)
        start = 0
        max_len = 1
        
        def expand_around_center(left, right):
            """
            中心扩展
            
            参数:
                left: 左指针
                right: 右指针
                
            返回:
                回文子串的长度
            """
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(n):
            # 奇数长度回文
            len1 = expand_around_center(i, i)
            # 偶数长度回文
            len2 = expand_around_center(i, i + 1)
            # 取较大的长度
            length = max(len1, len2)
            # 更新最长回文子串的位置
            if length > max_len:
                max_len = length
                start = i - (length - 1) // 2
        
        return s[start:start + max_len]


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: \"babad\"")
    s1 = "babad"
    solution = Solution()
    result1 = solution.longestPalindrome(s1)
    print(f"结果: {result1}")
    print(f"期望结果: \"bab\" 或 \"aba\"")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: \"cbbd\"")
    s2 = "cbbd"
    solution2 = Solution()
    result2 = solution2.longestPalindrome(s2)
    print(f"结果: {result2}")
    print(f"期望结果: \"bb\"")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: \"a\"")
    s3 = "a"
    solution3 = Solution()
    result3 = solution3.longestPalindrome(s3)
    print(f"结果: {result3}")
    print(f"期望结果: \"a\"")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: \"ac\"")
    s4 = "ac"
    solution4 = Solution()
    result4 = solution4.longestPalindrome(s4)
    print(f"结果: {result4}")
    print(f"期望结果: \"a\" 或 \"c\"")
