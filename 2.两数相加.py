#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        def adder(l, l1, l2, op):
            if l1 == None and l2 == None:
                l.val = 1
                return
            l1_num = 0 if l1 == None else l1.val
            l2_num = 0 if l2 == None else l2.val
            l.val = l1_num + l2_num + op
            oper = 1 if l.val >= 10 else 0
            l.val -= oper * 10
            if l1 == None:
                if l2.next != None or oper:
                    l.next = ListNode()
                    adder(l.next, None, l2.next, oper)
            elif l2 == None:
                if l1.next != None or oper:
                    l.next = ListNode()
                    adder(l.next, l1.next, None, oper)
            else:
                if l1.next != None or l2.next != None or oper:
                    l.next = ListNode()
                    adder(l.next, l1.next, l2.next, oper)
                    
        adder(l, l1, l2, 0)
        return l
# @lc code=end

