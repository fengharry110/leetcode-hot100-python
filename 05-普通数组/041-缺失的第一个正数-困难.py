# 41. 缺失的第一个正数
# 给你一个未排序的整数数组 nums，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
#
# 示例 1：
# 输入：nums = [1,2,0]
# 输出：3
#
# 示例 2：
# 输入：nums = [3,4,-1,1]
# 输出：2
#
# 示例 3：
# 输入：nums = [7,8,9,11,12]
# 输出：1
#
# 提示：
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 将所有负数和0替换为n+1（因为结果最大是n+1）
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        # 对于每个在[1, n]范围内的数字num，将nums[num-1]标记为负数
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        
        # 找到第一个正数，其下标+1就是答案
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # 如果所有位置都被标记，答案是n+1
        return n + 1


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    nums1 = [1, 2, 0]
    print(f"测试1结果: {solution.firstMissingPositive(nums1)}")  # 期望输出: 3
    
    # 测试2
    nums2 = [3, 4, -1, 1]
    print(f"测试2结果: {solution.firstMissingPositive(nums2)}")  # 期望输出: 2
    
    # 测试3
    nums3 = [7, 8, 9, 11, 12]
    print(f"测试3结果: {solution.firstMissingPositive(nums3)}")  # 期望输出: 1
