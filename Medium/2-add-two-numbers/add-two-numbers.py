# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_num(node):
            num = 0
            place = 1
            while node:
                num += node.val * place
                place *= 10
                node = node.next
            return num

        def num_to_list(n):
            dummy = ListNode(0)
            current = dummy
            if n == 0:
                return ListNode(0)
            while n > 0:
                current.next = ListNode(n % 10)
                n //= 10
                current = current.next
            return dummy.next

        n1 = list_to_num(l1)
        n2 = list_to_num(l2)
        total = n1 + n2
        return num_to_list(total)