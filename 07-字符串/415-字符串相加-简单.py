"""
415. 字符串相加
https://leetcode.cn/problems/add-strings/description/

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。

示例 1：
输入：num1 = "11", num2 = "123"
输出："134"

示例 2：
输入：num1 = "456", num2 = "77"
输出："533"

示例 3：
输入：num1 = "0", num2 = "0"
输出："0"
"""

class Solution:
    """
    字符串相加解法类
    
    解题思路：
        模拟手工加法，从右往左逐位相加
        
    算法步骤：
        1. 初始化指针i和j分别指向num1和num2的末尾
        2. 初始化进位carry为0
        3. 循环处理每一位：
           - 计算当前位的和
           - 更新进位
           - 将当前位的数字添加到结果中
        4. 处理最后的进位
        5. 反转结果字符串
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def addStrings(self, num1: str, num2: str) -> str:
        """
        字符串相加
        
        参数:
            num1: 第一个数字的字符串形式
            num2: 第二个数字的字符串形式
            
        返回:
            两数之和的字符串形式
        """
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry > 0:
            # 获取当前位的数字
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # 计算当前位的和
            total = digit1 + digit2 + carry
            
            # 更新进位
            carry = total // 10
            
            # 将当前位的数字添加到结果中
            result.append(str(total % 10))
            
            # 移动指针
            i -= 1
            j -= 1
        
        # 反转结果字符串
        return ''.join(reversed(result))


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: num1 = \"11\", num2 = \"123\"")
    num1_1 = "11"
    num2_1 = "123"
    solution = Solution()
    result1 = solution.addStrings(num1_1, num2_1)
    print(f"结果: {result1}")
    print(f"期望结果: \"134\"")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: num1 = \"456\", num2 = \"77\"")
    num1_2 = "456"
    num2_2 = "77"
    solution2 = Solution()
    result2 = solution2.addStrings(num1_2, num2_2)
    print(f"结果: {result2}")
    print(f"期望结果: \"533\"")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: num1 = \"0\", num2 = \"0\"")
    num1_3 = "0"
    num2_3 = "0"
    solution3 = Solution()
    result3 = solution3.addStrings(num1_3, num2_3)
    print(f"结果: {result3}")
    print(f"期望结果: \"0\"")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: num1 = \"999\", num2 = \"1\"")
    num1_4 = "999"
    num2_4 = "1"
    solution4 = Solution()
    result4 = solution4.addStrings(num1_4, num2_4)
    print(f"结果: {result4}")
    print(f"期望结果: \"1000\"")
