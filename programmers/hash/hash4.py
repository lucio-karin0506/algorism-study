def solution(genres, plays):

    if len(genres) == len(plays):
        all_plays = []
        set_genres = set(genres)

        answer = []

        for i in zip(genres, plays):
            all_plays.append(i)

        print(all_plays)
        print(set_genres)
        
        return answer
    else:
        return 'two data length is different!'

if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    result = solution(genres, plays)
    print(result)