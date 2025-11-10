
class Solution(object):
    def getNext(self,n):
        sum = 0
        while n>0:
            digit = n%10
            sum+=digit*digit
            n = n//10
        return sum
    def isHappy(self, n):
        slow = n
        fast = self.getNext(n)      
        while (fast != 1 and slow != fast):
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))
        return fast == 1
    
        '''
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            newn = 0
            while n != 0:
                d = n%10
                newn += d ** 2
                n //= 10
            n = newn
        if n == 1:
            return True
        return False'''
    