class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next 

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head_dummy = ListNode()
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head_dummy.next
        for _ in range(index):
            current = current.next

        return current.val   

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        
        if index > self.size:
            return

        current = self.head_dummy  
        for _ in range(index):
            current = current.next

        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        current = self.head_dummy    
        for _ in range(index):
            current = current.next

        node_to_delete = current.next
        current.next = node_to_delete.next
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)