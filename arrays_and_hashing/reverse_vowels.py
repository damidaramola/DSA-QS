class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        a
        iea
        ^ ^
        "AceCreim"
        ^      ^
        store vowel in a lookup - set?
        use 2 pointers, if it is a vowel
        swap the vowels and decrement?
        """
        vowels = {'A','a','e','E','I','i','O','o','U','u'}
        s = list(s) # takes O(n) time
        r = len(s) -1
        l = 0
        
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
            elif s[l] not in vowels:
                l +=1
            elif s[r] not in vowels:
                r-=1
        return "".join(s) # takes O(n) time
    
#Time complexity O(n) - iterating through the list with 2 pointers 
# Space complexity O(n)