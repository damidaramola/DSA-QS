# increment Decrement 

#pseudo code 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #get the count of all the numbers w hmap
        #if the count is the same, then it is an anagram or increment s then decremnt from t
        #if the count of values is !0 , return false 

        #order the values in alpha/lexi order and check if they are the same, otherwise false 

        hmap= {} #key - letter,value 

        for char in s:
            hmap[char] = hmap.get(char,0) + 1
        for char in t:
            hmap[char] = hmap.get(char,0) - 1

        for value in hmap.values():
            if value != 0:
                return False
        return True 
# s = "poll"
# t = "llop"
# s = "earth"
# t = "heart"
s = "market"
t = "target"
test = Solution()
run = test.isAnagram(s,t)
print(run)

# Time and space complexity 
# O(n) we are looping through the letters in the string which has a length of n
# O(n) we are using a hash map where it stores n entries (one for each unique character )

#least efficient solution 
