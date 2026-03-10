#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
     
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        a = self.reverseList(l1)
        b = self.reverseList(l2)
        head = ListNode() 
        curr = head 
        carryOver = 0
        
        while a != None or b != None or carryOver:
            val = carryOver

            if a != None:
                val += a.val
                a = a.next
            
            if b != None:
                val += b.val
                b = b.next

            carryOver = val // 10
            val = val % 10
            
            curr.next = ListNode(val)
            curr = curr.next
            
        head = self.reverseList(head.next)
        return head
            
            
            


# @lc code=end

