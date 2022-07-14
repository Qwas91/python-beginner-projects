import random

def play():
    user = input("Whta's yout choice? \n'r' for rock, 'p' for paper, 's' for sissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    elif is_win(user, computer):
        return 'You won!'
    return 'You lost!'

def is_win(player, opponent):
#return true if player wins
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 

print(play())