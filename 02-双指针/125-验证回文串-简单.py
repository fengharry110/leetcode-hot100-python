"""
125. 验证回文串
https://leetcode.cn/problems/valid-palindrome/description/

如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。

示例 1：
输入: s = "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串。

示例 2：
输入: s = "race a car"
输出: false
解释："raceacar" 不是回文串。

示例 3：
输入: s = " "
输出: true
解释：在移除非字母数字字符之后，s 是一个空字符串 ""。由于空字符串正着反着读都一样，所以是回文串。
"""

import re


class Solution:
    """
    验证回文串解法类
    
    解题思路：
        1. 过滤掉非字母数字字符
        2. 转换为小写
        3. 比较正序和逆序是否相同
        
    算法步骤：
        1. 使用正则表达式过滤非字母数字字符
        2. 转换为小写
        3. 比较字符串和其逆序是否相同
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def isPalindrome(self, s: str) -> bool:
        """
        验证是否为回文串
        
        参数:
            s: 输入字符串
            
        返回:
            是否为回文串
        """
        # 过滤非字母数字字符并转换为小写
        filtered = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # 比较正序和逆序
        return filtered == filtered[::-1]


class SolutionTwoPointer:
    """
    双指针解法类
    
    解题思路：
        使用双指针从两端向中间移动，比较字符
        
    算法步骤：
        1. 初始化左指针为0，右指针为字符串长度-1
        2. 当左指针小于右指针时：
           - 跳过非字母数字字符
           - 转换为小写并比较
           - 如果不同，返回False
           - 否则，移动指针
        3. 返回True
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def isPalindrome(self, s: str) -> bool:
        """
        验证是否为回文串（双指针版本）
        
        参数:
            s: 输入字符串
            
        返回:
            是否为回文串
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            # 跳过左指针的非字母数字字符
            while left < right and not s[left].isalnum():
                left += 1
            # 跳过右指针的非字母数字字符
            while left < right and not s[right].isalnum():
                right -= 1
            
            # 比较字符
            if s[left].lower() != s[right].lower():
                return False
            
            # 移动指针
            left += 1
            right -= 1
        
        return True


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: \"A man, a plan, a canal: Panama\"")
    s1 = "A man, a plan, a canal: Panama"
    solution = Solution()
    result1 = solution.isPalindrome(s1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: \"race a car\"")
    s2 = "race a car"
    solution2 = SolutionTwoPointer()
    result2 = solution2.isPalindrome(s2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: \" \"")
    s3 = " "
    solution3 = Solution()
    result3 = solution3.isPalindrome(s3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: \"0P\"")
    s4 = "0P"
    solution4 = SolutionTwoPointer()
    result4 = solution4.isPalindrome(s4)
    print(f"结果: {result4}")
    print(f"期望结果: False")
