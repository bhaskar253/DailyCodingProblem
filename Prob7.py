# Problem Stmt.:
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

def count_ways(encoded_msg,mapping):
    if len(encoded_msg)==1:
        return 1 if encoded_msg in mapping else 0
    elif len(encoded_msg)==2:
        if(encoded_msg.startswith('0')):
            return 0
        if encoded_msg in mapping:
            return 2
        if not encoded_msg.endswith('0'):
            return 1
        return 0
    else:
        x = 1 if encoded_msg[:1] in mapping else 0
        y = 1 if encoded_msg[:2] in mapping else 0
        return x*count_ways(encoded_msg[1:],mapping) + y*count_ways(encoded_msg[2:],mapping)


if __name__ == "__main__":
    mapping = {}
    for i in range(0,26):
        mapping[str(i+1)] = chr(ord('a')+i)
    print(count_ways('111',mapping))
    print(count_ways('001',mapping))
