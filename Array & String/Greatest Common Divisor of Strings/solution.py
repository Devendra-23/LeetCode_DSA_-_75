class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Function to compute the GCD using the Euclidean algorithm
        def compute_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Compute GCD of lengths of str1 and str2
        gcd_length = compute_gcd(len(str1), len(str2))

        # Extract possible common divisor substring
        candidate = str1[:gcd_length]

        # Check if repeating the candidate forms both str1 and str2
        if str1 == candidate * (len(str1) // gcd_length) and str2 == candidate * (len(str2) // gcd_length):
            return candidate
        return ""
