def solution(n, lost, reserve):
    answer = 0
    all_n_list = [i + 1 for i in range(n)]
    
    if n == len(lost + reserve):
        answer += len(reserve)
    else:
        answer += len(set(all_n_list) - set(lost + reserve)) + len(reserve)

    for i in reserve:
        if i + 1 in lost:
            answer += 1

    return answer

if __name__ == '__main__':
    n = 4
    lost = [3]
    reserve = [2]
    a = solution(n, lost, reserve)
    print(a)