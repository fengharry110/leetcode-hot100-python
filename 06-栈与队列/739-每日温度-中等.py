"""
739. 每日温度
https://leetcode.cn/problems/daily-temperatures/description/

给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1：
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2：
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3：
输入: temperatures = [30,60,90]
输出: [1,1,0]
"""

from typing import List


class Solution:
    """
    每日温度解法类
    
    解题思路：
        使用单调栈，栈中存储温度的索引，保持栈中温度递减
        
    算法步骤：
        1. 初始化结果数组为0
        2. 初始化单调栈
        3. 遍历温度数组：
           - 当栈不为空且当前温度大于栈顶温度时：
               - 弹出栈顶元素
               - 计算天数差并更新结果数组
           - 将当前索引入栈
        4. 返回结果数组
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        计算每日温度
        
        参数:
            temperatures: 温度数组
            
        返回:
            结果数组
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # 存储索引
        
        for i in range(n):
            # 当栈不为空且当前温度大于栈顶温度
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # 弹出栈顶元素
                prev_index = stack.pop()
                # 计算天数差
                answer[prev_index] = i - prev_index
            # 将当前索引入栈
            stack.append(i)
        
        return answer


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [73,74,75,71,69,72,76,73]")
    temperatures1 = [73,74,75,71,69,72,76,73]
    solution = Solution()
    result1 = solution.dailyTemperatures(temperatures1)
    print(f"结果: {result1}")
    print(f"期望结果: [1,1,4,2,1,1,0,0]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [30,40,50,60]")
    temperatures2 = [30,40,50,60]
    solution2 = Solution()
    result2 = solution2.dailyTemperatures(temperatures2)
    print(f"结果: {result2}")
    print(f"期望结果: [1,1,1,0]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [30,60,90]")
    temperatures3 = [30,60,90]
    solution3 = Solution()
    result3 = solution3.dailyTemperatures(temperatures3)
    print(f"结果: {result3}")
    print(f"期望结果: [1,1,0]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [55,38,53,81,61,93,97,32,43,78]")
    temperatures4 = [55,38,53,81,61,93,97,32,43,78]
    solution4 = Solution()
    result4 = solution4.dailyTemperatures(temperatures4)
    print(f"结果: {result4}")
    print(f"期望结果: [3,1,1,2,1,1,0,1,1,0]")
