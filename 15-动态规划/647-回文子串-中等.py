"""
647. 回文子串
https://leetcode.cn/problems/palindromic-substrings/description/

给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""

class Solution:
    """
    回文子串解法类
    
    解题思路：
        中心扩展法，遍历每个可能的回文中心
        
    算法步骤：
        1. 遍历每个字符作为回文中心
        2. 对于每个中心，向两边扩展，统计回文子串的数量
        3. 考虑奇数长度和偶数长度的回文
        
    时间复杂度：O(n²)
    空间复杂度：O(1)
    """
    
    def countSubstrings(self, s: str) -> int:
        """
        统计回文子串的数量
        
        参数:
            s: 输入字符串
            
        返回:
            回文子串的数量
        """
        def expand_around_center(left, right):
            """
            从中心向两边扩展，统计回文子串的数量
            
            参数:
                left: 左指针
                right: 右指针
                
            返回:
                回文子串的数量
            """
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        total = 0
        for i in range(len(s)):
            # 奇数长度的回文
            total += expand_around_center(i, i)
            # 偶数长度的回文
            total += expand_around_center(i, i + 1)
        
        return total


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: \"abc\"")
    s1 = "abc"
    solution = Solution()
    result1 = solution.countSubstrings(s1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: \"aaa\"")
    s2 = "aaa"
    solution2 = Solution()
    result2 = solution2.countSubstrings(s2)
    print(f"结果: {result2}")
    print(f"期望结果: 6")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: \"abba\"")
    s3 = "abba"
    solution3 = Solution()
    result3 = solution3.countSubstrings(s3)
    print(f"结果: {result3}")
    print(f"期望结果: 6")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: \"a\"")
    s4 = "a"
    solution4 = Solution()
    result4 = solution4.countSubstrings(s4)
    print(f"结果: {result4}")
    print(f"期望结果: 1")
