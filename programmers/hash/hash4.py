def solution(genres, plays):
    play_dict = {}
    play_list = []

    answer = []

    if len(genres) != len(plays):
        return 'error!'
    else:
        for item in zip(genres, plays):
            # 여기서 같은 장르 플레이수 합산 어캐 함..;;
            play_list.append(item)
    print(play_list)
    return answer

if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    result = solution(genres, plays)
    print(result)