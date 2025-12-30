import art
import random
from data import data


#Format the the data into printable format.
def format_data(account):
    name = account['name']
    description =  account['description']
    country = account["country"]
    return f'{name}, a {description}, from {country}'

def check_answer(user_guess,a_follower,b_follower):
    if a_follower > b_follower:
        return user_guess == 'a'
    else:
        return user_guess == 'b'
     
print(art.logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# Generate the random account form the data
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
        
    print(f'Compare A: {format_data(account_a)}.')
    print(art.vs)
    print(f'Against B: {format_data(account_b)}.')

    #Ask for user  guess:

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print('\n' * 40)
    print(art.logo)
        
    #Check if user is correct or not:
    # - get the follower_count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    # - Use if statments to check if user is corret.
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    #Give some feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's worng. Final score {score}")
        game_should_continue = False
