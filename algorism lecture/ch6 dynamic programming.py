def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

'''
dynamic programming
    1. 큰 문제를 작은 문제로 나눌 수 있다.
    2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일함.
'''

if __name__ == '__main__':
    print(fibo(4)) # 시간복잡도가 x가 커질수록 기하급수적으로 증가함...