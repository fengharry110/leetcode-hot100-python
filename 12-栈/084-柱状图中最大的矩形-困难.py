"""
84. 柱状图中最大的矩形
困难
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例 1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：该矩形的高度为 10，宽度为 2（柱子 5 和 6）。

示例 2：
输入：heights = [2,4]
输出：4

提示：
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # 单调栈：存储下标，高度递增
        stack = []
        max_area = 0
        
        for i in range(n + 1):
            # 添加一个高度为0的哨兵，处理剩余栈元素
            h = heights[i] if i < n else 0
            
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        return max_area


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    heights1 = [2, 1, 5, 6, 2, 3]
    print(f"输入: heights = {heights1}")
    print(f"输出: {solution.largestRectangleArea(heights1)}")
    
    # 测试用例2
    heights2 = [2, 4]
    print(f"\n输入: heights = {heights2}")
    print(f"输出: {solution.largestRectangleArea(heights2)}")
