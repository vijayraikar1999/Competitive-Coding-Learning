# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans_list = None
        p = l1
        q = l2
        r = None
        hasil = 0
        while (p or q):
            sum_nums = hasil
            two_sum = 0
            if p is not None:
                sum_nums += p.val
                p = p.next
            if q is not None:
                sum_nums += q.val
                q = q.next
            if sum_nums >= 10:
                two_sum = sum_nums % 10
                hasil = 1
            else:
                two_sum = sum_nums
                hasil = 0

            new_node = ListNode(two_sum)
            if ans_list is None:
                ans_list = new_node
                r = new_node
            else:
                r.next = new_node
                r = r.next    


        if hasil == 1:
            r.next = ListNode(1)

        return ans_list           
                



            
        
