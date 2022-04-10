import sys
N = int(sys.stdin.readline())
ox_list = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

def get_num(o_list):
    return sum([i+1 for i in range(len(o_list))])

for ox in ox_list:
    ox = ox[0]
    o_list = [list(i) for i in ox.split('X') if i != '']
    o_num_list = [get_num(i) for i in o_list]
    print(sum(o_num_list), end='\n')