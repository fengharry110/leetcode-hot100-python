"""
191. 位1的个数
https://leetcode.cn/problems/number-of-1-bits/description/

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

示例 1：
输入：n = 00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

示例 2：
输入：n = 00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。

示例 3：
输入：n = 11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
"""

class Solution:
    """
    位1的个数解法类
    
    解题思路：
        位运算，使用n & (n-1)消除最后一位1
        
    算法步骤：
        1. 初始化计数为0
        2. 循环直到n为0：
           - n = n & (n-1)
           - 计数加1
        3. 返回计数
        
    时间复杂度：O(logn)
    空间复杂度：O(1)
    """
    
    def hammingWeight(self, n: int) -> int:
        """
        计算二进制中1的个数
        
        参数:
            n: 无符号整数
            
        返回:
            1的个数
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


class SolutionBit:
    """
    位运算解法类
    """
    
    def hammingWeight(self, n: int) -> int:
        """
        计算二进制中1的个数（位运算版本）
        
        参数:
            n: 无符号整数
            
        返回:
            1的个数
        """
        count = 0
        for i in range(32):
            if n & (1 << i):
                count += 1
        return count


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: n = 00000000000000000000000000001011")
    n1 = 0b00000000000000000000000000001011
    solution = Solution()
    result1 = solution.hammingWeight(n1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: n = 00000000000000000000000010000000")
    n2 = 0b00000000000000000000000010000000
    solution2 = SolutionBit()
    result2 = solution2.hammingWeight(n2)
    print(f"结果: {result2}")
    print(f"期望结果: 1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: n = 11111111111111111111111111111101")
    n3 = 0b11111111111111111111111111111101
    solution3 = Solution()
    result3 = solution3.hammingWeight(n3)
    print(f"结果: {result3}")
    print(f"期望结果: 31")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: n = 0")
    n4 = 0
    solution4 = SolutionBit()
    result4 = solution4.hammingWeight(n4)
    print(f"结果: {result4}")
    print(f"期望结果: 0")
