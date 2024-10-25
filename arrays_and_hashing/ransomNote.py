class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        get the count of each word in magazine and put it in a dictionary
        if its not in the dictionary, set the value to one 
        otherwise increment 

        for each letter n the note if its not in the mag dictionary, return false 
        if we have not iterated through all the letters in the dict and the value of the char is 0, then 
        mag doesnt have enough of that char, return false 
        if we do find the char, decrement it because now we have used it 
        if we have looped through the whole string and all is good , return true
        """

        mag_dict = {}

        for char in magazine:
            if not mag_dict.get(char):
                mag_dict[char] = 1
            else:
                mag_dict[char] += 1 
        
        for letter in ransomNote:
            if letter not in mag_dict:
                return False 
            elif mag_dict[letter] == 0:
                return False
            else:
                 mag_dict[letter] -= 1
        return True 

#Time complexity - O(n+m)
#space complexity - O(m)