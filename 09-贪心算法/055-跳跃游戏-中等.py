"""
55. 跳跃游戏
https://leetcode.cn/problems/jump-game/description/

给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
"""

from typing import List


class Solution:
    """
    贪心解法类
    
    解题思路：
        维护一个最远可达的位置，遍历数组，不断更新最远可达位置
        如果当前位置超过最远可达位置，说明无法到达
        如果最远可达位置超过或等于最后一个下标，说明可以到达
        
    算法步骤：
        1. 初始化最远可达位置为0
        2. 遍历数组中的每个位置i：
           - 如果i超过最远可达位置，返回false
           - 更新最远可达位置为max(最远可达位置, i + nums[i])
           - 如果最远可达位置 >= 最后一个下标，返回true
        3. 遍历结束后，返回true
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def canJump(self, nums: List[int]) -> bool:
        """
        判断是否能够到达最后一个下标
        
        参数:
            nums: 非负整数数组
            
        返回:
            是否能够到达最后一个下标
        """
        n = len(nums)
        max_reach = 0
        
        for i in range(n):
            # 如果当前位置超过了最远可达位置，说明无法到达
            if i > max_reach:
                return False
            
            # 更新最远可达位置
            max_reach = max(max_reach, i + nums[i])
            
            # 如果已经可以到达最后一个下标，直接返回
            if max_reach >= n - 1:
                return True
        
        return True


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [2,3,1,1,4]")
    nums1 = [2, 3, 1, 1, 4]
    solution = Solution()
    result1 = solution.canJump(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [3,2,1,0,4]")
    nums2 = [3, 2, 1, 0, 4]
    solution2 = Solution()
    result2 = solution2.canJump(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [0]")
    nums3 = [0]
    solution3 = Solution()
    result3 = solution3.canJump(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [2,0,0]")
    nums4 = [2, 0, 0]
    solution4 = Solution()
    result4 = solution4.canJump(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: True")
    
    # 测试用例5
    print("\n" + "=" * 50)
    print("测试用例5: [1,1,1,1]")
    nums5 = [1, 1, 1, 1]
    solution5 = Solution()
    result5 = solution5.canJump(nums5)
    print(f"结果: {result5}")
    print(f"期望结果: True")
