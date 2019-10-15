import collections


class LRUCache1:
    def __init__(self, capacity: int):
        self.dic, self.cap = collections.OrderedDict(), capacity

    def get(self, key: int) -> int:
        if key not in self.dic: return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic: del self.dic[key]
        elif len(self.dic) == self.cap: self.dic.popitem(0)
        self.dic[key] = value


class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = list()
        self.cache = dict()

    def get(self, key):
        if key in self.cache:
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache[key]

        return -1

    def put(self, key, value):
        if key in self.cache:
            self.stack.remove(key)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.stack[0]]
                self.stack.pop(0)

        self.stack.append(key)
        self.cache[key] = value


# 创建双向链表
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.lookup = dict()
        self.max_len = capacity

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.remove(self.lookup[key])
        if len(self.lookup) == self.max_len:
            self.remove(self.head.next)
        self.add(Node(key, value))
    def remove(self, node):
        del self.lookup[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
    def add(self, node):
        self.lookup[node.key] = node
        pre_tail = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        pre_tail.next = node
        node.prev = pre_tail

