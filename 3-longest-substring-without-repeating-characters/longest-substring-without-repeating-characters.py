class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0 
        localSum = 0 
        space_count = 0 
        encountered = [] 

        for i in range(len(s)): 
            if s[i] == " " and space_count == 0: 
                localSum += 1
                space_count += 1  
            elif s[i] == " " and space_count > 0:
                if localSum > longestSubstring:
                    longestSubstring = localSum 
    
                localSum = 0   
                space_count = 0 

            elif s[i] not in encountered: 
                localSum += 1 
                encountered.append(s[i]) 

            elif s[i] in encountered: 
                encountered = encountered[encountered.index(s[i])+1:] 
                encountered.append(s[i])
                if localSum > longestSubstring:
                    longestSubstring = localSum 
          
                localSum = len(encountered)  
           
        if localSum > longestSubstring:
            return localSum
        else:
            return longestSubstring
        