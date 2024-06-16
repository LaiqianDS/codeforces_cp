# Template Codeforces
import sys
input = sys.stdin.readline
import math
     
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
    n, m, a = invr()
    res = []
    if n / a > 0:
        res.append(math.ceil(n/a))
    if m / a > 0:
        res.append(math.ceil(m/a))
    sys.stdout.write(str(f'{res[0]*res[1]}') + "\n")
     
if __name__ == '__main__':
    main()