"""
207. 课程表
https://leetcode.cn/problems/course-schedule/description/

你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。

请你判断是否可能完成所有课程的学习？

示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

示例 2：
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

提示：
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
prerequisites[i] 中的所有课程对 互不相同
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        判断是否可以完成所有课程
        
        参数:
            numCourses: 课程数量
            prerequisites: 先修课程关系
            
        返回:
            是否可以完成所有课程
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: numCourses = 2, prerequisites = [[1,0]]")
    numCourses1 = 2
    prerequisites1 = [[1,0]]
    solution = Solution()
    result1 = solution.canFinish(numCourses1, prerequisites1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: numCourses = 2, prerequisites = [[1,0],[0,1]]")
    numCourses2 = 2
    prerequisites2 = [[1,0],[0,1]]
    result2 = solution.canFinish(numCourses2, prerequisites2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]")
    numCourses3 = 4
    prerequisites3 = [[1,0],[2,0],[3,1],[3,2]]
    result3 = solution.canFinish(numCourses3, prerequisites3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: numCourses = 1, prerequisites = []")
    numCourses4 = 1
    prerequisites4 = []
    result4 = solution.canFinish(numCourses4, prerequisites4)
    print(f"结果: {result4}")
    print(f"期望结果: True")
