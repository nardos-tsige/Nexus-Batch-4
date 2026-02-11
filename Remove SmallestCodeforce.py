def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        a.sort()
        valid = True
        
        for i in range(1, n):
            if a[i] - a[i-1] > 1:
                valid = False
                break
        
        print("YES" if valid else "NO")

if __name__ == "__main__":
    solve()
