def solution(N, number):
    answer = -1
    
    # 계산에 사용하고자 하는 N과 그에 대한 사칙연산 결과 값 number가 같을 경우 최소 연산 횟수는 1이므로
    # answer = 1 return
    if number == N:
        return 1

    s = [set() for _ in range(8)]

    # s=[{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]
    for i in range(8):
        temp = int(str(N)*(i+1))
        s[i].add(temp)

    for i in range(1, 8): # i가 1~7까지 순회 => 계산된 수 집어 넣을 인덱스
        for j in range(i): # j는 i만큼 순회
            for x1 in s[j]: # j+1개로 만들 수 있는 조합 하나씩 꺼냄
                for x2 in s[i-j-1]:
                    s[i].add(x1 + x2)
                    s[i].add(x1 - x2)
                    s[i].add(x1 * x2)
                    if x2 != 0:
                        s[i].add(x1 // x2)

        if number in s[i]:
            return i+1

    return answer

if __name__ == '__main__':
    N = int(input())
    number = int(input())
    res = solution(N, number)
    print(res)