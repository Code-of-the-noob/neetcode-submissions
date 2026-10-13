# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head=ListNode()
        ptr=dummy_head
        c=0
        while (l1 is not None) or (l2 is not None) or (c>0):
            a=0
            b=0

            if l1 is not None:
                a=l1.val 
                l1=l1.next
            if l2 is not None:
                b=l2.val
                l2=l2.next

            ptr.next=ListNode(val=(a+b+c)%10)
            c=(a+b+c)//10
            ptr=ptr.next

        return dummy_head.next



        