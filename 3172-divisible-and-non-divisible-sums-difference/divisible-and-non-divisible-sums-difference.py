class Solution(object):
    def differenceOfSums(self, n, m):
        num1=[i for i in range(1,n+1) if i%m != 0]
        num2=[i for i in range(1,n+1) if i%m == 0]
        return (sum(num1)-sum(num2))
        