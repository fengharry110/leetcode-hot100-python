"""
198. 打家劫舍
https://leetcode.cn/problems/house-robber/description/

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def rob(self, nums: List[int]) -> int:
        """
        计算能偷窃到的最高金额
        
        参数:
            nums: 各房屋金额数组
            
        返回:
            最高金额
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [1,2,3,1]")
    nums1 = [1, 2, 3, 1]
    result1 = solution.rob(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 4")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [2,7,9,3,1]")
    nums2 = [2, 7, 9, 3, 1]
    result2 = solution.rob(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 12")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1]")
    nums3 = [1]
    result3 = solution.rob(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
