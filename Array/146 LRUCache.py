'''
思路一：每次把新加入的键值放到数组的最左边；每次把访问的数据抽出来放在最左边
需要找到被访问的数据的位置index，这个过程T(n) = n,比较耗时
'''
class LRUCache:
    def __init__(self, capacity):
        self.dic = {}
        self.capacity = capacity
        self.cnt = 0
        self.freq = {}

    def get(self, key):
        if key in self.dic:
            self.freq[key] += 1
            return self.dic[key]
        else:
            return -1

    def put(self, key, value):
        if self.cnt == self.capacity:
            temp = sorted(self.freq.items(),key = lambda x:x[1])
            del self.dic[temp[0][0]]
            del self.freq[temp[0][0]]
            self.cnt -= 1

        self.dic[key] = value
        self.freq[key] = 1
        self.cnt += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1,1)
    cache.put(2,2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

