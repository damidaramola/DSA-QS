#Default Dict
#tuples are immuatble and can be used for keys in dictionaries

 # brute force - O(n^2) check words side by side for anagram match 
# emty array/ append []
# append [strs[num]] to empty array 

# make the first letter of the word the key and the values the letters that alphabetucally similar to both nums

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dicts = defaultdict(list)
        arr = []
   
        for word in strs:
            sorted_str = tuple(sorted(word))
            dicts[sorted_str].append(word)

        for value in dicts.values():
            arr.append(value)
        return arr
    

#strs= ["art","rat","flow","wolf","cat","tac","bone"]
strs = [ "loop", "pool","nap", "pan"]

test = Solution()
run = test.groupAnagrams(strs)

print(run)

    # Time complexity - O(n * K log K) - K, sorting string of length k
    #Space complexity - O(n.k ) 
    #  Iterating over the dictionary's values and constructing the result list involves iterating over all the strings once more
    # which takes O(n.k) time where k is the avg length of the string 
    
    # Or TC - O(n), SC - O(n)