class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        d={}
        cle=""
        for i in paragraph:
            if i.isalpha():
                cle+= i.lower()
            else:
                cle+=" "
        for i in cle.split():
            if i not in banned:
                if i not in d:
                    d[i]=1
                else:
                    d[i.lower()]+=1
        m=max(d.values())
        for i in d.keys():
            if d[i]==m:
                return i
        