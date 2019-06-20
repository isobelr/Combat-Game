#Isobel Rowe
#Date first created:16/08/18, date last modified: 24/08/18
#This is the extended combat simulator game.


#Added rules for the game extensions.
print('Welcome to the Extended Combat Game!')                     
print('\nThe aim of the game is to defeat your opponent by using your $10 to purchase up to 10 units for your army.',
    '\nYour options are Archer (A), Soldier (S), Knight (K), Siege Equipment (SE), or Wizard (W).',
    '\nArcher beats Soldier, Soldier beats Knight, and Knight beats Archer.',
    '\nSiege Equipment beats everything other than Knights and Wizards. Wizards beat everything other than Archers. Anything else is a tie.',
    '\nArchers, Soldiers, and Knights cost $1. Siege Equipment costs $2, and Wizards cost $3.',
    '\nIn the event that you lose a round and you still have money remaining for Medics, your losing unit will be revived and returned to the back of your army.')

player_ready = input('\nAre you ready to play? Y/N: ').upper()   
if player_ready == 'Y':
    print('\nHere we go!')
else:
    input('\nWhen you are ready, enter any character: ')


army_1 = []                                                               
max_moves = 10                                                          
money_1 = 10
while len(army_1) <= max_moves:
    choice = input('\nPlayer 1, choose Archer (A), Soldier (S), Knight (K), Siege Equipment (SE), Wizard (W), or (F) to finish: ').upper()
    army_1.append(choice)
#Giving the new units different costs based on strength.
    if choice == 'SE':        
        money_1 -= 2
    elif choice == 'W':
        money_1 -= 3
    elif choice in ('A','S','K'):
        money_1 -= 1
    print('Current army is: ', army_1)
    print('Money remaining: ', money_1)
    if choice not in ('A','S','K','F', 'SE', 'W'):                                     
        print ('\nInvalid response. Please enter A, S, K, SE, W, or F.')
        army_1.pop()
        continue
    if choice == 'F':                                                               
        army_1.pop()
        break
    if money_1 == 0:       
        break
print('\nPlayer 1, this is your army: ', army_1)
#Added print statement for the medics.
print('Money remaining for the hire of medics: ', money_1,)   

army_2 = []                                                               
max_moves = 10                                                          
money_2 = 10
while len(army_2) <= max_moves:
    choice = input('\nPlayer 2, choose Archer (A), Soldier (S), Knight (K), Siege Equipment (SE), Wizard (W), or (F) to finish: ').upper()
    army_2.append(choice)
    if choice == 'SE':          
        money_2 -= 2
    elif choice == 'W':
        money_2 -= 3
    elif choice in ('A','S','K'):
        money_2 -= 1
    print('Current army is: ', army_2)
    print('Money remaining: ', money_2)
    if choice not in ('A','S','K','F', 'SE', 'W'):                                     
        print ('\nInvalid response. Please enter A, S, K, SE, W, or F.')
        army_2.pop()
        continue
    if choice == 'F':                                                               
        army_2.pop()
        break
    if money_2 == 0:       
        break
print('\nPlayer 2, this is your army: ', army_2)
print('Money remaining for the hire of medics: ', money_2, '\n')


if len(army_1) < len(army_2):       
    army_1.append(None)
if len(army_1) > len(army_2):
    army_2.append(None)
    

both_armies = zip(army_1, army_2)

for unit_1, unit_2 in both_armies:
    if (unit_1 == unit_2):
        print ("It's a tie!")
    elif (unit_1 == "A") and (unit_2 == "S"):
        print ('Player 1 Wins!')
        army_1.insert(0,"A")
