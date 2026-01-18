class Solution(object):
    def reversePrefix(self, word, ch):
        left = 0
        w=list(word)
        for right in range(len(w)):
            if w[right]==ch:
                while left<right:
                    w[right],w[left]=w[left],w[right]
                    left+=1
                    right-=1
                break
        res="".join(w)
        return res
        