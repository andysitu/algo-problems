class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    

class LRUCache:
    capacity = None
    # cache[key] = ListNode
    cache = None
    count = None

    oldest = None
    newest = None

    def delete_oldest_node(self):
        self.del_node( self.oldest.key )

    def create_node(self, key, val):
        n = ListNode(key, val)
        if self.oldest == None:
            self.oldest = n
            self.newest = n
        else:
            self.newest.next = n
            n.prev = self.newest

            self.newest = n
        self.cache[key] = n
        return n

    def del_node(self, key):
        node = self.cache[key]
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.prev: # but no next, so should be newest
            if self.newest == node:
                self.newest = node.prev
            node.prev.next = None
        elif node.next: # but no prev, so should be oldest
            if self.oldest == node:
                self.oldest = node.next
            node.next.prev = None
        else: # no prev nor next, so oldest and newest
            if self.oldest == node:
                self.oldest = None
                self.newest = None
        del self.cache[key]
        del node

    def touch_node(self, key, value=None):
        if value == None:
            value = self.cache[key].val
        self.del_node(key)
        self.create_node(key, value)
        return value        

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.touch_node(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.touch_node(key, value)
        else:
            if self.count + 1 > self.capacity:
                self.delete_oldest_node()
                
                self.create_node(key, value)
            else:
                self.create_node(key, value)
                self.count += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

["LRUCache", "put", "put", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [3, 3], [2], [4, 4], [1], [3], [4]]

["LRUCache","put","put","get","put","get","put","get","get","get", "put", "put", "put", "get", "put", "get", "put", "get", "put", "get", "get"]
[[4],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4],[10,10], [10,11], [4,3], [4], [45,13], [1], [44, 34], [2], [99, 98], [45], [10]]
"""