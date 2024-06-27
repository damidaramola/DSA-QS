#isalnum(),while loops

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # my solution 
        # 1. process string - remove none alphanums,spaces,uppercase
        # 2. check if it is a palindrome or not - true,false 
        # check if string isempty = rturn true
        # s.lower(), s.strip , s.isalphanum
        # two pointers, i at start, j at s-1
       
       #actual solution - using while loop ,check if string is non-alpha numeric,then compare,increment decrement

       i = 0
       j = len(s) - 1 

       while i < j:
        if not s[i].isalnum():
            i +=1
        elif not s[j].isalnum():
            j -=1
        elif s[i].lower() == s[j].lower():
            i +=1
            j -=1
        else:
            return False
       return True
   
s = "Programming is fun"
s = "Madam, in Eden, I'm Adam."
s= " "

test = Solution()
run = test.isPalindrome(s)
print(run)