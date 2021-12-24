
# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.defaultdict(int)
        start = 0 
        end = 0
        maxlen = 0
       
   
        while(end<len(s)):
            if s[end] not in d:
                d[s[end]] +=1
                maxlen = max(maxlen, end-start+1)
                end+=1
            else:
                del d[s[start]]
                start +=1
                
        return maxlen
        
        