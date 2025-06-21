class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = defaultdict()
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self,node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1

        node = self.table[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            old_node = self.table[key]
            self.remove(old_node)
        node = ListNode(key,value)
        self.table[key] = node
        self.add(node)

        if len(self.table) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.table[lru.key]
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
