def solution(n):
    answer = [i + 1 for i in range(n)]
    not_prime_num = []
    prime_num = []
    
    for i in answer:
        for num in range(2, i):
            if i % num == 0:
                not_prime_num.append(i)
    
    prime_num = list(set(answer) - set(not_prime_num))
    prime_num.remove(1)

    return answer

if __name__ == '__main__':
    n = 12
    res = solution(n)
    print(res)