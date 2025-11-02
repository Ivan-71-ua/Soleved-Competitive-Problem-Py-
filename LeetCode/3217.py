from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set_of_nums = set(nums)
        new_list = ListNode()
        head_of_list = new_list
        while head:
            if head.val not in set_of_nums:
                head_of_list.next = head
                head_of_list = head_of_list.next
            head = head.next
        head_of_list.next = None
        return new_list.next



