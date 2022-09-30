class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                l.append(ch)
            elif len(l) == 0: return False
            elif ch == ')':
                if l.pop() != '(': return False
            elif ch == ']':
                if l.pop() != '[': return False
            elif ch == '}':
                if l.pop() != '{': return False
        
        if len(l) != 0: return False
        return True
