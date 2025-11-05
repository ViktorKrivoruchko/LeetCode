class Solution:
    def isValid(self, s: str) -> bool:
        rounder = ["(", ")"]
        square = ["[", "]"]
        curly = ["{", "}"]
        stack1, stack2, stack3 = 0, 0, 0
        
        for i in s:
            if i in rounder:
                stack1 += 1
            elif i in square:
                stack2 += 1
            elif i in curly:
                stack3 += 1
        
        if (stack1 + stack2 + stack3) % 2 == 0 and (stack1 % 2) != 1 and (stack2 % 2) != 1:
            return True
        else:
            return False