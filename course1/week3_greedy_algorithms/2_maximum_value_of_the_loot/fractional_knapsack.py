# Uses python3
import sys

def get_optimal_value(capacity, items):
    value = 0.
    idx=0
    while capacity>=items[idx][1]:
        value+=items[idx][0]
        capacity-=items[idx][1]
        idx+=1
        if idx==len(items):
            break

    if idx<len(items):
        return value+capacity*(float(items[idx][0])/float(items[idx][1]))
    else: return value

def itemSortBool(item):
    return item[0]/float(item[1])

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #st="1 1000\n500 30"
    #data=list(map(int, st.split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    items = []
    for idx in range(n):
        items.append((values[idx],weights[idx]))

    items.sort(key=itemSortBool,reverse=True)
    opt_value = get_optimal_value(capacity, items)
    print("{:.10f}".format(opt_value))
