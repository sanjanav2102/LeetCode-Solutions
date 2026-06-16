class Solution(object):
    def addBinary(self, a, b):
        A = int(a,2)
        B = int(b,2)
        while B:
            carry = (A & B) << 1
            A = A ^ B
            B = carry
        return bin(A)[2:]