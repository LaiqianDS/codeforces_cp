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
    pass
     
if __name__ == '__main__':
    for _ in range(inp()):
        A, B = invr()
        if B != 1:
            sys.stdout.write(str('YES') + "\n")
            sys.stdout.write(str(A*B) + ' ' + str(A) + ' ' + str(A*(B+1)) + "\n")
        else:
            sys.stdout.write(str('NO') + "\n")
