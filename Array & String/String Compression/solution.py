class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0  # Index to write compressed characters
        read = 0   # Index to read characters
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count occurrences of the same character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # If count > 1, write the digits of the count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
