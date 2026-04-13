# 45. 跳跃游戏 II
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。
# 返回到达 nums[n - 1] 的最小跳跃次数。
#
# 示例 1:
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。从下标 0 跳到下标 1，跳 1 步，然后跳 3 步到达最后一个位置。
#
# 示例 2:
# 输入: nums = [2,3,0,1,4]
# 输出: 2

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                if current_end >= n - 1:
                    break
        
        return jumps


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    print(f"测试1结果: {solution.jump([2, 3, 1, 1, 4])}")  # 期望输出: 2
    
    # 测试2
    print(f"测试2结果: {solution.jump([2, 3, 0, 1, 4])}")  # 期望输出: 2
