# python3
multiplier1 = 2
multiplier2 = 56
prime1 = 1000000007
prime2 = 1000000009



def getHash(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier1 + ord(c)) % prime1
    return ans

# def getHash2(s):
#     ans = 0
#     for c in reversed(s):
#         ans = (ans * multiplier2 + ord(c)) % prime2
#     return ans


def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # return [
    #     i
    #     for i in range(len(text) - len(pattern) + 1)
    #     if text[i:i + len(pattern)] == pattern
    # ]
    patternHash=getHash(pattern)
    PL=len(pattern)
    TL=len(text)
    res=[]
    maxPower=multiplier1**(PL-1)
    Hash=getHash(text[TL-PL:TL])
    if text[TL-PL:TL] == pattern:
        res.append(TL-PL)
    for i in range(TL-1 ,max(PL-1,0),-1):
        Hash=((Hash-ord(text[i])*maxPower)*multiplier1+ord(text[i-PL]))
        #print("Hash=",Hash)
        if patternHash==Hash:
            if text[i-PL:i]==pattern:
                res.append(i-PL)
    return list(reversed(res))





if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
