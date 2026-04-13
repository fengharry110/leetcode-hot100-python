"""
56. 合并区间
https://leetcode.cn/problems/merge-intervals/description/

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠，将它们合并为 [1,6]。

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

提示：
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合并所有重叠的区间
        
        参数:
            intervals: 区间数组
            
        返回:
            合并后的区间数组
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [[1,3],[2,6],[8,10],[15,18]]")
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    solution = Solution()
    result1 = solution.merge(intervals1)
    print(f"结果: {result1}")
    print(f"期望结果: [[1,6],[8,10],[15,18]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [[1,4],[4,5]]")
    intervals2 = [[1, 4], [4, 5]]
    result2 = solution.merge(intervals2)
    print(f"结果: {result2}")
    print(f"期望结果: [[1,5]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [[1,5],[2,3]]")
    intervals3 = [[1, 5], [2, 3]]
    result3 = solution.merge(intervals3)
    print(f"结果: {result3}")
    print(f"期望结果: [[1,5]]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [[1,4],[0,4]]")
    intervals4 = [[1, 4], [0, 4]]
    result4 = solution.merge(intervals4)
    print(f"结果: {result4}")
    print(f"期望结果: [[0,4]]")
