"""
739. 每日温度
https://leetcode.cn/problems/daily-temperatures/description/

给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，使得 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]

提示：
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        计算每天需要等几天才会有更高的温度
        
        参数:
            temperatures: 每天温度数组
            
        返回:
            等待天数数组
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: temperatures = [73,74,75,71,69,72,76,73]")
    temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
    result1 = solution.dailyTemperatures(temperatures1)
    print(f"结果: {result1}")
    print(f"期望结果: [1, 1, 4, 2, 1, 1, 0, 0]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: temperatures = [30,40,50,60]")
    temperatures2 = [30, 40, 50, 60]
    result2 = solution.dailyTemperatures(temperatures2)
    print(f"结果: {result2}")
    print(f"期望结果: [1, 1, 1, 0]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: temperatures = [30,60,90]")
    temperatures3 = [30, 60, 90]
    result3 = solution.dailyTemperatures(temperatures3)
    print(f"结果: {result3}")
    print(f"期望结果: [1, 1, 0]")
