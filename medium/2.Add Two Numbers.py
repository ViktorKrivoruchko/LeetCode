from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

# нативное решение. Проблема: много лишних преобразований и два отдельных цикла для l1 и l2
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = []
        l4 = []
        current = l1
        result = []
        while current:
            l3.append(current.val)
            current = current.next
        current = l2
        while current:
            l4.append(current.val)
            current = current.next
        sum_nums = list(str(int(''.join(map(str, l3[::-1]))) + int(''.join(map(str, l4[::-1])))))[::-1]
        head = ListNode(int(sum_nums[0]))
        current = head
        for digit in sum_nums[1:]:
            current.next = ListNode(int(digit))
            current = current.next
        return head
    
# улучшенное решение с одним циклом и вынесением подсчета результата за цикл
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        l4 = l3
        num = 0
        while l1 or l2 or num:
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            
            l4.next = ListNode(num % 10)
            l4 = l4.next
            num //= 10

        return l3.next
            