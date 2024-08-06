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
        a1, a2, b1, b2 = invr()
        possible_games = [
            (a1, b1, a2, b2),
            (a1, b2, a2, b1),
            (a2, b1, a1, b2),
            (a2, b2, a1, b1)
        ]
        
        suneet_wins = 0
        
        for g in possible_games:
            suneet_score = 0
            slavic_score = 0
            
            if g[0] > g[1]:
                suneet_score += 1
            elif g[0] < g[1]:
                slavic_score += 1
            
            if g[2] > g[3]:
                suneet_score += 1
            elif g[2] < g[3]:
                slavic_score += 1
            
            if suneet_score > slavic_score:
                suneet_wins += 1
        
        sys.stdout.write(str(suneet_wins) + "\n")
        
if __name__ == '__main__':
    main()