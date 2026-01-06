class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        s1=set(ransomNote)
        s2=set(magazine)
        rd={}
        md={}
        for i in s1:
            rd[i]=ransomNote.count(i)
        for i in s2:
            md[i]=magazine.count(i)
        k=rd.keys()
        for i in k:
            if i not in md or rd[i]>md[i]:
                return False
        return True
        