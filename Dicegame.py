import random
win_frq=0
lose_freq=0
face_sum=0
for i in range(10000):
    dice1=random.randrange(1,7)
    dice2=random.randrange(1,7)
    face_sum=dice1+dice2
    if face_sum==3 or face_sum==7 or face_sum==5 or face_sum==11 or face_sum==9:
        win_frq+=1
    else:
        lose_freq+=1
if win_frq>lose_freq:
    print("You win the game")
    print("Your win rate is ",win_frq)
    print("Your lose rate is ",lose_freq)
else:
    print("You lose the game")
    print("Your win rate is ",win_frq)
    print("Your lose rate is ",lose_freq)