if __name__ == '__main__':
    import sys
    N = int(sys.stdin.readline())
    nums = sys.stdin.readline().split()[0]
    
    res = sum([int(i) for i in list(nums)])
    print(res)