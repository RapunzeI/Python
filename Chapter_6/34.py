from random import *
def warStats():
    card = [i for i in range(2, 15)] * 4
    battle_cnt, war_cnt, twice, twice_war_cnt = 0, 0, 0, 0

    # 카드 섞기
    shuffle(card)

    # 카드 분배
    user1 = card[:26]
    user2 = card[26:]

    # 카드 한 장씩 꺼내기
    while True:
        if len(user1) == 0 or len(user2) == 0: break

        user1_card = user1.pop(0)
        user2_card = user2.pop(0)

        battle_cnt += 1
        
         # 전투
        if user1_card == user2_card:
            user1_war = [user1_card]
            user2_war = [user2_card]

            war_cnt += 1

            while True:
                if len(user1) < 3 or len(user2) < 3:
                    if len(user1) < 3:
                        user1_war += user1
                        user1.clear()
                    if len(user2) < 3:
                        user2_war += user2
                        user2.clear()
                else:
                    user1_war += [user1.pop(0), user1.pop(0), user1.pop(0)]
                    user2_war += [user2.pop(0), user2.pop(0), user2.pop(0)]
                
                if choice(user1_war) > choice(user2_war):
                    user1_war += user2_war
                    shuffle(user1_war)
                    user1 += user1_war
                    break
                elif choice(user1_war) < choice(user2_war):
                    user2_war += user1_war
                    shuffle(user2_war)
                    user2 += user2_war
                    break
                twice += 1
            
            if twice == 2: twice_war_cnt += 1
            twice = 0

        elif user1_card > user2_card:
            user1 += [user1_card, user2_card]
        elif user2_card > user1_card:
            user2 += [user2_card, user1_card]
    
    return (battle_cnt, war_cnt, twice_war_cnt)

print(warStats())