# 189. 轮转数组
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
#
# 示例 1:
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
#
# 示例 2:
# 输入: nums = [-1,-100,3,99], k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
#
# 提示：
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # 处理k大于n的情况
        
        # 三次反转法
        # 1. 反转整个数组
        self.reverse(nums, 0, n - 1)
        # 2. 反转前k个元素
        self.reverse(nums, 0, k - 1)
        # 3. 反转后n-k个元素
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums1, 3)
    print(f"测试1结果: {nums1}")  # 期望输出: [5, 6, 7, 1, 2, 3, 4]
    
    # 测试2
    nums2 = [-1, -100, 3, 99]
    solution.rotate(nums2, 2)
    print(f"测试2结果: {nums2}")  # 期望输出: [3, 99, -1, -100]
