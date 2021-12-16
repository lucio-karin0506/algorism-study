from collections import Counter
import operator

def solution(genres, plays):

    if len(genres) == len(plays):
        all_plays = list(zip(genres, plays))
        play_count = []
        answer = []

        # tuple to dict
        for play in all_plays:
            play_count_dict = {}
            play_count_dict[play[0]] = play[1]
            play_count.append(play_count_dict)

        # 장르별 재생수 합산
        total_count = Counter({})
        for play in play_count:
            total_count += Counter(play)
        
        total_play_count = dict(sorted(dict(total_count).items(), key=operator.itemgetter(1), reverse=True))

        # 장르 별 총 재생 수가 정렬되어 반영된 장르 리스트
        total_play = [genre for genre in total_play_count.keys()]
        
        # print(total_play) => ['pop', 'classic']
        # print(all_plays) => [('classic', 500), ('pop', 600), ('classic', 150), ('classic', 800), ('pop', 2500)]

        # 장르 별 재생 수 정렬
        for genre in total_play:
            play_count_by_genre = []

            for index in range(len(all_plays)):
                all_plays_genre = all_plays[index][0]
                all_plays_count = all_plays[index][1]

                if genre == all_plays_genre:
                    play_count_by_genre.append(all_plays_count)

            play_count_by_genre = sorted(play_count_by_genre, reverse=True)
            print(play_count_by_genre)

            for i in play_count_by_genre[:2]:
                for index in range(len(plays)):
                    if i == plays[index]:
                        # if plays.count(i)
                        answer.append(index)

        return answer
    else:
        return "two datas' length is different!"

if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [150, 600, 150, 800, 2500]
    result = solution(genres, plays)
    print(result)