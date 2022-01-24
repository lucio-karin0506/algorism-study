def section_sum(idx, total):
    global answer
    
    # 모든 행을 다 돌았을 때,
    if idx == N:
        if total < answer:
            answer = total
            return

    if total > answer:
        return

    for i in range(N):
        if i not in visited:
            visited.append(i)
            section_sum(idx+1, total+matrix[idx][i])
            visited.pop()

if __name__ == '__main__':
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(N)]

        answer = 30
        visited = []

        section_sum(0, 0)
        print('#{} {}'.format(tc, answer))