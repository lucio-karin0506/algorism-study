def solution(a, b):
    
    return sum([i[0]*i[1] for i in zip(a, b)])

if __name__ == '__main__':
    a = [1,2,3,4]
    b = [-3,-1,0,2]

    res = solution(a, b)
    print(res)