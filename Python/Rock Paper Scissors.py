from random import randint


def keep_score(var_winner):
    player1_score=0;
    player2_score=0;
    player_tie_score=0;
    if var_winner==1:
       player1_score=player1_score+1 
    if var_winner==2:
       player2_score=player2_score+1 
    if var_winner==3:
       player_tie_score=player_tie_score+1 
    
   

def determine_who_wins(var_choice1, var_choice2):
    if var_choice1=="Rock" and var_choice2=="Rock":
        print('No one wins its a Tie')
        return 0
    if var_choice1=="Rock" and var_choice2=="Paper":
        return 2
    if var_choice1=="Rock" and var_choice2=="Scissors":
        print('Player 1 Wins')
        return 1


    if var_choice1=="Scissors" and var_choice2=="Rock":
        print('Player 2 Wins')
        return 2
    if var_choice1=="Scissors" and var_choice2=="Paper":
        print('Player 1 Wins')
        return 1
    if var_choice1=="Scissors" and var_choice2=="Scissors":
        print('No one wins its a Tie')
        return 0

    if var_choice1=="Paper" and var_choice2=="Rock":
        print('Player 1 Wins')
        return 1
    if var_choice1=="Paper" and var_choice2=="Paper":
        print('No one wins its a Tie')
        return 0
    if var_choice1=="Paper" and var_choice2=="Scissors":
        print('Player 2 Wins')
        return 2

player1_score=0;
player2_score=0;
player_tie_score=0;


loop_count = 0
while loop_count<100:


    cpu_player1_choice= randint(1, 3)
    cpu_player2_choice = randint(1, 3)
    cpu_player1_choice_eng="test"
    cpu_player2_choice_eng="test"


    if cpu_player1_choice==1:
        cpu_player1_choice_eng='Rock'
    if cpu_player1_choice==2:
        cpu_player1_choice_eng='Paper'
    if cpu_player1_choice==3:
        cpu_player1_choice_eng='Scissors'


    if cpu_player2_choice==1:
        cpu_player2_choice_eng='Rock'
    if cpu_player2_choice==2:
        cpu_player2_choice_eng='Paper'
    if cpu_player2_choice==3:
        cpu_player2_choice_eng='Scissors'


    print('------------------------------------------')
    print('Game Number: ', loop_count)
    print('------------------------------------------')
    print('Player 1 Picks:' + cpu_player1_choice_eng)
    print('Player 2 Picks:' + cpu_player2_choice_eng)

    winner_int=determine_who_wins(cpu_player1_choice_eng,cpu_player2_choice_eng)
    print('Winner is: ', determine_who_wins(cpu_player1_choice_eng,cpu_player2_choice_eng))
    
    
    
    if winner_int==1:
       player1_score=player1_score+1 
    if winner_int==2:
       player2_score=player2_score+1 
    if winner_int==0:
       player_tie_score=player_tie_score+1 
    
    keep_score(determine_who_wins(cpu_player1_choice_eng,cpu_player2_choice_eng))
    loop_count=loop_count+1


print('------------------------------------------')
print('Total Score')
print('------------------------------------------')

print(player1_score)
print(player2_score)
print(player_tie_score)



if player1_score>player2_score and player1_score>player_tie_score:
    print('player one won the game')

if player2_score>player1_score and player2_score>player_tie_score:
    print('player two won the game')

if player_tie_score>player1_score and player_tie_score>player2_score:
    print('No One Won')