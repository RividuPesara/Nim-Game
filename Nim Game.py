import random
import time

def board(sticks):
    stick_max = max(sticks)
    for row_num, stick_num in enumerate(sticks):
        print(f"{row_num + 1}. {' ' * ((stick_max - stick_num )// 2)}{'🡅' * stick_num}")  # Calculate the number of spaces need to center the sticks and print the pattern

def choose_opponent(): 
    while True:
        opponent_choice = input("To play against the CPU type c or another player type p: ").lower().strip()
        if opponent_choice in ['c', 'p']:
            break
    return opponent_choice

#This function is use to take input from both players
def user_move(sticks):
    while True:
        try:
            selected_row, stick_amount = input("Enter the selected row number first, followed by number of sticks to take (separated by , ): ").split(',')
            selected_row, stick_amount = int(selected_row), int(stick_amount)
            if (1 <= selected_row <= 4 and sticks[selected_row - 1] != 0)and (1 <= stick_amount <= sticks[selected_row - 1]):
                break
        except ValueError:
            continue
    return selected_row, stick_amount

def cpu_move(sticks):
    selected_row = random.randint(1, 4)
    while sticks[selected_row - 1] == 0:
        selected_row = random.randint(1, 4)
    stick_amount = random.randint(1, sticks[selected_row - 1])
    time.sleep(1)
    return selected_row, stick_amount

def print_move(current_player, row, stick_quantity):
    if stick_quantity > 1:
        print(f"{current_player} takes {stick_quantity} sticks from row {row}.\n")
    else:
        print(f"{current_player} takes {stick_quantity} stick from row {row}.\n")

def game_process(user,current_player,opponent):
    sticks = [1, 3, 5, 7]
    while sum(sticks) > 0:
        board(sticks)
        if current_player == user:
            if opponent=='p':
                selected_row, stick_amount = user_move(sticks)
                sticks[selected_row - 1] -= stick_amount
                print_move(current_player, selected_row, stick_amount)
                current_player = "Player 2"
            else:
                selected_row, stick_amount = user_move(sticks)
                sticks[selected_row - 1] -= stick_amount
                print_move(current_player, selected_row, stick_amount)
                current_player = "CPU"

        elif current_player=='CPU':
            selected_row, stick_amount = cpu_move(sticks)
            sticks[selected_row - 1] -= stick_amount
            print_move(current_player, selected_row, stick_amount)
            current_player = user
        else:                                                         #when the current player is the player 2
            selected_row, stick_amount = user_move(sticks)
            sticks[selected_row - 1] -= stick_amount
            print_move(current_player, selected_row, stick_amount)
            current_player = user

    return current_player

def game_style():   #This function asks the user what game style they prefer either last picked is "loser" or "winner"
    while True:
        style=input("Do you wish the last stick picked to be the winner?(y/n): ").lower().strip()
        if style in ['y','n']:
            break
    return style

def main():
    print("Welcome to Nim!")
    user = input("Enter your name: ")
    style=game_style()
    opponent=choose_opponent()
    if opponent=='c':
        players = [user, "CPU"]
    else:
        players=[user,"Player 2"]
    current_player = random.choice(players)
    print(f"Game is starting {current_player} will be going first!\n")
    wins = 0
    losses = 0

    play_again = True
    while play_again:
        winner = game_process(user,current_player,opponent)
        print("Game Over")
        if style=='n':
            if winner == user:                #checks if you won or lost for game style "last picked is loser"
                print(f"Winner is {user}")
                wins += 1 
            else:
                print("You lost.")
                losses += 1
        else:
            if winner !=user:               #checks if you won or lost for game style "last picked is Winner"
                print(f"Winner is {user}")
                wins += 1
            else:
                print("You lost")
                losses += 1
        while True:
            again = input("Would you like to play again? (y/n): ")
            if again.lower().strip() == 'n':
                print("Thank you for playing.")
                print(f"You won {wins} time(s) and lost {losses} time(s).")
                play_again = False
                break
            elif again.lower().strip() == 'y':
                style=game_style()
                opponent=choose_opponent()
                if opponent=='c':
                    players = [user, "CPU"]
                else:
                    players=[user,"Player 2"]
                current_player = random.choice(players)
                print(f"Game is starting {current_player} will be going first!\n")
                break
            else:
                continue
main()
