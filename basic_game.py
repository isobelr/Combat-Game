#Isobel Rowe
#Date first created:10/08/18, date last modified: 23/08/18
#This is a simple two-player combat simulator game.


#An intro screen outlining the game rules.
print('Welcome to the Combat Game!')                        
print('\nThe aim of the game is to defeat your opponent by using your $10 to purchase up to 10 units for your army. Each unit costs $1.',
    '\nYour options are Archer (A), Soldier (S), and Knight (K).',
    '\nArcher beats Soldier, Soldier beats Knight, and Knight beats Archer. Anything else is a tie.')

#Confirming the players are ready to start the game.
player_ready = input('\nAre you ready to play? Y/N: ').upper()       
if player_ready == 'Y':
    print('\nHere we go!')
else:
    input('\nWhen you are ready, enter any character: ')


#Creating an empty list to append with players unit choices.
army_1 = []
#Defining the maximum number of moves the player can make, and money the player can use.
max_moves = 10		                    
money_1 = 10
#Initiating the loop to run through players' choices.
while len(army_1) <= max_moves:
    choice = input('\nPlayer 1, choose Archer (A), Soldier (S), Knight (K), or (F) to finish: ').upper()
    army_1.append(choice)
#Adds valid input to army and takes money away.   
    if choice in ('A','S','K'):             
        print('\nCurrent army is: ', army_1),
        money_1 -= 1
        print('Money remaining: ', money_1)
#Prompts user to enter valid input.
    if choice not in ('A','S','K','F'):     
        print ('\nInvalid response. Please enter A, S, K, or F.')
        army_1.pop()
        continue
#Breaks the loop when the Player is finished or their money is exhausted.
    if choice == 'F':                       
        army_1.pop()
        break
    if money_1 == 0:       
        break
print('\nPlayer 1, this is your army: ', army_1)

#Creating the army for player 2, with exactly the same parameters/loops as player 1.
army_2 = []                             
max_moves = 10  
money_2 = 10
while len(army_1) <= max_moves:
    choice = input('\nPlayer 2, choose Archer (A), Soldier (S), Knight (K), or (F) to finish: ').upper()
    army_2.append(choice)
    if choice in ('A','S','K'):
        print('\nCurrent army is: ', army_2),
        money_2 -= 1
        print('Money remaining: ', money_2)
    if choice not in ('A','S','K','F'):
        print ('\nInvalid response. Please enter A, S, K, or F.')
        army_2.pop()
        continue
    if choice == 'F':
        army_2.pop()
        break
    if money_2 == 0:       
        break
print('\nPlayer 2, this is your army: ', army_2, '\n')


#Appending list sizes in the case that they are an uneven length.
if len(army_1) < len(army_2):                           
    army_1.append(None)
if len(army_1) > len(army_2):
    army_2.append(None)
    

#Zipping the armies together into a -----
both_armies = zip(army_1, army_2)


#Setting up a for loop to run through all the choices and comparing each Players choices to one another
for unit_1, unit_2 in both_armies:                      
    if (unit_1 == unit_2):                              
        print ("It's a tie")
    elif (unit_1 == "A") and (unit_2 == "S"):
        print ('Player 1 wins!')
#Inserting the winning unit into starting position (zeroth index) for the next round.
        army_1.insert(0,"A")                            
    elif (unit_1 == "S") and (unit_2 == "K"):
        print ('Player 1 wins!')
        army_1.insert(0,"S")
    elif (unit_1 == "K") and (unit_2 == "A"):
        print ('Player 1 wins!')
        army_1.insert(0,"K")
    elif (unit_1 == "S") and (unit_2 == "A"):          
        print ('Player 2 wins!')
        army_2.insert(0,"A")
    elif (unit_1 == "K") and (unit_2 == "S"):
        print ('Player 2 wins!')
        army_2.insert(0,"S")
    elif (unit_1 == "A") and (unit_2 == "K"):
        print ('Player 2 wins!')
        army_2.insert(0,"K")


#A quick sign off to signal the end of the game.
print('\nThanks for playing! Have a good day.')

