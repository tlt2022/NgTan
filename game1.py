#!/bin/python3

from random import randint

# fire burns logs
# logs make a bridge over water
# water puts out fire
# fire -> _M_
# logs -> @@@
# water -> ~~~
  
player = input('fire (f), logs (l) or water (w)?')

if player == 'f':
  print('_M_', end=' ')
  
elif player == 'l':
  print('@@@', end=' ')
  
elif player == 'w':
  print('~~~', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

chosen = randint(1,3)

if chosen == 1 :
  computer = 'f'
  print('_M_')
  
elif chosen == 2 :
  computer = 'l'
  print('@@@')
  
else:
  computer = 'w'
  print('~~~')

if player == computer:
  print('DRAW!')
  
elif player == 'f' and computer == 'l':
  print('Player wins!')
  
elif player == 'f' and computer == 'w':
  print('Computer wins!')
  
elif player == 'l' and computer == 'f':
  print('Computer wins!')
  
elif player == 'l' and computer == 'w':
  print('Player wins!')

elif player == 'w' and computer == 'f':
  print('Player wins!')
  
elif player == "w" and computer == 'l':
  print('Computer wins!')

else:
  print('Huh?')