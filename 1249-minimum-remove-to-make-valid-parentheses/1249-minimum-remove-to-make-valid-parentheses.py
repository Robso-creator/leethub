"""
 input   a,  , b, (, c, ), d, '', '',
    stck 8
  i  8

    


    

output  ab(c)d
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s) # O(n)
        stck = [] # O(n)

        for i, let in enumerate(s):
            if let == '(':
                stck.append(i)
            elif let == ')':
                if stck:
                    stck.pop()
                else:
                    s[i] = ''
        while stck:
            s[stck.pop()] = '' #stck.pop return the index saved on the stack, then replace it
        
        return ''.join(s)

#: n = amount of char in the string
#: T: O(n)
#: S: O(n)