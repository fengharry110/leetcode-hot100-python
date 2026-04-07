"""
134. 加油站
https://leetcode.cn/problems/gas-station/description/

在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。

示例 1:
输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。

示例 2:
输入: gas = [2,3,4], cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
开往 2 号加油站，你需要消耗 4 升汽油，这时候油箱里只有 3 升汽油，无法到达 2 号加油站。
因此，无论怎样，你都不可能绕环路行驶一周。
"""

from typing import List


class Solution:
    """
    加油站解法类
    
    解题思路：
        使用贪心算法，遍历加油站，计算总油量和总消耗
        
    算法步骤：
        1. 计算总油量和总消耗
        2. 如果总油量小于总消耗，返回-1
        3. 遍历加油站，计算当前油量
        4. 如果当前油量小于0，重置起始位置和当前油量
        5. 返回起始位置
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        计算能否环绕一周并返回起始加油站
        
        参数:
            gas: 加油站的油量数组
            cost: 行驶消耗的油量数组
            
        返回:
            起始加油站的编号，无法环绕返回-1
        """
        n = len(gas)
        total_gas = 0
        total_cost = 0
        current_gas = 0
        start = 0
        
        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
            
            # 如果当前油量小于0，说明从当前起始位置无法到达
            if current_gas < 0:
                # 重置起始位置为下一个加油站
                start = i + 1
                current_gas = 0
        
        # 如果总油量小于总消耗，无法环绕
        if total_gas < total_cost:
            return -1
        
        return start


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: gas = [1,2,3,4,5], cost = [3,4,5,1,2]")
    gas1 = [1,2,3,4,5]
    cost1 = [3,4,5,1,2]
    solution = Solution()
    result1 = solution.canCompleteCircuit(gas1, cost1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: gas = [2,3,4], cost = [3,4,3]")
    gas2 = [2,3,4]
    cost2 = [3,4,3]
    solution2 = Solution()
    result2 = solution2.canCompleteCircuit(gas2, cost2)
    print(f"结果: {result2}")
    print(f"期望结果: -1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: gas = [5,1,2,3,4], cost = [4,4,1,5,1]")
    gas3 = [5,1,2,3,4]
    cost3 = [4,4,1,5,1]
    solution3 = Solution()
    result3 = solution3.canCompleteCircuit(gas3, cost3)
    print(f"结果: {result3}")
    print(f"期望结果: 4")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: gas = [3,1,1], cost = [1,2,2]")
    gas4 = [3,1,1]
    cost4 = [1,2,2]
    solution4 = Solution()
    result4 = solution4.canCompleteCircuit(gas4, cost4)
    print(f"结果: {result4}")
    print(f"期望结果: 0")
