"""
215. 数组中的第K个最大元素
https://leetcode.cn/problems/kth-largest-element-in-an-array/description/

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4

提示：
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        找出数组中第k大的元素
        
        参数:
            nums: 整数数组
            k: 第k大
            
        返回:
            第k大的元素
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [3,2,1,5,6,4], k = 2")
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    result1 = solution.findKthLargest(nums1, k1)
    print(f"结果: {result1}")
    print(f"期望结果: 5")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [3,2,3,1,2,4,5,5,6], k = 4")
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    result2 = solution.findKthLargest(nums2, k2)
    print(f"结果: {result2}")
    print(f"期望结果: 4")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1], k = 1")
    nums3 = [1]
    k3 = 1
    result3 = solution.findKthLargest(nums3, k3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
