# 621. 任务调度器
# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
# 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
# 你需要计算完成所有任务所需要的 最短时间 。


class Solution:
    def leastInterval(self, tasks, n):
        """
        计算完成所有任务所需要的最短时间
        方法：贪心算法
        时间复杂度：O(n)，其中n是任务的数量
        空间复杂度：O(1)，因为任务种类最多为26种
        """
        from collections import Counter
        
        # 统计每个任务的出现次数
        task_counts = Counter(tasks)
        # 找到出现次数最多的任务及其出现次数
        max_count = max(task_counts.values())
        # 统计有多少个任务的出现次数等于最大次数
        max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)
        
        # 计算所需的最少时间
        # 公式：(max_count - 1) * (n + 1) + max_count_tasks
        # 但如果任务总数大于这个值，则取任务总数
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    tasks1 = ["A","A","A","B","B","B"]
    n1 = 2
    print("测试用例1:")
    print("输入: tasks =", tasks1, "n =", n1)
    print("输出:", solution.leastInterval(tasks1, n1))
    print()
    
    # 测试用例2
    tasks2 = ["A","A","A","B","B","B"]
    n2 = 0
    print("测试用例2:")
    print("输入: tasks =", tasks2, "n =", n2)
    print("输出:", solution.leastInterval(tasks2, n2))
    print()
    
    # 测试用例3
    tasks3 = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n3 = 2
    print("测试用例3:")
    print("输入: tasks =", tasks3, "n =", n3)
    print("输出:", solution.leastInterval(tasks3, n3))
    print()
    
    # 测试用例4
    tasks4 = ["A","B","C","D","E","A","B","C","D","E"]
    n4 = 4
    print("测试用例4:")
    print("输入: tasks =", tasks4, "n =", n4)
    print("输出:", solution.leastInterval(tasks4, n4))