# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res  = ListNode()
        root  = res 
        extra = 0
        
        while True:
            fst_value = l1.val if l1 else 0
            l1 = l1.next if l1 else None
            sec_value = l2.val if l2 else 0 
            l2 = l2.next if l2 else None
            
            value = fst_value+sec_value + extra 
            extra  = value // 10 
            value_to_append = value % 10 
            res.val = value_to_append
            
            if not l1 and not l2 :
                if extra :
                    res.next = ListNode(val = extra )
                    
                else :
                    res = None
                break 
            res.next = ListNode()
            res = res.next 
        return root
                
