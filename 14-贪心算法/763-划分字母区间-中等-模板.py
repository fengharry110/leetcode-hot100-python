"""
763. 划分字母区间
https://leetcode.cn/problems/partition-labels/description/

给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。

注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

返回一个表示每个字符串片段的长度的列表。

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 

示例 2：
输入：s = "eccbbbbxxc"
输出：[10]

提示：
1 <= s.length <= 500
s 仅由小写英文字母组成
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def partitionLabels(self, s: str) -> List[int]:
        """
        划分字母区间
        
        参数:
            s: 输入字符串
            
        返回:
            每个片段长度的列表
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: s = 'ababcbacadefegdehijhklij'")
    s1 = "ababcbacadefegdehijhklij"
    result1 = solution.partitionLabels(s1)
    print(f"结果: {result1}")
    print(f"期望结果: [9, 7, 8]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: s = 'eccbbbbxxc'")
    s2 = "eccbbbbxxc"
    result2 = solution.partitionLabels(s2)
    print(f"结果: {result2}")
    print(f"期望结果: [10]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = 'a'")
    s3 = "a"
    result3 = solution.partitionLabels(s3)
    print(f"结果: {result3}")
    print(f"期望结果: [1]")
