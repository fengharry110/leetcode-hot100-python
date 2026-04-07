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
"""

from typing import List


class Solution:
    """
    盛最多水的容器解法类
    
    解题思路：
        使用双指针法，从两端向中间移动，每次移动较矮的一端
        
    算法步骤：
        1. 初始化左指针为0，右指针为数组长度-1
        2. 初始化最大面积为0
        3. 当左指针小于右指针时：
           - 计算当前面积：min(height[left], height[right]) * (right - left)
           - 更新最大面积
           - 如果左指针的高度小于右指针的高度，左指针右移
           - 否则，右指针左移
        4. 返回最大面积
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def maxArea(self, height: List[int]) -> int:
        """
        计算盛最多水的容器
        
        参数:
            height: 高度数组
            
        返回:
            最大水量
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # 计算当前面积
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width
            
            # 更新最大面积
            if current_area > max_area:
                max_area = current_area
            
            # 移动较矮的一端
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,8,6,2,5,4,8,3,7]")
    height1 = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    result1 = solution.maxArea(height1)
    print(f"结果: {result1}")
    print(f"期望结果: 49")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [1,1]")
    height2 = [1, 1]
    solution2 = Solution()
    result2 = solution2.maxArea(height2)
    print(f"结果: {result2}")
    print(f"期望结果: 1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [4,3,2,1,4]")
    height3 = [4, 3, 2, 1, 4]
    solution3 = Solution()
    result3 = solution3.maxArea(height3)
    print(f"结果: {result3}")
    print(f"期望结果: 16")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1,2,1]")
    height4 = [1, 2, 1]
    solution4 = Solution()
    result4 = solution4.maxArea(height4)
    print(f"结果: {result4}")
    print(f"期望结果: 2")
