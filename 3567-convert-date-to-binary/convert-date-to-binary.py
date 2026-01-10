class Solution(object):
    def convertDateToBinary(self, date):
        bDate = ""
        for i in date.split('-'):
            bDate+=bin(int(i))[2:]+'-'
        return bDate[:-1]
        