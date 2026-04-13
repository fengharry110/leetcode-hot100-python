# 153. 寻找旋转排序数组中的最小值
# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。
# 给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，
# 并按上述情形进行了多次旋转。请你找出并返回数组中的最小元素。
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
#
# 示例 1：
# 输入：nums = [3,4,5,1,2]
# 输出：1
#
# 示例 2：
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0
#
# 示例 3：
# 输入：nums = [11,13,15,17]
# 输出：11

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # 最小值在右半部分
                left = mid + 1
            else:
                # 最小值在左半部分（包含mid）
                right = mid
        
        return nums[left]


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    print(f"测试1结果: {solution.findMin([3, 4, 5, 1, 2])}")  # 期望输出: 1
    
    # 测试2
    print(f"测试2结果: {solution.findMin([4, 5, 6, 7, 0, 1, 2])}")  # 期望输出: 0
    
    # 测试3
    print(f"测试3结果: {solution.findMin([11, 13, 15, 17])}")  # 期望输出: 11
