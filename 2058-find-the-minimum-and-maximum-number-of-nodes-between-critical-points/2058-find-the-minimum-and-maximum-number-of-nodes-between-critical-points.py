# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        idx = 0
        
        first_idx = None
        ex_idx = None
        
        minn = 99999999
        
        eex, ex = None, None
        while head != None:
            cur = head.val
            if eex != None and ex != None:
                if (ex < eex and ex < cur) or (ex > eex and ex > cur):
                    if first_idx == None:
                        first_idx = idx
                    if ex_idx != None:
                        minn = min(minn, idx - ex_idx)
                    ex_idx = idx
            idx += 1
            head = head.next
            eex = ex
            ex = cur
            
            
        minn = -1 if minn == 99999999 else minn
        maxx = -1 if first_idx == None or ex_idx == first_idx else ex_idx - first_idx
        
        return [minn, maxx]
                    
                    
        