print('Welcome to the GuessingGame')

user_name = input('What is your name')
secret_number = '8'

print('Hello:', user_name)
print('Guess the secret number')

user_guess = input()

if user_guess == secret_number:
   print('correct, you win')
else:
   print('wrong, guess again')
   
user_guess = input()

if user_guess == secret_number:
    print('correct,you win')
else:
    print('wrong, guess again')
    
user_guess = input()
 
if user_guess == secret_number:
    print('correct,you win')
else:
    print('wrong, game over')
    
user_guess = input()
