#Uses python3

import sys



def intilizeDistMatrix(dimx,dimy):
    distance_matrix = [[0 for _ in range(dimx)] for _ in range(dimy)]
    return distance_matrix

def lcs2(s, t):
    #write your code here
    dimx=len(t)
    dimy=len(s)
    distance_matrix=intilizeDistMatrix(dimx+1,dimy+1)
    candidates=[0]*3
    route=[]
    for i in range(1,dimy+1):
        for j in range(1,dimx+1):
            candidates[0]=distance_matrix[i-1][j]
            candidates[1]=distance_matrix[i][j-1]
            if (s[i-1]==t[j-1]):
                candidates[2]=distance_matrix[i-1][j-1]+1
            else:
                candidates[2]=-1
                # candidates[2]=0
            distance_matrix[i][j]=max(candidates)
    return distance_matrix[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data=[1,1,1,10]

    #data=[4,2,7,8,3,4,5,2,8,7]
    # data=[3,2,7,5,2,2,5]
    # data=[6,1,2,3,4,6,6,8,6,5,1,2,4,7,6,6]
    #data=[1,7,4,1,2,3,4]
    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
