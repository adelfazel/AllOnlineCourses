# Uses python3
def intilizeDistMatrix(dimx,dimy):
    distance_matrix = [[0 for _ in range(dimx)] for _ in range(dimy)]
    for i in range(1,dimy):
        distance_matrix[i][0]=i

    for i in range(1,dimx):
        distance_matrix[0][i]=i
    return distance_matrix


def edit_distance(s, t):
    dimx=len(t)
    dimy=len(s)
    distance_matrix=intilizeDistMatrix(dimx+1,dimy+1)
    candidates=[0]*3
    route=[]
    for i in range(1,dimy+1):
        for j in range(1,dimx+1):
            candidates[0]=distance_matrix[i-1][j]+1
            candidates[1]=distance_matrix[i][j-1]+1
            if (s[i-1]==t[j-1]):
                candidates[2]=distance_matrix[i-1][j-1]
            else:
                candidates[2]=distance_matrix[i-1][j-1]+1
            distance_matrix[i][j]=min(candidates)


    return distance_matrix[dimy][dimx]

if __name__ == "__main__":
    # a=str(input(''))
    # b=str(input(''))
    print(edit_distance(input(), input()))
    print(edit_distance(a, b))
