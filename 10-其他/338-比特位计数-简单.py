"""
338. 比特位计数
https://leetcode.cn/problems/counting-bits/description/

给你一个整数 n ，对于 0 ≤ i ≤ n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

示例 1：
输入：n = 2
输出：[0,1,1]
解释：
0 → 0
1 → 1
2 → 10

示例 2：
输入：n = 5
输出：[0,1,1,2,1,2]
解释：
0 → 0
1 → 1
2 → 10
3 → 11
4 → 100
5 → 101
"""

from typing import List


class Solution:
    """
    比特位计数解法类
    
    解题思路：
        动态规划，利用已计算的结果
        
    算法步骤：
        1. 初始化结果数组，ans[0] = 0
        2. 对于每个数i：
           - 如果i是偶数，ans[i] = ans[i // 2]
           - 如果i是奇数，ans[i] = ans[i - 1] + 1
        3. 返回结果数组
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def countBits(self, n: int) -> List[int]:
        """
        计算0到n的每个数的二进制中1的个数
        
        参数:
            n: 整数
            
        返回:
            结果数组
        """
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            if i % 2 == 0:
                ans[i] = ans[i // 2]
            else:
                ans[i] = ans[i - 1] + 1
        
        return ans


class SolutionDP:
    """
    动态规划解法类
    """
    
    def countBits(self, n: int) -> List[int]:
        """
        计算0到n的每个数的二进制中1的个数（动态规划版本）
        
        参数:
            n: 整数
            
        返回:
            结果数组
        """
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1
        
        return ans


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: n = 2")
    n1 = 2
    solution = Solution()
    result1 = solution.countBits(n1)
    print(f"结果: {result1}")
    print(f"期望结果: [0,1,1]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: n = 5")
    n2 = 5
    solution2 = SolutionDP()
    result2 = solution2.countBits(n2)
    print(f"结果: {result2}")
    print(f"期望结果: [0,1,1,2,1,2]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: n = 0")
    n3 = 0
    solution3 = Solution()
    result3 = solution3.countBits(n3)
    print(f"结果: {result3}")
    print(f"期望结果: [0]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: n = 10")
    n4 = 10
    solution4 = SolutionDP()
    result4 = solution4.countBits(n4)
    print(f"结果: {result4}")
    print(f"期望结果: [0,1,1,2,1,2,2,3,1,2,2]")
