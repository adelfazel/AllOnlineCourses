# Uses python3
import sys

# + + + m + + +
# - c - - - - -
#

def binary_search(a, x):
    left, right = 0, len(a)
    newMid=-1
    mid= (left+right)//2
    while newMid!=mid:
        mid= (left+right)//2
        if (a[mid])==x:return mid
        if x<a[mid]:
            right=mid
        else:
            left=mid
        newMid=   (left+right)//2
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
