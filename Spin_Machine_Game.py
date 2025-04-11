import random


def deposit():
    while True:
        amount = int(input("What amount($) would you like to deposit?"))
        if amount < 0 :
            print("Enter amount greater than zero.")
        else:
            return amount

def bet(balance):
    while True:
        bet_amount = int(input("What bet amount($) would you like to bet?"))
        if bet_amount < 0 :
            print("Enter bet amount greater than 0.")
        elif bet_amount > balance:
            print("Enter bet amount less than or equal to balance")
        else:
            return bet_amount


def game(game_bet, game_balance):
    while True:
        r1,r4,r7 = random.choices(choices, k=3)
        r2,r5,r8 = random.choices(choices, k=3)
        r3,r6,r9 = random.choices(choices, k=3)
        game_print = f"""
        {r1} | {r2} | {r3}
        {r4} | {r5} | {r6}
        {r7} | {r8} | {r9}
        """
        
        print(game_print)

        game_balance =  game_balance - game_bet
        
        if r4==r5 and r5==r6:
         prize = 2*game_bet
         print(f"You won ${prize}")
         game_balance = game_balance + prize
         print(f"Your new balance is {game_balance}")
                
        else:
          print(f"You Lost!")
          print(f"Your new balance is ${game_balance}")
            

        game_check = input("Do you want to play the slot machine(Y/N)?")
        if game_check.lower() in ['n', 'no']:
            return game_balance
        elif game_check.lower() in['y', 'yes']:
            if game_balance < game_bet:
                print("you don't have enough balance to play again.")
                return game_balance


choices = ['A','B','C','D']
user_balance = deposit()
user_bet = bet(balance=user_balance)

game(game_bet = user_bet, game_balance = user_balance)