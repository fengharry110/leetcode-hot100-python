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
"""

from typing import List
import heapq
from collections import Counter


class Solution:
    """
    前K个高频元素解法类
    
    解题思路：
        使用堆，维护一个大小为k的最小堆
        
    算法步骤：
        1. 统计每个元素的频率
        2. 使用最小堆，遍历频率字典：
           - 将元素和频率加入堆
           - 如果堆的大小超过k，弹出最小元素
        3. 从堆中提取元素，反转顺序
        
    时间复杂度：O(nlogk)
    空间复杂度：O(n)
    """
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        前K个高频元素
        
        参数:
            nums: 整数数组
            k: 前k个
            
        返回:
            前k个高频元素
        """
        # 统计频率
        freq = Counter(nums)
        
        # 使用最小堆
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 提取结果
        return [num for count, num in reversed(heap)]


class SolutionBucketSort:
    """
    桶排序解法类
    """
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        前K个高频元素（桶排序版本）
        
        参数:
            nums: 整数数组
            k: 前k个
            
        返回:
            前k个高频元素
        """
        # 统计频率
        freq = Counter(nums)
        
        # 桶排序
        max_freq = max(freq.values())
        buckets = [[] for _ in range(max_freq + 1)]
        
        for num, count in freq.items():
            buckets[count].append(num)
        
        # 收集结果
        result = []
        for i in range(max_freq, 0, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                break
        
        return result[:k]


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [1,1,1,2,2,3], k = 2")
    nums1 = [1,1,1,2,2,3]
    k1 = 2
    solution = Solution()
    result1 = solution.topKFrequent(nums1, k1)
    print(f"结果: {result1}")
    print(f"期望结果: [1,2]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [1], k = 1")
    nums2 = [1]
    k2 = 1
    solution2 = SolutionBucketSort()
    result2 = solution2.topKFrequent(nums2, k2)
    print(f"结果: {result2}")
    print(f"期望结果: [1]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1,2,3,4,5,5,5,6,6,6,6], k = 2")
    nums3 = [1,2,3,4,5,5,5,6,6,6,6]
    k3 = 2
    solution3 = Solution()
    result3 = solution3.topKFrequent(nums3, k3)
    print(f"结果: {result3}")
    print(f"期望结果: [6,5]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: nums = [3,0,1,0], k = 1")
    nums4 = [3,0,1,0]
    k4 = 1
    solution4 = SolutionBucketSort()
    result4 = solution4.topKFrequent(nums4, k4)
    print(f"结果: {result4}")
    print(f"期望结果: [0]")
