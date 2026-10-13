# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_start=ListNode()
        dummy_start.next=head
        ptr=head

        while ptr is not None and ptr.next is not None:
            next_node=ptr.next

            ptr.next=next_node.next
            next_node.next = dummy_start.next
            dummy_start.next = next_node


        return dummy_start.next


        