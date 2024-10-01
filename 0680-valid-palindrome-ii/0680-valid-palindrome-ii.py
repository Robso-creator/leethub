"""
two pointer
left right

if the letter != count +=1
if count = 2 then false
else true



[abc]

counter 1
left 0 a
right 2 c
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrom(s, left, right, deleted):
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    else:
                        return is_palindrom(s,left+1, right, True) or is_palindrom(s, left, right-1, True) #need this because i can delete either left or right and have a valid palindrome
                else:
                    left += 1
                    right -= 1
            return True #return of is_palindrom

        return is_palindrom(s, 0, len(s) -1,  False) # return of the main function

#:T: O(n)
#:S: O(n)