import random

###Training Algorithm###
'''def GetPiles():
  PileList = [random.randint(1, 100) for _ in range(3)]
  return PileList'''

###REQUEST A POSITIVE AMOUNT OF CHIPS AND RETURN AS A LIST###
def GetPiles():
  while True:
    PileInput = input("Enter a positive number of chips for piles A B C: ")
    PileList = PileInput.split()

    try:
      PileList = [int(num) for num in PileList]
      if all(num >= 0 for num in PileList):
        return PileList
      else:
        print("Please enter positive integers only.")

    except ValueError:
      print("Please enter valid positive integers only.")

###FIND AND RETURN THE UNSAFE MOVES###
def unsafeMoves():
  unsafeList = []
  with open('unsafe.start', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

    for line in lines:
      unsafeString = line.split()
      unsafeString = [int(num) for num in unsafeString]
      unsafeList.append(unsafeString)

  return unsafeList

###FIND AND RETURN THE NEXT POSSIBLE MOVES###
def nextMoves(pileList):
  nextList = []
  for i in [0, 1, 2]:
    for j in [3, 2, 1]:
      if pileList[i] - j >= 0:
        temp = pileList[:]
        temp[i] = temp[i] - j
        nextList.append(temp)
    
  return nextList

###UPDATE THE UNSAFE FILE###
def updateUnsafe(unsafeList, PileList):
  tempList = []
  
  for i in [0, 1, 2]:
    for j in [1, 2, 3]:
      if PileList[i] + j >= 0:
        temp = PileList[:]
        temp[i] = temp[i] + j
        tempList.append(temp)

  for i in tempList:
    if i not in unsafeList:
      unsafeList.append(i)
        
  unsafeList = sorted(unsafeList)
  
  with open('unsafe.start', 'w') as file:
      for i in unsafeList:
          unsafeStr = ' '.join(map(str, i))
          file.write(unsafeStr + '\n')

###DETERMINE THE WINNER###
def determineWinner(player):
  if player == "Human":
    return "Human"
  else:
    return "Machine"

###GET THE PILE CHOICE AND THE CHIPS TO REMOVE###
def HumanMove(PileList):
  while True:
    try:
      pile_choice, amount = input(
          "\nEnter the pile letter (A, B, C) and the number of chips to remove: "
      ).split()
      pile_choice = pile_choice.upper()

      if pile_choice not in ['A', 'B', 'C']:
        print("\nInvalid pile choice. Please choose A, B, or C.")
        continue

      if pile_choice == 'A':
        pile_index = 0
      elif pile_choice == 'B':
        pile_index = 1
      else:
        pile_index = 2

      if PileList[pile_index] == 0:
        print("\nThat pile is already empty. Please choose a different pile.")
        continue

      amount = int(amount)

      if amount <= 0 or amount > PileList[
          pile_index] or amount > 3:
        print(
            "\nInvalid number of chips. Please enter a positive integer between 1 and 3."
        )
        continue

      PileList[pile_index] -= amount

      print(f"\nThe Human will take {amount} chip(s) from pile {pile_choice}.")
      print("THE NUMBER OF CHIPS IN EACH PILE NOW:\nA: {}    B: {}    C: {}\n".format(PileList[0], PileList[1], PileList[2]))
      break
    except ValueError:
      print("Invalid input. Please enter the pile letter (A, B, C) "
            "and the number of chips to remove separated by a space.")

      
###GET THE PILE CHOICE AND THE CHIPS TO REMOVE USING INTELLIGENCE AND LEARNING ALGORITHMS###
def MachineMove(PileList):
  possibleMoves = nextMoves(PileList)
  unsafeList = unsafeMoves()

  for move in possibleMoves:
    if move not in unsafeList:
      nextMove = move
      break
    else:
      updateUnsafe(unsafeList, PileList)
      nextMove = move

  for i in range(len(PileList)):
    if PileList[i] != nextMove[i]:
        pile_choice = i
        amount = PileList[i] - nextMove[i]
        break

  PileList = nextMove
  
  if pile_choice == 0:
    pile_choice = 'A'
  elif pile_choice == 1:
    pile_choice = 'B'
  else:
    pile_choice = 'C'
    
  print(f"I take {amount} chip(s) from pile {pile_choice}.")
  print("The number of chips in each pile after the computer moves is:\nA: {}    B: {}    C: {}".format(PileList[0], PileList[1], PileList[2]))

  return PileList

###CONTROL THE FLOW OF GAMEPLAY###
def Play(PileList):
  print(
      "\nThe number of chips in each pile initially:\nA: {}    B: {}    C: {}".
      format(PileList[0], PileList[1], PileList[2]))
  
  start = input("\nType 0 if you want the MACHINE to start, and 1 if YOU want to start: ")

  player = "Human" if start == "1" else "Machine"

  while any(PileList):
    if player == "Human":
      HumanMove(PileList)
      
      ###Training Algorithm###
      '''PileList = MachineMove(PileList)'''
      
      player = "Machine"
      
    else:
      PileList = MachineMove(PileList)
      player = "Human"

  winner = determineWinner(player)
  print(f"\nThe winner is: The {winner}\n")


###START THE GAME###
playtime = "Y"
while playtime == "Y":
  PileList = GetPiles()
  Play(PileList)
  playtime = input("Play Again? (Y/N): ")

