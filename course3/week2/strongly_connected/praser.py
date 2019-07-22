x = input()
x = x.split(' ')
for i in range(int(len(x)/2)):
    print(x[2*i], x[2*i+1])
