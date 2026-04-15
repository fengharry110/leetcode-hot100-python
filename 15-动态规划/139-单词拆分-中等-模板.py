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

提示：
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s 和 wordDict[i] 仅由小写英文字母组成
wordDict 中的所有字符串 互不相同
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        判断字符串是否可以由字典中的单词拼接而成
        
        参数:
            s: 目标字符串
            wordDict: 单词字典
            
        返回:
            是否可以拼接
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: s = 'leetcode', wordDict = ['leet', 'code']")
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    result1 = solution.wordBreak(s1, wordDict1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: s = 'applepenapple', wordDict = ['apple', 'pen']")
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    result2 = solution.wordBreak(s2, wordDict2)
    print(f"结果: {result2}")
    print(f"期望结果: True")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = 'catsandog', wordDict = ['cats', 'dog', 'sand', 'and', 'cat']")
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    result3 = solution.wordBreak(s3, wordDict3)
    print(f"结果: {result3}")
    print(f"期望结果: False")
