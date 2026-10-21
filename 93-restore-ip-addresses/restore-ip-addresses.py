class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res=[]
        if len(s)>12:
            return res
        
        def backtrack(i,dots,curip):
            #base case
            if dots==4 and i==len(s): # in recurssive call we are using j
                res.append(curip[:-1]) # as per problem statement we ned to get 4 dot point, that 4th dot point should be there in the last so last point is not to displayed to we are removing that
            if dots>4:
                return
            
            for j in range(i,min(i+3,len(s))):# if i use i+3 it may lead to out of index
              if  int(s[i:j+1])<256 and (i==j or s[i]!="0"):
                 backtrack(j+1,dots+1,curip+s[i:j+1]+".")
        backtrack(0,0,"")
        return res
                

            