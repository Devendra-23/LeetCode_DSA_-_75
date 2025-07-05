class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0  # i for s, j for t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # move forward in s (match found)
            j += 1      # always move forward in t

        return i == len(s)  # all characters of s matched in t