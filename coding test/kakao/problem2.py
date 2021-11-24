def solution(n, k):
    answer = ''
    prime_num_count = 0
    prime_num = []

    while n // k >= 1:
        remain = n % k
        n = n // k
        answer = str(remain) + answer
        if n < k :
            answer = str(n) + answer

    for i in answer:
        not_prime = 0
        for n in range(2, int(i)):
            if int(i) % n == 0:
                not_prime = 1
        if not_prime == 0:
            prime_num.append(n)

    prime_num = list(set(prime_num))

    for i in answer:
        for num in prime_num:
            if int(i) == num:
                prime_num_count += 1
            else:
                prime_num_count += 0

    return prime_num_count

if __name__ == '__main__':
    n = 437674
    k = 3
    res = solution(n, k)
    print(res)