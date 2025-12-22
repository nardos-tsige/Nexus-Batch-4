if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    maxx = max(arr)
    while maxx in arr:
        arr.remove(maxx)
    print(max(arr))
        
    
        
