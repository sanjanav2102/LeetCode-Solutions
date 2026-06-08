class Solution(object):
    def countOdds(self, low, high):
        ninbtw = high-low+1
        if (ninbtw%2 !=0 and low%2 !=0 and high%2 != 0):
            return (ninbtw//2)+1
        else:
            return ninbtw//2



        