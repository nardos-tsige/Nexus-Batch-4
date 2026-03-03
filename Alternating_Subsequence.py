def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        total = 0
        i = 0
        
        while i < n:
            curr_max = arr[i]
            curr_sign = 1 if arr[i] > 0 else -1
            
            j = i + 1
            while j < n and (arr[j] > 0) == (arr[i] > 0):
                curr_max = max(curr_max, arr[j])
                j += 1
            
            total += curr_max
            i = j
        
        print(total)

if __name__ == "__main__":
    solve()
