# 763. 划分字母区间
# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
# 返回一个表示每个字符串片段的长度的列表。
#
# 示例 1：
# 输入：s = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
#
# 示例 2：
# 输入：s = "eccbbbbxxc"
# 输出：[10]

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 记录每个字符最后出现的位置
        last_pos = {}
        for i, ch in enumerate(s):
            last_pos[ch] = i
        
        result = []
        start = 0
        end = 0
        
        for i, ch in enumerate(s):
            end = max(end, last_pos[ch])
            
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    print(f"测试1结果: {solution.partitionLabels('ababcbacadefegdehijhklij')}")  # 期望输出: [9, 7, 8]
    
    # 测试2
    print(f"测试2结果: {solution.partitionLabels('eccbbbbxxc')}")  # 期望输出: [10]
