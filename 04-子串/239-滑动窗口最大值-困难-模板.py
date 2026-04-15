"""
239. 滑动窗口最大值
https://leetcode.cn/problems/sliding-window-maximum/description/

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               ------
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]

提示：
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

from typing import List
from collections import deque


class Solution:
    """
    请在此处实现你的解法
    """
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        计算滑动窗口的最大值
        
        参数:
            nums: 整数数组
            k: 窗口大小
            
        返回:
            滑动窗口的最大值列表
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [1,3,-1,-3,5,3,6,7], k = 3")
    nums1 = [1,3,-1,-3,5,3,6,7]
    k1 = 3
    solution = Solution()
    result1 = solution.maxSlidingWindow(nums1, k1)
    print(f"结果: {result1}")
    print(f"期望结果: [3,3,5,5,6,7]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [1], k = 1")
    nums2 = [1]
    k2 = 1
    result2 = solution.maxSlidingWindow(nums2, k2)
    print(f"结果: {result2}")
    print(f"期望结果: [1]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1,-1], k = 1")
    nums3 = [1,-1]
    k3 = 1
    result3 = solution.maxSlidingWindow(nums3, k3)
    print(f"结果: {result3}")
    print(f"期望结果: [1,-1]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: nums = [9,11], k = 2")
    nums4 = [9,11]
    k4 = 2
    result4 = solution.maxSlidingWindow(nums4, k4)
    print(f"结果: {result4}")
    print(f"期望结果: [11]")
