def solution(numbers):

    num_list = [i for i in range(10)]
    not_existed = (set(num_list) - set(numbers))

    return sum(not_existed)

if __name__ == '__main__':
    numbers = [1,2,3,4,6,7,8,0]
    res = solution(numbers)
    print(res)