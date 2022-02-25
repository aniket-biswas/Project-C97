print("*"*10,"Number guessing Game","*"*10)
import random

n=random.randint(1,9)#number
c=0
while c<5: 
  # c=chances
  g=int(input("Guess a number between 1 to 9:"))#guess
  if g>9:
    print("The no is greater than 9")
  elif g<1:
    print("The no is smaller than 1")
  elif n==g:
    print("You won")
  else:
    print("You lose")
  c+=1
if not c < 5:
    print("YOU LOSE! The number is", n)
