class Solution:

    def encode(self, strs: list[str]) -> str:
        #["neet","code","love","you"]
        #turn into a single string
        # bf - create an empty string
        #for every word, append each letter of that word to the string
        # return string
        # newstr = ""
        # for word in strs:
        #     for ch in word:
        #         newstr.append(ch)
        # print(newstr)
        
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
        

    def decode(self, s: str) -> list[str]:
        #take the previous string, then split it back up into original string
        # empty array
        res = []
        
        i = 0
        
        while i < len(s):
            j=i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
            
        return res

strs=["hold","on","nearly","there"]
s = '4#hold2#on6#nearly5#there'
# strs = ["go","in","the","hole"]
# s= '2#go2#in3#the4#hole'
test = Solution()
# run = test.encode(strs)
run = test.decode(s)
       
print(run)

#Time complexity O(n) looping through the strings in the list 
#Space complexity O(n)
