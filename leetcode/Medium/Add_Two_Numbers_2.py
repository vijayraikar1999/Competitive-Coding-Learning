# Problem link - https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        str1 = ''
        str2 = ''
        p = l1
        q = l2
        while p != None:
            str1 += str(p.val)
            p = p.next
            
        while q != None:
            str2 += str(q.val)
            q = q.next
            
        ans = str(int(str1) + int(str2))
        
        ansList = [int(ele) for ele in ans]
        
        
        p = ListNode(ansList[0])
        if len(ansList) == 1:
            return p
        q = p
        
        for ele in ansList[1:]:
            q.next = ListNode(ele)
            q = q.next
            
        return p  