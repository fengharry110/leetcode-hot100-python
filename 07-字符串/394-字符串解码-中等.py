"""
394. 字符串解码
https://leetcode.cn/problems/decode-string/description/

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

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

示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
"""

class Solution:
    """
    字符串解码解法类
    
    解题思路：
        使用栈，分别存储数字和字符串
        
    算法步骤：
        1. 初始化数字栈和字符串栈
        2. 遍历字符串：
           - 如果是数字，累计计算数字
           - 如果是'['，将数字和当前字符串入栈，重置
           - 如果是']'，弹出数字和字符串，将当前字符串重复数字次后与弹出的字符串拼接
           - 否则，将字符添加到当前字符串
        3. 返回当前字符串
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def decodeString(self, s: str) -> str:
        """
        解码字符串
        
        参数:
            s: 编码后的字符串
            
        返回:
            解码后的字符串
        """
        num_stack = []  # 存储数字
        str_stack = []  # 存储字符串
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                # 累计数字
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # 入栈
                num_stack.append(current_num)
                str_stack.append(current_str)
                # 重置
                current_num = 0
                current_str = ""
            elif char == ']':
                # 出栈
                num = num_stack.pop()
                prev_str = str_stack.pop()
                # 拼接字符串
                current_str = prev_str + current_str * num
            else:
                # 普通字符
                current_str += char
        
        return current_str


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: \"3[a]2[bc]\"")
    s1 = "3[a]2[bc]"
    solution = Solution()
    result1 = solution.decodeString(s1)
    print(f"结果: {result1}")
    print(f"期望结果: \"aaabcbc\"")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: \"3[a2[c]]\"")
    s2 = "3[a2[c]]"
    solution2 = Solution()
    result2 = solution2.decodeString(s2)
    print(f"结果: {result2}")
    print(f"期望结果: \"accaccacc\"")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: \"2[abc]3[cd]ef\"")
    s3 = "2[abc]3[cd]ef"
    solution3 = Solution()
    result3 = solution3.decodeString(s3)
    print(f"结果: {result3}")
    print(f"期望结果: \"abcabccdcdcdef\"")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: \"abc3[cd]xyz\"")
    s4 = "abc3[cd]xyz"
    solution4 = Solution()
    result4 = solution4.decodeString(s4)
    print(f"结果: {result4}")
    print(f"期望结果: \"abccdcdcdxyz\"")
