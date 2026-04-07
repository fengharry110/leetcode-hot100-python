"""
287. 寻找重复数
https://leetcode.cn/problems/find-the-duplicate-number/description/

给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有一个重复的整数，找出这个重复的数。

你必须设计并实现线性时间复杂度 O(n) 且仅使用常量额外空间 O(1) 的算法。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3

示例 3：
输入：nums = [3,3,3,3,3]
输出：3
"""

from typing import List


class Solution:
    """
    寻找重复数解法类
    
    解题思路：
        快慢指针，类似于环形链表的检测
        
    算法步骤：
        1. 初始化慢指针为nums[0]，快指针为nums[nums[0]]
        2. 移动指针，直到快慢指针相遇
        3. 重置慢指针为0，然后同时移动快慢指针，直到再次相遇
        4. 返回相遇的位置
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def findDuplicate(self, nums: List[int]) -> int:
        """
        寻找重复的数
        
        参数:
            nums: 整数数组
            
        返回:
            重复的数
        """
        # 快慢指针
        slow = nums[0]
        fast = nums[nums[0]]
        
        # 找到相遇点
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # 重置慢指针
        slow = 0
        
        # 找到重复的数
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,3,4,2,2]")
    nums1 = [1,3,4,2,2]
    solution = Solution()
    result1 = solution.findDuplicate(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 2")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [3,1,3,4,2]")
    nums2 = [3,1,3,4,2]
    solution2 = Solution()
    result2 = solution2.findDuplicate(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 3")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [3,3,3,3,3]")
    nums3 = [3,3,3,3,3]
    solution3 = Solution()
    result3 = solution3.findDuplicate(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 3")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [2,2,2,2,2]")
    nums4 = [2,2,2,2,2]
    solution4 = Solution()
    result4 = solution4.findDuplicate(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: 2")
