"""
283. 移动零
https://leetcode.cn/problems/move-zeroes/description/

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]
"""

from typing import List


class Solution:
    """
    移动零解法类
    
    解题思路：
        使用双指针，快指针遍历数组，慢指针指向非零元素的位置
        
    算法步骤：
        1. 初始化慢指针为0
        2. 遍历数组，对于每个元素：
           - 如果元素非零，将其移动到慢指针位置，慢指针+1
        3. 遍历结束后，将慢指针及之后的位置填充为0
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        移动零到数组末尾
        
        参数:
            nums: 整数数组
            
        返回:
            None（原地修改）
        """
        n = len(nums)
        slow = 0
        
        # 移动非零元素
        for fast in range(n):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        
        # 填充零
        while slow < n:
            nums[slow] = 0
            slow += 1


class SolutionSwap:
    """
    交换解法类
    
    解题思路：
        使用双指针，交换零和非零元素
        
    算法步骤：
        1. 初始化慢指针为0
        2. 遍历数组，对于每个元素：
           - 如果元素非零，与慢指针位置交换，慢指针+1
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        移动零到数组末尾（交换版本）
        
        参数:
            nums: 整数数组
            
        返回:
            None（原地修改）
        """
        n = len(nums)
        slow = 0
        
        for fast in range(n):
            if nums[fast] != 0:
                # 交换元素
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [0,1,0,3,12]")
    nums1 = [0,1,0,3,12]
    solution = Solution()
    solution.moveZeroes(nums1)
    print(f"结果: {nums1}")
    print(f"期望结果: [1,3,12,0,0]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [0]")
    nums2 = [0]
    solution2 = Solution()
    solution2.moveZeroes(nums2)
    print(f"结果: {nums2}")
    print(f"期望结果: [0]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1,0,1]")
    nums3 = [1,0,1]
    solution3 = SolutionSwap()
    solution3.moveZeroes(nums3)
    print(f"结果: {nums3}")
    print(f"期望结果: [1,1,0]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [0,0,1]")
    nums4 = [0,0,1]
    solution4 = SolutionSwap()
    solution4.moveZeroes(nums4)
    print(f"结果: {nums4}")
    print(f"期望结果: [1,0,0]")
