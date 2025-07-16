class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
    
        a,b=0,0
  
        s=[]
        while a < len(word1) and b < len(word2):
            s.append(word1[a])
            a+=1
            s.append(word2[b])
            b+=1
        s.append(word1[a:])
        s.append(word2[b:])
        return "".join(s)

        
     
        
            

            

        
        
            

        
        