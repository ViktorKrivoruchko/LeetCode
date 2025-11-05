class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        l4 = l3
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            l4.next = ListNode(carry % 10)
            l4 = l4.next
            carry //= 10
        return l3.next
    
class SomeClass:
    def SomeFunction(self, l1: list, l2: list) -> list:
        # newList = int(reversed(l1)) + int(reversed(l2))
        newList = []
        i = 0
        while i <= len(l1) or i <= len(l2):
            newList.append(l1[i] + l2[i])
        return reversed(newList)

SomeClass.SomeFunction([2, 4, 3], [5, 6, 4], [7, 0, 8])