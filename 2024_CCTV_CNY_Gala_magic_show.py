import random
import time
import pandas as pd

def rotate_list (deck, n):
    actual_n = n % len(deck)
    return deck[actual_n:] + deck[:actual_n]

def put_in_middle(deck, put_count):
    if put_count > len(deck) - 2:
        raise Exception("新年不要太贪！")
    remaining_list = deck[put_count:]
    put_position = random.randint(1, len(remaining_list)-1)
    return remaining_list[:put_position] + deck[:put_count] + remaining_list[put_position:], put_position

def put_in_middle_shi_wu_ban(deck, put_count): # 小泥失误版, code quality重复太多可以改，但暂时不重要
    if put_count > len(deck) - 2:
        raise Exception("新年不要太贪！")
    remaining_list = deck[put_count:]
    put_position = random.randint(1, len(remaining_list)-1)
    return remaining_list[:put_position] + deck[:put_count-1] + remaining_list[put_position:] + deck[put_count-1: put_count], put_position


def good_luck_keep_keep_bad_luck_throw_throw(deck):
    while len(deck) > 1:
        deck = rotate_list(deck, 1)[1:]
    return deck[0]

def magic(deck, error=False):
    name_length = random.randint(1, 10) # 按照名字长度操作
    deck = rotate_list(deck, name_length)
    if error:
        deck, put_position_1 = put_in_middle_shi_wu_ban(deck, 3)
    else:
        deck, put_position_1 = put_in_middle(deck, 3)
    #  # 小泥失误版
    card_kept = deck[0]
    deck = deck[1:]

    place_choice = random.randint(1, max(place_dict.keys())) # 在哪儿过年
    deck, put_position_2 = put_in_middle(deck, place_choice)

    gender_choice = random.randint(1, max(gender_dict.keys())) # 你是mm还是gg
    deck = deck[gender_choice:]

    deck = rotate_list(deck, 7) # 见证奇迹的时刻
    final_card = good_luck_keep_keep_bad_luck_throw_throw(deck)

    # print("card_kept", card_kept)
    # print("final_card", final_card)

    # print("name_length", name_length)
    # print("put_position_1", put_position_1)
    # print("place_choice", place_choice)
    # print("put_position_2", put_position_2)
    # print("gender_choice", gender_choice)
    remarks = "新年快乐！"
    if card_kept[0] != final_card[0]:
        remarks = "汗流浃背了吧小泥！"
    if card_kept[1] == final_card[1]:
        remarks += "wc背面也对不上！！！gg～"


    return {
        "Card Kept": card_kept,
        "Final Card": final_card,
        "Name Length": name_length,
        "Put Position 1": put_position_1,
        "Place Choice": place_dict[place_choice],
        "Put Position 2": put_position_2,
        "Gender Choice": gender_dict[gender_choice],
        "Remarks": remarks
    }


place_dict = {
    1: "南方",
    2: "北方",
    3: "不知道在南方还是北方的留子"
}

gender_dict = {
    1: "gg",
    2: "mm",
    3: "武装直升机"
}


even_back_does_not_match_count = 0

error = True # 小泥失误与否
all_trials = []
for _ in range(1000):
    deck = ['a1', 'b1', 'c1', 'd1', 'a2', 'b2', 'c2', 'd2']
    new_result = magic(deck, error)
    all_trials.append(new_result)
    if new_result["Remarks"].endswith("gg～"):
        even_back_does_not_match_count += 1
    # print(new_result["Remarks"])
    # if new_result["Card Kept"] != new_result["Final Card"]:
    #     print("汗流浃背了吧小泥!")

print(even_back_does_not_match_count/1000) 
df = pd.DataFrame.from_records(all_trials)
if error:
    df.to_csv(f"sample_output/failed_magic_{int(time.time())}.csv", index=False, encoding="utf-8-sig")
else:
    df.to_csv(f"sample_output/successful_magic_{int(time.time())}.csv", index=False, encoding="utf-8-sig")


        
