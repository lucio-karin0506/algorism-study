if __name__ == '__main__':
    word = list(input().upper())
    letter_list = list(set(word))

    cnt_dic = {}
    for letter in letter_list:
        cnt_dic[letter] = word.count(letter)

    cnt_val = list(cnt_dic.values())
    max_val = max(cnt_val)

    # 최대값이 하나일 경우
    if cnt_val.count(max_val) == 1:
        for info in cnt_dic.items():
            if info[1] == max_val:
                print(info[0])
    # 최대값이 두 개 이상일 경우
    else:
        print('?')