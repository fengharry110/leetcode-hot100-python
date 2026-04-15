"""
279. 完全平方数
https://leetcode.cn/problems/perfect-squares/description/

给你一个整数 n ，返回和为 n 的完全平方数的最少数量。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

提示：
1 <= n <= 10^4
"""


class Solution:
    """
    请在此处实现你的解法
    """
    
    def numSquares(self, n: int) -> int:
        """
        返回和为n的完全平方数的最少数量
        
        参数:
            n: 目标整数
            
        返回:
            最少数量
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: n = 12")
    n1 = 12
    result1 = solution.numSquares(n1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: n = 13")
    n2 = 13
    result2 = solution.numSquares(n2)
    print(f"结果: {result2}")
    print(f"期望结果: 2")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: n = 1")
    n3 = 1
    result3 = solution.numSquares(n3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
