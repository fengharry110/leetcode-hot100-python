"""
42. 接雨水
https://leetcode.cn/problems/trapping-rain-water/description/

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

提示：
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def trap(self, height: List[int]) -> int:
        """
        计算能接多少雨水
        
        参数:
            height: 高度数组
            
        返回:
            能接的雨水量
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"输入: height = {height1}")
    print(f"输出: {solution.trap(height1)}")
    print(f"期望: 6")
    
    # 测试用例2
    height2 = [4, 2, 0, 3, 2, 5]
    print(f"\n输入: height = {height2}")
    print(f"输出: {solution.trap(height2)}")
    print(f"期望: 9")
