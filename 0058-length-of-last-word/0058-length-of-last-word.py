class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        c=0
        for w in words[-1]:
            c+=1
        return c
            


        