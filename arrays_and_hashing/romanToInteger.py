class Solution:
    def romanToInt(self, s: str) -> int:
        """
        4, 9 
        I V - 5-1
        IX - 10 -1 

        if it is a 4 we add I - V

        we are given III convert
        I = 1 , increment the count by the value in the string
        return the count 

        LVIII
        50,5,1,1,1 -> 55

        MCMXCIV
        1000, (CM) 900, (XC) 90,(4) IV
        how do i check if the number ahead is going to make it 900, 90, 9 , 400, 40, 4?
        if the number before 5,50, or 500 is I , X or C , subtract I, X or C from that number 
        if the number before 10,100, or 1000 is I , X or C , subtract I, X or C from that number
        
        hint -> if the number is smaller than the number ahead of it, decrement by that number
        adjust for out of bound errors
        """

        rom_int = {'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }
        
        count = 0
        for i in range(len(s) -1):

            if rom_int[s[i]] < rom_int[s[i+ 1]]:
                count -= rom_int[s[i]]
            else:
                count += rom_int[s[i]]
        return count + rom_int[s[-1]]
    
# Time and  complexity - > O(n)
# space complexity -> O(1) , constant fixed hmap makes it O(1)
            