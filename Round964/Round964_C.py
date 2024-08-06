# Template Codeforces
import sys
input = sys.stdin.readline
     
    ############ ---- Input Functions ---- ############
def inp(): #integer
    return(int(input()))
def inlt(): # list
    return(list(map(int,input().split())))
def insr(): # string
    s = input()
    return("".join(list(s[:len(s) - 1])))
def invr(): # separated int
    return(map(int,input().split()))
     
    # sys.stdout.write(str('yes') + "\n")
     
############ ---- Problem Solution ---- ############
def main():
    for _ in range(inp()):
        n, s, m = invr()
        aux = []
        yes = False
        prev = 0

        for j in range(n):
            l, r = invr()
            aux.append(l-prev)
            prev = r
        aux.append(m-prev)
        
        if any(s <= x for x in aux):
            sys.stdout.write("YES" + "\n")
        else:
            sys.stdout.write("NO" + "\n")

if __name__ == '__main__':
    main()