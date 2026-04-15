"""
70. 爬楼梯
https://leetcode.cn/problems/climbing-stairs/description/

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

提示：
1 <= n <= 45
"""


class Solution:
    """
    请在此处实现你的解法
    """
    
    def climbStairs(self, n: int) -> int:
        """
        计算爬到楼顶的方法数
        
        参数:
            n: 楼梯阶数
            
        返回:
            不同的方法数
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: n = 2")
    n1 = 2
    result1 = solution.climbStairs(n1)
    print(f"结果: {result1}")
    print(f"期望结果: 2")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: n = 3")
    n2 = 3
    result2 = solution.climbStairs(n2)
    print(f"结果: {result2}")
    print(f"期望结果: 3")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: n = 1")
    n3 = 1
    result3 = solution.climbStairs(n3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
