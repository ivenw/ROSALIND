import math
from fastaImport import *

def common_substr(seq_0, seqs, start, length):
    for i in range(start, len(seq_0) - length + 1):
        substr = seq_0[i:i+length]
        for seq in seqs:
            if substr not in seq:
                break
        else:
            return (i, substr)
    return (-1, '')

def longest_common_substr(seqs):
    seq_0 = seqs.pop()
    low = 0
    high = len(seq_0) + 1
    start = 0
    longest_substr = ''

    while low + 1 < high:
        mid = math.floor((low + high) / 2)
        idx, substr = common_substr(seq_0, seqs, start, mid)
        if idx > -1:
            start = idx
            longest_substr = substr
            low = mid
        else:
            high = mid

    seqs.append(seq_0)

    return longest_substr

file = 'test_input.txt'

seqs = sorted( list( fastaImport(file).values() ), key=len )

print(longest_common_substr(seqs))
