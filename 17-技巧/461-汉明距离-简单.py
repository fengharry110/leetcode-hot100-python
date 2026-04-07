"""
461. 汉明距离
https://leetcode.cn/problems/hamming-distance/description/

两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。

示例 1：
输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。

示例 2：
输入：x = 3, y = 1
输出：1
"""

class Solution:
    """
    汉明距离解法类
    
    解题思路：
        位运算，计算x ^ y的二进制中1的个数
        
    算法步骤：
        1. 计算x和y的异或
        2. 统计异或结果中1的个数
        3. 返回统计结果
        
    时间复杂度：O(logn)
    空间复杂度：O(1)
    """
    
    def hammingDistance(self, x: int, y: int) -> int:
        """
        计算两个整数之间的汉明距离
        
        参数:
            x: 第一个整数
            y: 第二个整数
            
        返回:
            汉明距离
        """
        xor = x ^ y
        count = 0
        while xor:
            xor &= xor - 1
            count += 1
        return count


class SolutionBit:
    """
    位运算解法类
    """
    
    def hammingDistance(self, x: int, y: int) -> int:
        """
        计算两个整数之间的汉明距离（位运算版本）
        
        参数:
            x: 第一个整数
            y: 第二个整数
            
        返回:
            汉明距离
        """
        return bin(x ^ y).count('1')


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: x = 1, y = 4")
    x1 = 1
    y1 = 4
    solution = Solution()
    result1 = solution.hammingDistance(x1, y1)
    print(f"结果: {result1}")
    print(f"期望结果: 2")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: x = 3, y = 1")
    x2 = 3
    y2 = 1
    solution2 = SolutionBit()
    result2 = solution2.hammingDistance(x2, y2)
    print(f"结果: {result2}")
    print(f"期望结果: 1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: x = 0, y = 0")
    x3 = 0
    y3 = 0
    solution3 = Solution()
    result3 = solution3.hammingDistance(x3, y3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: x = 2, y = 3")
    x4 = 2
    y4 = 3
    solution4 = SolutionBit()
    result4 = solution4.hammingDistance(x4, y4)
    print(f"结果: {result4}")
    print(f"期望结果: 1")
