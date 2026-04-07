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
"""

from typing import List
from collections import deque


class Solution:
    """
    滑动窗口最大值解法类
    
    解题思路：
        使用单调队列，保持队列头部为当前窗口的最大值
        
    算法步骤：
        1. 初始化双端队列
        2. 遍历数组：
           - 移除队列中小于当前元素的元素
           - 将当前元素的索引加入队列
           - 移除队列中超出窗口范围的元素
           - 当窗口形成后，记录队列头部的元素
        3. 返回结果列表
        
    时间复杂度：O(n)
    空间复杂度：O(k)
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
        if not nums:
            return []
        
        result = []
        deq = deque()
        
        for i, num in enumerate(nums):
            # 移除队列中小于当前元素的元素
            while deq and nums[deq[-1]] < num:
                deq.pop()
            
            # 将当前元素的索引加入队列
            deq.append(i)
            
            # 移除队列中超出窗口范围的元素
            if deq[0] < i - k + 1:
                deq.popleft()
            
            # 当窗口形成后，记录最大值
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result


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
    solution2 = Solution()
    result2 = solution2.maxSlidingWindow(nums2, k2)
    print(f"结果: {result2}")
    print(f"期望结果: [1]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1,-1], k = 1")
    nums3 = [1,-1]
    k3 = 1
    solution3 = Solution()
    result3 = solution3.maxSlidingWindow(nums3, k3)
    print(f"结果: {result3}")
    print(f"期望结果: [1,-1]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: nums = [9,11], k = 2")
    nums4 = [9,11]
    k4 = 2
    solution4 = Solution()
    result4 = solution4.maxSlidingWindow(nums4, k4)
    print(f"结果: {result4}")
    print(f"期望结果: [11]")
