#!/usr/bin/env python
import sys

def search2(a,m):
    low = 0
    high = len(a) - 1
    while(low <= high):
        mid = (low + high)/2
        midval = a[mid]

        if midval < m:
            low = mid + 1
        elif midval > m:
            high = mid - 1
        else:
            print mid
            return mid
    print -1
    return -1

# if __name__ == "__main__":
#     a = [int(i) for i in list(sys.argv[1])]
#     print(a)
#     m = int(sys.argv[2])
#     search2(a,m)

search2([1,2,3,4],3)
