T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split(" "))
    V = list(map(int, input().split(" ")))

    max_sum = min_sum = sum(V[:M])
    for i in range(1,N-M+1):
        cur_sum = sum(V[i:i+M])
        print(V[i:i+M])
        print(cur_sum)
        max_sum = max(max_sum, cur_sum)
        min_sum = min(min_sum, cur_sum)
    
    result.append(max_sum - min_sum)

for i in range(len(result)):
    print(f"#{i+1} {result[i]}")