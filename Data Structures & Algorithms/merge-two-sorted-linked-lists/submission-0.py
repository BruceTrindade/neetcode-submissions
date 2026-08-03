# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#                |                |
#.  list1 = [1,2,4], list2 = [1,3,4]
#   merged = [1,1,2,3,44]
# 
#  while curr1 != None AND curr2 != None
#   if curr1 <= curr2
#  merged_list.next = curr1
#   merged_list.next.next = curr2
#   elif curr1 > curr2
#   merged_list.next = curr2
#   merged_list.next.next = curr1
# 
#

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        current1 = list1
        current2 = list2   
        head = ListNode()  
        tail = head  

        while current1 and current2:

            if current1.val <= current2.val:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next

            tail = tail.next    

        tail.next = current1 if current1 else current2

        return head.next        