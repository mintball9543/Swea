T = int(input())
arr = []
result = []
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split(" ")))
    result.append(max(arr) - min(arr))

for i in range(T):
    print(f"#{i+1}",end=" ")
    print(result[i])