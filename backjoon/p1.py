import sys

def stackNum(num):
    stack_list = []
    for _ in range(num):
        a = sys.stdin.readline().strip()
        if a[0:4] == 'push':
            stack_list.append(a[5:])
        elif a == 'pop':
            if len(stack_list) == 0:
                print(-1)
            else:
                print(stack_list[-1])
                del stack_list[-1]
        elif a == 'size':
            stack_list_size = len(stack_list)
            print(stack_list_size)
        elif a == 'empty':
            is_empty = len(stack_list)
            if is_empty == 0:
                print(1)
            else:
                print(0)
        elif a == 'top':
            if len(stack_list) == 0:
                print(-1)
            else:
                print(stack_list[-1])

if __name__ == '__main__':
    input_num = int(sys.stdin.readline())
    stackNum(input_num)