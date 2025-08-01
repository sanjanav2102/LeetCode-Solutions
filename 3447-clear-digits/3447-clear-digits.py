class Solution(object):
    def clearDigits(self, s):
        stack=[]
        ans = ' '
        for i in s:
            if i.isdigit():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
     
        