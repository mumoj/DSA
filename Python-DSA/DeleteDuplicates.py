# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr_node: ListNode = head
            set_list: list = []
            prev_node: Optional[ListNode] = None
            while(curr_node.next != None):
                if curr_node.val not in set_list:
                    set_list.append(curr_node.val)
                else:
                    if prev_node: prev_node.next = curr_node.next
                    curr_node = curr_node.next
                    continue

                prev_node = curr_node
                curr_node = curr_node.next

            if curr_node.val in set_list:
                prev_node.next = None

            return head

        else:
            return






        
        