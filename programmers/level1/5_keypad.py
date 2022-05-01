def solution(numbers, hand):
    answer = ''

    answer_list = []
    pos_info = ['*', '#']
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer_list.append('L')
            pos_info[0] = num

        elif num == 3 or num == 6 or num == 9:
            answer_list.append('R')
            pos_info[1] = num

        else:
            l_distance = abs(pos_info[0] - num)
            r_distance = abs(pos_info[1] - num)

            if l_distance < r_distance:
                answer_list.append('L')
                pos_info[0] = num

            elif l_distance > r_distance:
                answer_list.append('R')
                pos_info[1] = num
                
            else:
                if hand == 'left':
                    answer_list.append('L')
                    pos_info[0] = num
                elif hand == 'right':
                    answer_list.append('R')
                    pos_info[1] = num

    answer = ''.join(answer_list)

    return answer

if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = 'right'
    res = solution(numbers, hand)
    print(res)