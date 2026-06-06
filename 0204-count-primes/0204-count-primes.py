class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        p = 2
        while p * p < n:
            if prime[p]:
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1

        return sum(prime)
        
        '''c = 0

        for num in range(2, n):
            flag = 0

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    flag = 1
                    break

            if flag == 0:
                c += 1

        return c'''