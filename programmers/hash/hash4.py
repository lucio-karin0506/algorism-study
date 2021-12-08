def solution(genres, plays):

    if len(genres) == len(plays):
        all_plays = []
        genre_play_dict = {}
        answer = []

        for play in zip(genres, plays):
            all_plays.append(play)

        for play_index in range(len(all_plays)):
            pass
            
        # print(all_plays)
        # [('classic', 500), ('pop', 600), ('classic', 150), ('classic', 800), ('pop', 2500)]
        
        return answer
    else:
        return "two datas' length is different!"

if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    result = solution(genres, plays)
    print(result)