"""
56. 合并区间
https://leetcode.cn/problems/merge-intervals/description/

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠，将它们合并为 [1,6]。

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

from typing import List


class Solution:
    """
    合并区间解法类
    
    解题思路：
        贪心算法，按照区间的开始坐标排序，然后合并重叠的区间
        
    算法步骤：
        1. 按照区间的开始坐标排序
        2. 初始化结果列表，将第一个区间加入结果
        3. 遍历剩余区间：
           - 如果当前区间的开始坐标小于等于结果列表最后一个区间的结束坐标，说明有重叠，合并区间
           - 否则，将当前区间加入结果列表
        4. 返回结果列表
        
    时间复杂度：O(nlogn)
    空间复杂度：O(n)
    """
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合并重叠的区间
        
        参数:
            intervals: 区间数组
            
        返回:
            合并后的区间数组
        """
        if not intervals:
            return []
        
        # 按照区间的开始坐标排序
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current = intervals[i]
            last = result[-1]
            
            # 如果有重叠，合并区间
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                result.append(current)
        
        return result


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [[1,3],[2,6],[8,10],[15,18]]")
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    solution = Solution()
    result1 = solution.merge(intervals1)
    print(f"结果: {result1}")
    print(f"期望结果: [[1,6],[8,10],[15,18]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [[1,4],[4,5]]")
    intervals2 = [[1,4],[4,5]]
    solution2 = Solution()
    result2 = solution2.merge(intervals2)
    print(f"结果: {result2}")
    print(f"期望结果: [[1,5]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [[1,5],[2,3]]")
    intervals3 = [[1,5],[2,3]]
    solution3 = Solution()
    result3 = solution3.merge(intervals3)
    print(f"结果: {result3}")
    print(f"期望结果: [[1,5]]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: []")
    intervals4 = []
    solution4 = Solution()
    result4 = solution4.merge(intervals4)
    print(f"结果: {result4}")
    print(f"期望结果: []")
