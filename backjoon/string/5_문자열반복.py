import sys

num = int(sys.stdin.readline())
repeat_info = [list(map(str, sys.stdin.readline().split())) for _ in range(num)]

res = []
for info in repeat_info:
    single_res = []
    repeat_num = info[0]
    repeat_string = info[1]

    for letter in list(repeat_string):
        single_res.append(int(repeat_num)*letter)

    res.append(''.join(single_res))

print('\n'.join(res))