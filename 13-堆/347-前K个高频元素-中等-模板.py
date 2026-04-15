"""
347. 前K个高频元素
https://leetcode.cn/problems/top-k-frequent-elements/description/

给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

提示：
1 <= nums.length <= 10^5
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        找出出现频率前k高的元素
        
        参数:
            nums: 整数数组
            k: 前k个
            
        返回:
            前k个高频元素
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [1,1,1,2,2,3], k = 2")
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = solution.topKFrequent(nums1, k1)
    print(f"结果: {result1}")
    print(f"期望结果: [1, 2]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [1], k = 1")
    nums2 = [1]
    k2 = 1
    result2 = solution.topKFrequent(nums2, k2)
    print(f"结果: {result2}")
    print(f"期望结果: [1]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1,1,2,2,3,3,3], k = 2")
    nums3 = [1, 1, 2, 2, 3, 3, 3]
    k3 = 2
    result3 = solution.topKFrequent(nums3, k3)
    print(f"结果: {result3}")
    print(f"期望结果: [3, 1] 或 [3, 2]")
