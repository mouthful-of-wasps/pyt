def prettyPrint():
  print() 
  for row in listOfShame: 
    for item in row: 
      # item refers to each item in the column for that row
     print(f"{item:^10}", end=" | ") 
      # :^10 means 10 characters as the space with the data in the center. The end character has been changed to space vertical line space to make it look more like a table.
      
    print() 
    
  print()
    

listOfShame = [] 

while True: 
  menu = input("Add or Remove?") # Gives the user a choice prompt and stores their input.

  if(menu.strip().lower()[0]=="a"): # Uses selection to run the 'add' code if user inputs 'a'. I've "sanitized" the input here too.
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref] 
  
    listOfShame.append(row) 
    # All the 'add' code is now indented, so it's part of the 'add' branch and will only run if the user enters 'a'.

  else: # If the user doesn't choose 'a', run this new remove code instead.
    name = input("What is the name of the record to delete?") # Get the input of a name
    for row in listOfShame: # Use a loop to extract one row at a time
      
      if name in row: # Check if the name is in the extracted row.
        listOfShame.remove(row) # remove the whole row if name is in it

  prettyPrint()




  import random, os, time

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    for item in row:
      print(item, end="\t|\t")
    print()

def createCard():
  global bingo
  numbers = []
  for i in range(8):
    num = ran()
    while num in numbers:
      num = ran()
    numbers.append(ran())
  
  numbers.sort()
  
  bingo = [ [ numbers[0], numbers[1], numbers[2]],
            [ numbers[3], "BG", numbers[4] ],
            [ numbers [5], numbers[6], numbers[7]]
          ]

createCard()
while True:
  prettyPrint()
  num = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == num:
        bingo[row][item] = "X"

  exes = 0
  for row in bingo:
    for item in row:
      if item=="X":
        exes+=1

  if exes == 8:
    print("You have won")
    break

  time.sleep(1)
  os.system("clear")