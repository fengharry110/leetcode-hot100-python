"""
55. 跳跃游戏
https://leetcode.cn/problems/jump-game/description/

给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

提示：
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def canJump(self, nums: List[int]) -> bool:
        """
        判断是否能到达最后一个下标
        
        参数:
            nums: 跳跃数组
            
        返回:
            是否能到达
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [2,3,1,1,4]")
    nums1 = [2, 3, 1, 1, 4]
    result1 = solution.canJump(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [3,2,1,0,4]")
    nums2 = [3, 2, 1, 0, 4]
    result2 = solution.canJump(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [0]")
    nums3 = [0]
    result3 = solution.canJump(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
