"""
128. 最长连续序列
https://leetcode.cn/problems/longest-consecutive-sequence/description/

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

提示：
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        找出最长连续序列的长度
        
        参数:
            nums: 未排序的整数数组
            
        返回:
            最长连续序列的长度
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [100,4,200,1,3,2]")
    nums1 = [100, 4, 200, 1, 3, 2]
    solution = Solution()
    result1 = solution.longestConsecutive(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 4")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [0,3,7,2,5,8,4,6,0,1]")
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result2 = solution.longestConsecutive(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 9")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: []")
    nums3 = []
    result3 = solution.longestConsecutive(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
