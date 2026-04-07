"""
452. 用最少数量的箭引爆气球
https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/description/

有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，其中 points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend 之间的气球。你不知道气球的确切 y 坐标。

一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。

给你一个数组 points ，返回引爆所有气球所必须射出的最小弓箭数。

示例 1：
输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：气球可以用2支箭来爆破:
- 在x = 6处射出箭，击破气球[2,8]和[1,6]。
- 在x = 11处发射箭，击破气球[10,16]和[7,12]。

示例 2：
输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
解释：每个气球需要射出一支箭，总共需要4支箭。

示例 3：
输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2
解释：气球可以用2支箭来爆破:
- 在x = 2处发射箭，击破气球[1,2]和[2,3]。
- 在x = 4处发射箭，击破气球[3,4]和[4,5]。
"""

from typing import List


class Solution:
    """
    用最少数量的箭引爆气球解法类
    
    解题思路：
        贪心算法，按照气球的结束坐标排序，然后尽可能多地覆盖气球
        
    算法步骤：
        1. 按照气球的结束坐标排序
        2. 初始化箭的位置为第一个气球的结束坐标
        3. 遍历气球，如果当前气球的开始坐标大于箭的位置，说明需要新的箭，更新箭的位置为当前气球的结束坐标
        4. 返回箭的数量
        
    时间复杂度：O(nlogn)
    空间复杂度：O(1)
    """
    
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        计算引爆所有气球所需的最小弓箭数
        
        参数:
            points: 气球的坐标数组
            
        返回:
            最小弓箭数
        """
        if not points:
            return 0
        
        # 按照结束坐标排序
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_end = points[0][1]
        
        for i in range(1, len(points)):
            # 如果当前气球的开始坐标大于当前箭的位置，需要新的箭
            if points[i][0] > current_end:
                arrows += 1
                current_end = points[i][1]
        
        return arrows


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [[10,16],[2,8],[1,6],[7,12]]")
    points1 = [[10,16],[2,8],[1,6],[7,12]]
    solution = Solution()
    result1 = solution.findMinArrowShots(points1)
    print(f"结果: {result1}")
    print(f"期望结果: 2")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [[1,2],[3,4],[5,6],[7,8]]")
    points2 = [[1,2],[3,4],[5,6],[7,8]]
    solution2 = Solution()
    result2 = solution2.findMinArrowShots(points2)
    print(f"结果: {result2}")
    print(f"期望结果: 4")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [[1,2],[2,3],[3,4],[4,5]]")
    points3 = [[1,2],[2,3],[3,4],[4,5]]
    solution3 = Solution()
    result3 = solution3.findMinArrowShots(points3)
    print(f"结果: {result3}")
    print(f"期望结果: 2")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: []")
    points4 = []
    solution4 = Solution()
    result4 = solution4.findMinArrowShots(points4)
    print(f"结果: {result4}")
    print(f"期望结果: 0")
