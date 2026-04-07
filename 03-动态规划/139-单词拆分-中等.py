"""
139. 单词拆分
https://leetcode.cn/problems/word-break/description/

给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""

from typing import List


class Solution:
    """
    单词拆分解法类
    
    解题思路：
        使用动态规划，dp[i]表示前i个字符是否可以被拆分
        
    算法步骤：
        1. 初始化dp数组，dp[0] = True
        2. 遍历字符串，对于每个位置i：
           - 遍历单词字典，对于每个单词word：
               - 如果i >= len(word)且dp[i - len(word)]为True，并且s[i - len(word):i] == word，则dp[i] = True
        3. 返回dp[-1]
        
    时间复杂度：O(n² * m)
    空间复杂度：O(n)
    """
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        判断是否可以利用字典中的单词拼接出s
        
        参数:
            s: 目标字符串
            wordDict: 单词字典
            
        返回:
            是否可以拼接
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # 空字符串可以被拆分
        
        for i in range(1, n + 1):
            for word in wordDict:
                word_len = len(word)
                if i >= word_len and dp[i - word_len] and s[i - word_len:i] == word:
                    dp[i] = True
                    break
        
        return dp[n]


class SolutionSet:
    """
    集合优化解法类
    
    解题思路：
        使用集合存储单词，优化查找效率
        
    算法步骤：
        1. 将单词字典转换为集合
        2. 初始化dp数组
        3. 遍历字符串，对于每个位置i：
           - 遍历从0到i的位置j：
               - 如果dp[j]为True且s[j:i]在集合中，则dp[i] = True
        4. 返回dp[-1]
        
    时间复杂度：O(n²)
    空间复杂度：O(n + m)
    """
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        判断是否可以利用字典中的单词拼接出s（集合优化版本）
        
        参数:
            s: 目标字符串
            wordDict: 单词字典
            
        返回:
            是否可以拼接
        """
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: s = \"leetcode\", wordDict = [\"leet\", \"code\"]")
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    solution = Solution()
    result1 = solution.wordBreak(s1, wordDict1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: s = \"applepenapple\", wordDict = [\"apple\", \"pen\"]")
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    solution2 = SolutionSet()
    result2 = solution2.wordBreak(s2, wordDict2)
    print(f"结果: {result2}")
    print(f"期望结果: True")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = \"catsandog\", wordDict = [\"cats\", \"dog\", \"sand\", \"and\", \"cat\"]")
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    solution3 = Solution()
    result3 = solution3.wordBreak(s3, wordDict3)
    print(f"结果: {result3}")
    print(f"期望结果: False")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: s = \"a\", wordDict = [\"a\"]")
    s4 = "a"
    wordDict4 = ["a"]
    solution4 = SolutionSet()
    result4 = solution4.wordBreak(s4, wordDict4)
    print(f"结果: {result4}")
    print(f"期望结果: True")