#Adding the losing unit to the back of the army where funds aren't exhausted.
        if money_2 >1:
            army_2.append('S')
            money_2 -=1
    elif (unit_1 == "S") and (unit_2 == "K"):
        print ('Player 1 Wins!')
        army_1.insert(0,"S")
        if money_2 >1:
            army_2.append('K')
            money_2 -=1
    elif (unit_1 == "K") and (unit_2 == "A"):
        print ('Player 1 Wins!')
        army_1.insert(0,"K")
        if money_2 >1:
            army_2.append('A')
            money_2 -=1
    elif (unit_1 == "S") and (unit_2 == "A"):
        print ('Player 2 wins!')
        army_2.insert(0,"A")
        if money_1 >1:
            army_1.append('S')
            money_1 -=1
    elif (unit_1 == "K") and (unit_2 == "S"):
        print ('Player 2 wins!')
        army_2.insert(0,"S")
        if money_1 >1:
            army_1.append('K')
            money_1 -=1
    elif (unit_1 == "A") and (unit_2 == "K"):
        print ('Player 2 wins!')
        army_2.insert(0,"K")
        if money_1 >1:
            army_1.append('A')
            money_1 -=1
#Player 1 extended armies
    elif (unit_1 == 'SE' and unit_2 == 'A'):               
        print('Player 1 Wins!')
        army_1.insert(0,"SE")
        if money_2 >1:
            army_2.append('A')
            money_2 -=1
    elif (unit_1 == 'SE' and unit_2 == 'S'):               
        print('Player 1 Wins!')
        army_1.insert(0,"SE")
        if money_2 >1:
            army_2.append('S')
            money_2 -=1
    elif (unit_1 == 'W' and unit_2 == 'S'):
        print('Player 1 Wins!')
        army_1.insert(0,'W')
        if money_2 >1:
            army_2.append('S')
            money_2 -=1
    elif (unit_1 == 'W' and unit_2 == 'K'):
        print('Player 1 Wins!')
        army_1.insert(0,'W')
        if money_2 >1:
            army_2.append('K')
            money_2 -=1 
    elif (unit_1 == 'W' and unit_2 == 'SE'):
        print('Player 1 Wins!')
        army_1.insert(0,'W')
        if money_2 >1:
            army_2.append('SE')
            money_2 -=1
    elif (unit_1 == 'SE' and unit_2 == 'K'):
        print('Player 2 wins!')
        army_2.insert(0,'K')
        if money_1 >1:
            army_1.append('SE')
            money_1 -=1
    elif (unit_1 == 'SE' and unit_2 == 'W'):
        print('Player 2 wins!')
        army_2.insert(0,'W')
        if money_1 >1:
            army_1.append('SE')
            money_1 -=1
    elif (unit_1 == 'W' and unit_2 == 'A'):
        print('Player 2 wins!')
        army_2.insert(0,'A')
        if money_1 >1:
            army_1.append('W')
            money_1 -=1
#Player 2 extended armies
    elif (unit_2 == 'SE' and unit_1 == 'A'):               
        print('Player 2 wins!')
        army_2.insert(0,'SE')
        if money_1 >1:
            army_1.append('A')
            money_1 -=1
    elif (unit_2 == 'SE' and unit_1 == 'S'):               
        print('Player 2 wins!')
        army_2.insert(0,'SE')
        if money_1 >1:
            army_1.append('S')
            money_1 -=1
    elif (unit_2 == 'W' and unit_1 == 'SE'):
        print('Player 2 wins!')
        army_2.insert(0,'W')
        if money_1 >1:
            army_1.append('SE')
            money_1 -=1
    elif (unit_2 == 'W' and unit_1 == 'K'):
        print('Player 2 wins!')
        army_2.insert(0,'W')
        if money_1 >1:
            army_1.append('K')
            money_1 -=1
    elif (unit_2 == 'W' and unit_1 == 'S'):
        print('Player 2 wins!')
        army_2.insert(0,'W')
        if money_1 >1:
            army_1.append('S')
            money_1 -=1
    elif (unit_2 == 'W' and unit_1 == 'A'):
        print('Player 1 Wins!')
        army_1.insert(0,'A')
        if money_2 >1:
            army_2.append('W')
            money_2 -=1
    elif (unit_2 == 'SE' and unit_1 == 'K'):
        print('Player 1 Wins!')
        army_1.insert(0,'K')
        if money_2 >1:
            army_2.append('SE')
            money_2 -=1
    elif (unit_2 == 'SE' and unit_1 == 'W'):
        print('Player 1 Wins!')
        army_1.insert(0,'W')
        if money_2 >1:
            army_2.append('SE')
            money_2 -=1


print('\nThanks for playing! Have a good day.')

