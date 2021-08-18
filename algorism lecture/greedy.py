# problem 1
def calc(n, k):
    count = 0

    while n != 1:
        if n % k == 0:
            n = n / k
            count += 1
        else:
            n = n - 1
            count += 1
        if n == 1:
            break
    
    return count

# problem 2
def calc2(data):
    result = int(data[0])

    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or result <=1:
            result += num
        else:
            result *= num

    return result

if __name__ == '__main__':
    # a, b = map(int, input('input numbers: ').split())
    # result = calc(a, b)
    # print(result)

    a = input()
    result = calc2(a)
    print(result)
