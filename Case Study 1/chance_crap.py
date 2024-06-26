import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def calculate_sum(die1, die2):
    return die1 + die2

def play_game():
    die1, die2 = roll_dice()
    sum_of_dice = calculate_sum(die1, die2)
    print(f'You rolled {die1} + {die2} = {sum_of_dice}')
    
    # First roll rules
    if sum_of_dice in [7, 11]:
        print('You win!')
        return
    elif sum_of_dice in [2, 3, 12]:
        print('Craps! You lose.')
        return
    else:
        point = sum_of_dice
        print(f'Your point is {point}. Continue rolling until you make your point or roll a 7 to lose.')
        
        while True:
            die1, die2 = roll_dice()
            sum_of_dice = calculate_sum(die1, die2)
            print(f'You rolled {die1} + {die2} = {sum_of_dice}')
            
            if sum_of_dice == point:
                print('You make your point! You win!')
                return
            elif sum_of_dice == 7:
                print('You rolled a 7. You lose.')
                return

if __name__ == "__main__":
    play_game()
