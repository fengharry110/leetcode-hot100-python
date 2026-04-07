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
"""

from typing import List


class Solution:
    """
    打家劫舍解法类
    
    解题思路：
        使用动态规划，状态转移方程为：dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
    算法步骤：
        1. 处理边界情况：数组为空返回0，数组长度为1返回第一个元素
        2. 初始化dp数组，dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        3. 遍历数组从索引2开始：
           - dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        4. 返回dp[-1]
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def rob(self, nums: List[int]) -> int:
        """
        计算最大偷窃金额
        
        参数:
            nums: 房屋金额数组
            
        返回:
            最大偷窃金额
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        # 初始化dp数组
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # 状态转移
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]


class SolutionOptimized:
    """
    空间优化的打家劫舍解法类
    
    解题思路：
        使用两个变量代替dp数组，优化空间复杂度
        
    算法步骤：
        1. 处理边界情况
        2. 初始化prev1和prev2，分别表示前一个和前前一个的最大金额
        3. 遍历数组：
           - current = max(prev1, prev2 + nums[i])
           - 更新prev2和prev1
        4. 返回prev1
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def rob(self, nums: List[int]) -> int:
        """
        计算最大偷窃金额（空间优化版本）
        
        参数:
            nums: 房屋金额数组
            
        返回:
            最大偷窃金额
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        # 初始化变量
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        # 状态转移
        for i in range(2, n):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        
        return prev1


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,2,3,1]")
    nums1 = [1, 2, 3, 1]
    solution = Solution()
    result1 = solution.rob(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 4")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [2,7,9,3,1]")
    nums2 = [2, 7, 9, 3, 1]
    solution2 = SolutionOptimized()
    result2 = solution2.rob(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 12")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [2,1,1,2]")
    nums3 = [2, 1, 1, 2]
    solution3 = Solution()
    result3 = solution3.rob(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 4")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1,3,1,3,100]")
    nums4 = [1, 3, 1, 3, 100]
    solution4 = SolutionOptimized()
    result4 = solution4.rob(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: 103")
