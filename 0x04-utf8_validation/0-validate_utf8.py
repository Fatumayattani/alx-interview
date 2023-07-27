#!/usr/bin/python3

def validUTF8(data):
    # Function to count the number of leading ones in a byte
    def countLeadingOnes(byte):
        count = 0
        mask = 1 << 7
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    # Check if the data represents a valid UTF-8 encoding
    i = 0
    while i < len(data):
        leading_ones = countLeadingOnes(data[i])
        
        # 1-byte character (0xxxxxxx)
        if leading_ones == 0:
            i += 1
        # Invalid character or incomplete encoding
        elif leading_ones == 1 or leading_ones > 4:
            return False
        # Multi-byte character (11xxxxxx, 110xxxxx, 1110xxxx, or 11110xxx)
        else:
            # Check if there are enough bytes following the leading byte
            if i + leading_ones > len(data) - 1:
                return False
            # Check if the following bytes are of the form 10xxxxxx
            for j in range(1, leading_ones):
                if not (data[i + j] & 0b11000000 == 0b10000000):
                    return False
            i += leading_ones

    return True

# Test cases
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # Output: True

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # Output: True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # Output: False
