num_list = list(input())
res = []
for idx in range(len(num_list)):
    num_list1 = num_list[0:idx]
    num_list2 = num_list[idx:]

    if len(num_list1) != 0 and len(num_list2) != 0:
        num_res1 = eval('*'.join(num_list1))
        num_res2 = eval('*'.join(num_list2))

        if num_res1 == num_res2:
            res.append('YES')
        else:
            pass

if len(res) != 0:
    print('YES')
else:
    print('NO')