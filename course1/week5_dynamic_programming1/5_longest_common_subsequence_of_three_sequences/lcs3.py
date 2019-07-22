#Uses python3

import sys

def intilizeDistMatrix(dimx,dimy,dimz):
    distance_matrix = [[[0 for _ in range(dimx)] for _ in range(dimy)] for _ in range(dimz)]
    return distance_matrix

def lcs3(a, b, c):

        #write your code here
    dimx=len(a)
    dimy=len(b)
    dimz=len(c)

    distance_matrix=intilizeDistMatrix(dimx+1,dimy+1,dimz+1)
    candidates=[0]*9
    for i in range(1,dimy+1):
        for j in range(1,dimx+1):
            for k in range(1,dimz+1):

                candidates[0]=distance_matrix[i][j][k-1]
                candidates[1]=distance_matrix[i][j-1][k]
                candidates[2]=distance_matrix[i][j-1][k-1]
                candidates[3]=distance_matrix[i-1][j][k]



                if (a[i-1]==b[j-1] and a[i-1]==c[k-1]):
                    candidates[2]=distance_matrix[i-1][j-1][k-1]+1
                else:
                    candidates[2]=-1
                    # candidates[2]=0
                distance_matrix[i][j]=max(candidates)
    return distance_matrix[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
