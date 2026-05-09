# Computer picks a random number 1–100.
# User keeps guessing until correct.
# Hint: print "Too high" or "Too low" each time.
import random
number = random.randint(1,100)
count =0;
print('I selected a random number.')
while True:
  count += 1
  user_input = int(input(f'Try {count}: Guess the correct number: '))
  if number == user_input:
    print('You are correct')
    break
  elif number > user_input:
    print('Too low: Tray again.')
  else :
    print('Too high: Tray again.')
#while True: