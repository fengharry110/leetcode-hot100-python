"""
394. 字符串解码
https://leetcode.cn/problems/decode-string/description/

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的。输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"

示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

提示：
1 <= s.length <= 30
s 由小写英文字母、数字和方括号 '[]' 组成
s 保证是一个 有效 的输入
s 中所有整数的取值范围为 [1, 300]
"""


class Solution:
    """
    请在此处实现你的解法
    """
    
    def decodeString(self, s: str) -> str:
        """
        解码字符串
        
        参数:
            s: 编码后的字符串
            
        返回:
            解码后的字符串
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: s = '3[a]2[bc]'")
    s1 = "3[a]2[bc]"
    result1 = solution.decodeString(s1)
    print(f"结果: {result1}")
    print(f"期望结果: 'aaabcbc'")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: s = '3[a2[c]]'")
    s2 = "3[a2[c]]"
    result2 = solution.decodeString(s2)
    print(f"结果: {result2}")
    print(f"期望结果: 'accaccacc'")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = '2[abc]3[cd]ef'")
    s3 = "2[abc]3[cd]ef"
    result3 = solution.decodeString(s3)
    print(f"结果: {result3}")
    print(f"期望结果: 'abcabccdcdcdef'")
