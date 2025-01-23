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
    return(list(s[:len(s) - 1]))
def invr(): # separated int
    return(map(int,input().split()))

############ ---- Problem Solution ---- ############
def main():
    c = inp()
    coins = inlt()
    coins.sort()
    total = sum(coins)
    print(coins)
    s, i = 0, 0
    while s <= total-s:
        print((s, total-s))
        s += coins.pop()
        i += 1
    print(i)


if __name__ == '__main__':
    main()