"""
84. 柱状图中最大的矩形
https://leetcode.cn/problems/largest-rectangle-in-histogram/description/

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例 1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10

示例 2：
输入：heights = [2,4]
输出：4

提示：
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        计算柱状图中最大的矩形面积
        
        参数:
            heights: 柱子高度数组
            
        返回:
            最大矩形面积
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: heights = [2,1,5,6,2,3]")
    heights1 = [2, 1, 5, 6, 2, 3]
    result1 = solution.largestRectangleArea(heights1)
    print(f"结果: {result1}")
    print(f"期望结果: 10")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: heights = [2,4]")
    heights2 = [2, 4]
    result2 = solution.largestRectangleArea(heights2)
    print(f"结果: {result2}")
    print(f"期望结果: 4")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: heights = [1]")
    heights3 = [1]
    result3 = solution.largestRectangleArea(heights3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
