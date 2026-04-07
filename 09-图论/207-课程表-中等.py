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
"""

from typing import List
from collections import deque


class Solution:
    """
    课程表解法类
    
    解题思路：
        拓扑排序，使用广度优先搜索
        
    算法步骤：
        1. 构建邻接表和入度数组
        2. 将入度为0的节点加入队列
        3. 广度优先搜索，每次取出一个节点，减少其邻接节点的入度
        4. 如果入度为0，加入队列
        5. 最后检查是否所有节点都被访问
        
    时间复杂度：O(V + E)
    空间复杂度：O(V + E)
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
        # 构建邻接表和入度数组
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
        
        # 将入度为0的节点加入队列
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # 广度优先搜索
        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 检查是否所有节点都被访问
        return count == numCourses


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
    solution2 = Solution()
    result2 = solution2.canFinish(numCourses2, prerequisites2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]")
    numCourses3 = 4
    prerequisites3 = [[1,0],[2,0],[3,1],[3,2]]
    solution3 = Solution()
    result3 = solution3.canFinish(numCourses3, prerequisites3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: numCourses = 1, prerequisites = []")
    numCourses4 = 1
    prerequisites4 = []
    solution4 = Solution()
    result4 = solution4.canFinish(numCourses4, prerequisites4)
    print(f"结果: {result4}")
    print(f"期望结果: True")
