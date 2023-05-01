import random

def play():
    user =  input("What's your choice? 'r' for rock, 'p' for paper, and 's' for scissors\n")
    if user == 's':
        player_choice = 'Scissors'
    elif user == 'r':
        player_choice = 'Rock'
    elif user == 'p':
        player_choice = 'Paper'
    else:
        print("Invalid choice, please try again")
        play()
    computer = random.choice(['r','p', 's'])
    if computer == 's':
        computer_choice = "Scissors"
    elif computer == 'r':
        computer_choice = 'Rock'
    else:
        computer_choice = "Paper"
    print(f"The computer chose {computer_choice} for their weapon and the player chose {player_choice} for theirs. TO THE DEATH!")
    if (user == computer):
        return "Tie!"
    if (is_win(user,computer)):
        return "You Won!"
    return "You Lost... Sad"


# r>s, s>p, p>r

def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's'):
        return True
    


print(play())