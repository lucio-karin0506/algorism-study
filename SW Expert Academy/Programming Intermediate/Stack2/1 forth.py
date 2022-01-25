def forth(input_list):
    ans_list = []

    for letter in input_list:
        # 1. type check
        if letter.isnumeric() == True:
            ans_list.append(int(letter))
        else:
            n1 = 0
            n2 = 0

            if letter == '.':
                if len(ans_list) == 1:
                    return ans_list[0]
                else:
                    return 'error'

            # . 연산자 나오기도 전에 길이 1이면 error
            if len(ans_list) < 2:
                return 'error'
            else:
                n1 = ans_list.pop()
                n2 = ans_list.pop()

            if letter == '+':
                ans_list.append(n1 + n2)
            elif letter == '-':
                ans_list.append(n1 - n2)
            elif letter == '*':
                ans_list.append(n1 * n2)
            elif letter == '/':
                ans_list.append(n1 // n2)

def forth2(input_list):
    ans_list = []

    for letter in input_list:
        # 1. type check
        if letter.isnumeric() == True:
            ans_list.append(int(letter))
        else:
            if letter == '.':
                if len(ans_list) == 1:
                    ans = ans_list.pop()
                    return ans
                else:
                    return 'error'

            try:
                num1 = ans_list.pop()
                num2 = ans_list.pop()

                if letter == '+':
                    ans_list.append(num1+num2)
                elif letter == '-':
                    ans_list.append(num1-num2)
                elif letter == '*':
                    ans_list.append(num1*num2)
                elif letter == '/':
                    ans_list.append(num1//num2)

            except IndexError:
                return 'error'


if __name__ == '__main__':
    T = int(input())
    res = []

    for _ in range(1, T + 1):
        input_list = list(input().split())
        ans = forth(input_list)
        res.append(ans)

    for idx, value in enumerate(res):
        print(f'#{idx+1} {value}')