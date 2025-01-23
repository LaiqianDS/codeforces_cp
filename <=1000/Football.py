# Template Codeforces
import sys
input = sys.stdin.readline
print = sys.stdout.write

############ ---- Input Functions ---- ############
def inp(): #integer
    return(int(input()))
def inlt(): # list
    return(list(map(int,input().split())))
def insr(): # string
    s = input()
    return(list(s[:len(s) - 1]))
def invr(): # separated int
    return(map(int,input().split()))

############ ---- Problem Solution ---- ############
def main():
    c = '0'
    cont = 0
    f = False
    for char in insr():
        if char == c:
            cont += 1
        else: 
            c = char
            cont = 1
        if cont >= 7:
            print("YES\n")
            f = True
            break
    if not f:
        print("NO\n")
    
if __name__ == '__main__':
    main()