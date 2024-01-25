dx = [-1,0,1,0] # 상우하좌
dy = [0,1,0,-1]

k = int(input())
N = []
for i in range(k):
    N.append(int(input()))

for l in range(k):
    idx = 1
    pos = [0,0]
    snail = [[0] * N[l] for _ in range(N[l])]

    snail[pos[0]][pos[1]] = 1
    i = 2
    while i <= N[l]**2:
        pos[0] += dx[idx % 4]
        pos[1] += dy[idx % 4]
        if 0 <= pos[0] < N[l] and 0 <= pos[1] < N[l]:
            if snail[pos[0]][pos[1]] == 0:
                snail[pos[0]][pos[1]] = i
                i+=1
                continue
        
        pos[0] -= dx[idx % 4]
        pos[1] -= dy[idx % 4]
        idx+=1

    print(f'#{l+1}')
    for row in range(N[l]):
        for col in range(N[l]):
            print(snail[row][col], end=" ")
        print()