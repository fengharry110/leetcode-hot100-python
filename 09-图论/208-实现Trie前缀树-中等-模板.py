"""
208. 实现 Trie (前缀树)
https://leetcode.cn/problems/implement-trie-prefix-tree/description/

Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：
Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

示例：
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True

提示：
1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 10^4 次
"""


class TrieNode:
    def __init__(self):
        self.children = {}  # 子节点
        self.is_end = False  # 是否是单词结尾


class Trie:
    """
    请在此处实现你的解法
    """
    
    def __init__(self):
        # TODO: 在此实现初始化
        pass

    def insert(self, word: str) -> None:
        """
        向前缀树中插入字符串
        
        参数:
            word: 要插入的字符串
        """
        # TODO: 在此实现你的解法
        pass

    def search(self, word: str) -> bool:
        """
        搜索字符串是否在前缀树中
        
        参数:
            word: 要搜索的字符串
            
        返回:
            字符串是否存在
        """
        # TODO: 在此实现你的解法
        pass

    def startsWith(self, prefix: str) -> bool:
        """
        检查前缀是否存在
        
        参数:
            prefix: 要检查的前缀
            
        返回:
            前缀是否存在
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    trie = Trie()
    print("Trie()")
    
    trie.insert("apple")
    print('insert("apple")')
    
    print(f'search("apple") = {trie.search("apple")}')    # True
    print(f'search("app") = {trie.search("app")}')        # False
    print(f'startsWith("app") = {trie.startsWith("app")}')  # True
    
    trie.insert("app")
    print('insert("app")')
    
    print(f'search("app") = {trie.search("app")}')        # True
