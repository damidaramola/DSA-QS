class Solution:
    def decodeString(self, s: str) -> str:
        """
        we need to check if char is a digit, bracket or letter
        """
        stack = []
        curNum = 0 
        curString = ''

        for ch in s:
            if ch == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0

            elif ch == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif ch.isdigit():
                curNum = curNum*10 + int(ch)

            else:
                curString += ch
        return curString
    
#TC and SC -> O(n)