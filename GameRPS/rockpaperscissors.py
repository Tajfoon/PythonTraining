from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

typeOfMoves = [rock, paper, scissors]

def choosed(player: str) -> str:
    randomChoose = randint(0, 2)
    print(f'{player} choosed {typeOfMoves[randomChoose]}')
    return randomChoose

playerOneChoose = choosed('Jerry p1')
playerTwoChoose = choosed('Alex p2')

if(playerOneChoose == 1 and playerTwoChoose == 0) or (playerOneChoose == 0 and playerTwoChoose == 2) or (playerOneChoose == 2 and playerTwoChoose == 1):
    print("Player one WIN!")
elif(playerOneChoose == playerTwoChoose):
    print("TIE!!!!")
else:
    print("Player two WIN!")




