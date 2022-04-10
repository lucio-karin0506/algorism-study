if __name__ == '__main__':
    import sys
    N = int(sys.stdin.readline())
    graph = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
    print(graph)