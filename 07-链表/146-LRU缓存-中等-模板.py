"""
146. LRU缓存
https://leetcode.cn/problems/lru-cache/description/

请你设计并实现一个满足 LRU (最近最少使用) 缓存约束的数据结构。
实现 LRUCache 类：
- LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
- int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1
- void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value；如果不存在，则向缓存中插入该组 key-value。如果插入操作导致关键字数量超过 capacity，则应该逐出最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

提示：
- 1 <= capacity <= 3000
- 0 <= key <= 10000
- 0 <= value <= 10^5
- 最多调用 2 * 10^5 次 get 和 put
"""


class LRUCache:
    """
    请在此处实现你的解法
    """
    
    def __init__(self, capacity: int):
        # TODO: 在此实现你的解法
        pass
    
    def get(self, key: int) -> int:
        # TODO: 在此实现你的解法
        pass
    
    def put(self, key: int, value: int) -> None:
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例
    lru = LRUCache(2)
    print("LRUCache(2)")
    
    lru.put(1, 1)
    print("put(1, 1)")
    
    lru.put(2, 2)
    print("put(2, 2)")
    
    print(f"get(1) = {lru.get(1)}")  # 返回 1
    
    lru.put(3, 3)
    print("put(3, 3)")  # 淘汰 key 2
    
    print(f"get(2) = {lru.get(2)}")  # 返回 -1
    
    lru.put(4, 4)
    print("put(4, 4)")  # 淘汰 key 1
    
    print(f"get(1) = {lru.get(1)}")  # 返回 -1
    print(f"get(3) = {lru.get(3)}")  # 返回 3
    print(f"get(4) = {lru.get(4)}")  # 返回 4
