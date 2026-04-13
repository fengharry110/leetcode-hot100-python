"""
189. 轮转数组
https://leetcode.cn/problems/rotate-array/description/

给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]

提示：
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5

进阶：你可以使用空间复杂度为 O(1) 的原地算法解决这个问题吗？
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        将数组中的元素向右轮转 k 个位置
        
        参数:
            nums: 整数数组
            k: 轮转位置数
            
        返回:
            None（原地修改数组）
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,2,3,4,5,6,7], k=3")
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    solution = Solution()
    solution.rotate(nums1, 3)
    print(f"结果: {nums1}")
    print(f"期望结果: [5,6,7,1,2,3,4]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [-1,-100,3,99], k=2")
    nums2 = [-1, -100, 3, 99]
    solution.rotate(nums2, 2)
    print(f"结果: {nums2}")
    print(f"期望结果: [3,99,-1,-100]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1,2], k=3")
    nums3 = [1, 2]
    solution.rotate(nums3, 3)
    print(f"结果: {nums3}")
    print(f"期望结果: [2,1]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1], k=0")
    nums4 = [1]
    solution.rotate(nums4, 0)
    print(f"结果: {nums4}")
    print(f"期望结果: [1]")
