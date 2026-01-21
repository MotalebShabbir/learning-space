# Ask user for a number.
# Print its multiplication table from 1 to 10.
user_input = int(input('Enter a number: '))
print('multiplication table')
print('===================')
for n in range(1,11):
  print(f'{user_input}×{n} = {user_input*n}')