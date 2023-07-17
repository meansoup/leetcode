# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = self.to_num(l1) + self.to_num(l2)
        
        result = ListNode(val=int(str(num)[0]))
        current = result
        for c in str(num)[1:]:
            current.next = ListNode()
            current = current.next
            current.val = int(c)
        return result
    
    def to_num(self, listNode: Optional[ListNode]):
        current = listNode
        num = 0
        while True:
            num = num * 10 + current.val
            current = current.next
            if current == None:
                break
        return num