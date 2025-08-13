class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10==0 and x!=0):
            return False
        rev_l=0
        while x > rev_l:
            rev_l=rev_l*10+x%10
            x=x//10
        return x==rev_l or x == rev_l//10
    
        
            

            



class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        rev_list=0
        while x > rev_list:
            rev_list=rev_list*10+x%10
            x//=10
        return x==rev_list or x==rev_list//10

           
       


      
        
      
        
        
       
        
        