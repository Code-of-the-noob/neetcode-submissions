# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node=ListNode()
        ptr=dummy_node

        while list1 is not None or list2 is not None:
            if list1 is None or (list2 is not None and list2.val<list1.val):
                ptr.next=list2
                list2=list2.next

            else:
                ptr.next=list1
                list1=list1.next
                

            ptr=ptr.next

        return dummy_node.next