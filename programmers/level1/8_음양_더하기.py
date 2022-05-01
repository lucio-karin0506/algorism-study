def solution(absolutes, signs):

    for idx, num_info in enumerate(list(zip(absolutes, signs))):
        if num_info[1] == False:
            absolutes[idx] = -num_info[0]

    return sum(absolutes)

if __name__ == '__main__':
    absolutes = [1,2,3]
    signs = [False, False, True]

    res = solution(absolutes, signs)
    print(res)