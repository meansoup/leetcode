# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = cur = ListNode()
        
        sum = 0
        head = head.next
        
        while head != None:
            if head.val == 0:
                cur.next = ListNode(sum)
                sum = 0
                cur = cur.next
            else:
                sum += head.val
            head = head.next
                
        return result.next