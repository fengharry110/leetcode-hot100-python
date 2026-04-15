"""
4. 寻找两个正序数组的中位数
https://leetcode.cn/problems/median-of-two-sorted-arrays/description/

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        找出两个正序数组的中位数
        
        参数:
            nums1: 第一个正序数组
            nums2: 第二个正序数组
            
        返回:
            中位数
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums1 = [1,3], nums2 = [2]")
    nums1_1 = [1, 3]
    nums2_1 = [2]
    result1 = solution.findMedianSortedArrays(nums1_1, nums2_1)
    print(f"结果: {result1}")
    print(f"期望结果: 2.00000")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums1 = [1,2], nums2 = [3,4]")
    nums1_2 = [1, 2]
    nums2_2 = [3, 4]
    result2 = solution.findMedianSortedArrays(nums1_2, nums2_2)
    print(f"结果: {result2}")
    print(f"期望结果: 2.50000")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums1 = [], nums2 = [1]")
    nums1_3 = []
    nums2_3 = [1]
    result3 = solution.findMedianSortedArrays(nums1_3, nums2_3)
    print(f"结果: {result3}")
    print(f"期望结果: 1.00000")
