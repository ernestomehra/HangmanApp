movies = ['Diljale', 'Khoobsurat', 'Dangal', 'Aashiqui']

import random
selected = random.choice(movies).casefold()

intermediate = []

for char in selected:
  if char not in ['a','e','i','o','u']:
    char = '*'
  intermediate.append(char)

masked = ''.join(intermediate)

print(masked)

guesses = []
turns = 3

while turns > 0:
  if '*' in intermediate:
    guess = input('Enter a guess...\n').casefold()
    if (guess in selected) and (guess not in guesses):
      print('Yes, thats a correct guess...enter another guess\n')
      position = selected.index(guess)
      intermediate[position] = guess
    elif guess not in selected:
      turns -= 1
      print(f'Sorry, this is a wrong guess...you have {turns} left...')
      
    guesses.append(guess)
  elif '*' not in intermediate:
    result = ''.join(intermediate)
    print(f'you won...the movie is {result}')
    break
else:
  print(f'Sorry, you lost..the correct answer is {selected}')
  
