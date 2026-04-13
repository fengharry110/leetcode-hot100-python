"""
253. 会议室 II
中等
给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回 所需会议室的最小数量 。

示例 1：
输入：intervals = [[0,30],[5,10],[15,20]]
输出：2

示例 2：
输入：intervals = [[7,10],[2,4]]
输出：1

提示：
1 <= intervals.length <= 10^4
0 <= starti < endi <= 10^6
"""

from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 按开始时间排序
        intervals.sort(key=lambda x: x[0])
        
        # 使用最小堆存储会议结束时间
        heap = []
        heapq.heappush(heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            # 如果最早结束的会议已经结束，可以复用会议室
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            
            # 添加当前会议的结束时间
            heapq.heappush(heap, intervals[i][1])
        
        return len(heap)


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    intervals1 = [[0, 30], [5, 10], [15, 20]]
    print(f"输入: intervals = {intervals1}")
    print(f"输出: {solution.minMeetingRooms(intervals1)}")
    
    # 测试用例2
    intervals2 = [[7, 10], [2, 4]]
    print(f"\n输入: intervals = {intervals2}")
    print(f"输出: {solution.minMeetingRooms(intervals2)}")
