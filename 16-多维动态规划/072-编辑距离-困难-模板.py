"""
72. 编辑距离
https://leetcode.cn/problems/edit-distance/description/

给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：
- 插入一个字符
- 删除一个字符
- 替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

提示：
0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成
"""


class Solution:
    """
    请在此处实现你的解法
    """
    
    def minDistance(self, word1: str, word2: str) -> int:
        """
        计算将word1转换为word2的最少操作数
        
        参数:
            word1: 第一个单词
            word2: 第二个单词
            
        返回:
            最少操作数
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: word1 = 'horse', word2 = 'ros'")
    word1_1 = "horse"
    word2_1 = "ros"
    result1 = solution.minDistance(word1_1, word2_1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: word1 = 'intention', word2 = 'execution'")
    word1_2 = "intention"
    word2_2 = "execution"
    result2 = solution.minDistance(word1_2, word2_2)
    print(f"结果: {result2}")
    print(f"期望结果: 5")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: word1 = '', word2 = 'a'")
    word1_3 = ""
    word2_3 = "a"
    result3 = solution.minDistance(word1_3, word2_3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
