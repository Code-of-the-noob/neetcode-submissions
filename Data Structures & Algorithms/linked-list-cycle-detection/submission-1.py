# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_ptr=head
        slow_ptr=head

        while fast_ptr is not None and fast_ptr.next is not None:
            
            fast_ptr=fast_ptr.next
            if fast_ptr:
                fast_ptr=fast_ptr.next
            if fast_ptr == slow_ptr:
                return True

            slow_ptr=slow_ptr.next

            
            

                

        return False