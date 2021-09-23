def solution(fees, records):
    answer = []
    basic_time = fees[0]
    basic_fee = fees[1]
    period_time = fees[2]
    period_fee = fees[3]

    car_fee_records = {}
    car_time_fee = []

    for i in records:
        car_num = i.split(' ')[1]
        time = 0
        car_fee_records[car_num] = basic_fee + ((time - basic_time) / period_time) * period_fee

    return answer

if __name__ == '__main__':
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

    res = solution(fees, records)
    print(res)