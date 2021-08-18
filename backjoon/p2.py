import sys

def checkVPS(num):
    vps_list = []
    for _ in range(num):
        a = sys.stdin.readline().strip()
        if a[0] == '(' and a[-1] == ')':
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    input_num = int(sys.stdin.readline())
    checkVPS(input_num)