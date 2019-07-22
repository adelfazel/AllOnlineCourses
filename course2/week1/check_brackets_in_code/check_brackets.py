# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def ops(x):
    if x==")":
        return "("
    elif x=="]":
        return "["
    elif x=="}":
        return "{"

def find_mismatch(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):
        #print(i),

        if next in "([{":
            opening_brackets_stack.append((i,str(next)))

        elif next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i+1
            else:
                if opening_brackets_stack[-1][1]==ops(str(next)):
                    opening_brackets_stack.pop()
                else:
                    return i+1

    if opening_brackets_stack==[]:
        return "Success"
    else:
        return opening_brackets_stack[0][0]+1

def main():
    text = input()
    #text="{[}"
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    #print()
    print(mismatch)

if __name__ == "__main__":
    main()
