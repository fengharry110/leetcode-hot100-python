"""
11. 盛最多水的容器
https://leetcode.cn/problems/container-with-most-water/description/

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1

提示：
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def maxArea(self, height: List[int]) -> int:
        """
        计算盛最多水的容器
        
        参数:
            height: 高度数组
            
        返回:
            最大水量
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,8,6,2,5,4,8,3,7]")
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    result1 = solution.maxArea(height1)
    print(f"结果: {result1}")
    print(f"期望结果: 49")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [1,1]")
    height2 = [1, 1]
    result2 = solution.maxArea(height2)
    print(f"结果: {result2}")
    print(f"期望结果: 1")
