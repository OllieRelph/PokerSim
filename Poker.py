import random
#set global variables
player1cards = []
player2cards = []
tablecards = []
player1values = [] #2-ace
player2values = [] # 2-ace
player1rawvalues = [] #2-14
player2rawvalues = [] # 2-14
tablevalues = []
tablecardsrawvalues = []
player1suits = []
player2suits = []
tablesuits = []
winning_index = 0
highcardrule = False

pair = []
twopair = []
threeOAK = []
quads = []
flush = []
straight = []
fullhouse = []
straightflush = []
royalflush = []


# multiple hot style approach, 0 becomes 1 if the conditions is met in rank order
#index 0 indicates whwther the player has the higher card
#index 1 indicated whether a pair condition has been met
#index 2 is a 2 pair
#index 3 is a three of a kind
#index 4 is a Straight
#index 5 is a Flush
#index 6 is a full house
#index 7 is a Four of a kind
#index 8 is a Straight Flush
#Index 9 is a Royal Flush
player1conditions = [0,0,0,0,0,0,0,0,0,0]
player2conditions = [0,0,0,0,0,0,0,0,0,0]
def add_card(player,value,suit):
    temp = ""
    #suit is 1-4 inclusive diamonds,hearts,clubs,spades
    #value is 2-14 inclusive
    if type(value) != int:
        print("invalid type of value")
        return 0

    if type(suit) != int:
        print("Invalid type of suit")
        return 0

    if value < 2 or value > 14:
        print("invalid range of value, please enter 2-14 inclusive")
        return 0

    if value < 2 or value > 14:
        print("invalid range of suit, please enter 1-4 inclusive")
        return 0
    if value < 11:
        temp = temp + str(value)
    elif value == 11:
        temp = temp + "Jack"
    elif value == 12:
        temp = temp + "Queen"
    elif value == 13:
        temp = temp + "King"
    elif value == 14:
        temp = temp + "Ace"


    if suit == 1:
        temp = temp + " Diamonds"
    elif suit == 2:
        temp = temp + " Hearts"
    elif suit == 3:
        temp = temp + " Clubs"
    elif suit == 4:
        temp = temp + " Spades"
    #check for duplicates
    if temp in player1cards or temp in player2cards or temp in tablecards:
        add_card(player,random_value(),random_suit())
    else:
        if player == 1:
            player1cards.append(temp)
            player1values.append(temp.split(' ')[0])
            player1rawvalues.append(value)
            player1suits.append(temp.split(' ')[1])
        elif player == 2:
            player2cards.append(temp)
            player2values.append(temp.split(' ')[0])
            player2rawvalues.append(value)
            player2suits.append(temp.split(' ')[1])
        elif player == 3:
            tablecards.append(temp)
            tablevalues.append(temp.split(' ')[0])
            tablecardsrawvalues.append(value)
            tablesuits.append(temp.split(' ')[1])



def random_value():
    return random.randint(2,14)


def random_suit():
    return random.randint(1,4)

def flop():
    add_card(3,random_value(), random_suit())
    add_card(3,random_value(), random_suit())
    add_card(3,random_value(), random_suit())

def turnorriver():
    add_card(3,random_value(), random_suit())

def remove_value_from_list(thelist,value):
    return [val for val in thelist if val != value]

def combine_values(player):
    #check validity
    if type(player) != int:
        print("Invalid type of \'Player\'")
        return []

    if player != 1 and player !=2:
        print("Invalid value of \'Player\'")
        return []
    #combines the player value passeds values with the tables
    if player == 1:
        return player1values + tablevalues

    if player == 2:
        return player2values + tablevalues

def combine_suits(player):
    #check validity
    if type(player) != int:
        print("Invalid type of \'Player\'")
        return []

    if player != 1 and player !=2:
        print("Invalid value of \'Player\'")
        return []
    #combines the player value passeds values with the tables
    if player == 1:
        return player1suits + tablesuits

    if player == 2:
        return player2suits + tablesuits

def check_flush():
    returnarray = [0,0]
    setP1 = combine_suits(1)
    setP2 = combine_suits(2)

    for suit in setP1:
        if setP1.count(suit) >= 5:
            returnarray[0] = 1

    for suit in setP2:
        if setP2.count(suit) >= 5:
            returnarray[1] = 1

    return returnarray

def check_straight():
    returnarray = [0,0]
    setP1 = player1rawvalues + tablecardsrawvalues
    setP2 = player2rawvalues + tablecardsrawvalues

    for value in range(4,13):
        if value-2 in setP1 and value-1 in setP1 and value in setP1 and value+1 in setP1 and value+2 in setP1:
            returnarray[0] = 1
        if value-2 in setP2 and value-1 in setP2 and value in setP2 and value+1 in setP2 and value+2 in setP2:
            returnarray[1] = 1

    return returnarray

def check_set(amount):

    returnarray = [0,0]
    setP1 = []
    setP2 = []
    #combine the hands of player 1 and the table
    setP1 = combine_values(1)
    setP2 = combine_values(2)


    for value in setP1:
        if setP1.count(value) >= amount:
            returnarray[0] = 1

    for value in setP2:
        if setP2.count(value) >= amount:
            returnarray[1] = 1
    return returnarray


def check_highcard():
    if max(player1rawvalues) > max(player2rawvalues):
        player1conditions[0] = 1
    elif max(player1rawvalues) < max(player2rawvalues):
        player2conditions[0] = 1
    else:
        player1conditions[0] = 1
        player2conditions[0] = 1

def check_twopair():
    returnarray = [0,0]
    setP1 = combine_values(1)
    setP2 = combine_values(2)
    temp_list = []
    #initially check for a pair, if found we remove it
    #from a temporary list and check for a 2nd pair in the reduced list
    for value in setP1:

        if setP1.count(value) >=2:
            temp_list = remove_value_from_list(setP1, value)

            for value2 in temp_list:
                if temp_list.count(value2) >=2:
                    returnarray[0] = 1

    for value in setP2:

        if setP2.count(value) >=2:
            temp_list = remove_value_from_list(setP2, value)
            for value2 in temp_list:
                if temp_list.count(value2) >=2:
                    returnarray[1] = 1


    return returnarray

def check_fullhouse():
    returnarray = [0,0]
    setP1 = combine_values(1)
    setP2 = combine_values(2)
    temp_list = []
    #initially check for a three of a kind, if found we remove it
    #from a temporary list and check for a pair in the reduced list
    for value in setP1:

        if setP1.count(value) >=3:
            temp_list = remove_value_from_list(setP1, value)

            for value2 in temp_list:
                if temp_list.count(value2) >=2:
                    returnarray[0] = 1

    for value in setP2:

        if setP2.count(value) >=3:
            temp_list = remove_value_from_list(setP2, value)
            for value2 in temp_list:
                if temp_list.count(value2) >=2:
                    returnarray[1] = 1


    return returnarray

def check_straightflush():
    returnarray = [0,0]
    #check for a flush, any cards in the flush we put in temp
    #we check temp for a straight
    templist = []
    hitsuit = ""
    setP1suits = combine_suits(1)
    setP2suits = combine_suits(2)
    setP1rawvalues = player1rawvalues + tablecardsrawvalues
    setP2rawvalues = player2rawvalues + tablecardsrawvalues

    for suit in setP1suits:
        if setP1suits.count(suit) >= 5:
            hitsuit = suit
            #print(hitsuit)
            #at this point we know there is a flush of some suit
            #check which indexes that suit occurs at
            for x in range(0,len(setP1suits)):
                if setP1suits[x] == hitsuit:
                    templist.append(setP1rawvalues[x])

            #check templist for a straight
            for value in range(4,13):
                if value-2 in templist and value-1 in templist and value in templist and value+1 in templist and value+2 in templist:
                    returnarray[0] = 1
    templist = []
    for suit in setP2suits:
        if setP2suits.count(suit) >= 5:
            hitsuit = suit
            #at this point we know there is a flush of some suit
            #check which indexes that suit occurs at
            for x in range(0,len(setP2suits)):
                if setP2suits[x] == hitsuit:
                    templist.append(setP2rawvalues[x])

            #check templist for a straight
            for value in range(4,13):
                if value-2 in templist and value-1 in templist and value in templist and value+1 in templist and value+2 in templist:
                    returnarray[1] = 1


    return returnarray

def check_royalflush():
    returnarray = [0,0]
    setP1 = player1cards + tablecards
    setP2 = player2cards + tablecards


    if '10 Diamonds' in setP1 and 'Jack Diamonds' in setP1 and 'Queen Diamonds' in setP1 and 'King Diamonds' in setP1 and 'Ace Diamonds' in setP1:
        returnarray[0] = 1
    if '10 Hearts' in setP1 and 'Jack Hearts' in setP1 and 'Queen Hearts' in setP1 and 'King Hearts' in setP1 and 'Ace Hearts' in setP1:
        returnarray[0] = 1
    if '10 Clubs' in setP1 and 'Jack Clubs' in setP1 and 'Queen Clubs' in setP1 and 'King Clubs' in setP1 and 'Ace Clubs' in setP1:
        returnarray[0] = 1
    if '10 Spades' in setP1 and 'Jack Spades' in setP1 and 'Queen Spades' in setP1 and 'King Spades' in setP1 and 'Ace Spades' in setP1:
        returnarray[0] = 1


    if '10 Diamonds' in setP2 and 'Jack Diamonds' in setP2 and 'Queen Diamonds' in setP2 and 'King Diamonds' in setP2 and 'Ace Diamonds' in setP2:
        returnarray[1] = 1
    if '10 Hearts' in setP2 and 'Jack Hearts' in setP2 and 'Queen Hearts' in setP2 and 'King Hearts' in setP2 and 'Ace Hearts' in setP2:
        returnarray[1] = 1
    if '10 Clubs' in setP2 and 'Jack Clubs' in setP2 and 'Queen Clubs' in setP2 and 'King Clubs' in setP2 and 'Ace Clubs' in setP2:
        returnarray[1] = 1
    if '10 Spades' in setP2 and 'Jack Spades' in setP2 and 'Queen Spades' in setP2 and 'King Spades' in setP2 and 'Ace Spades' in setP2:
        returnarray[1] = 1



    return returnarray
'''
#manual card setup

add_card(1,2,1)   #2 diamonds
add_card(1,3,1)   #3 diamonds

add_card(2,14,3)   #ace clubs
add_card(2,14,4)   #ace spades

add_card(3,4,1)   #4 diamonds
add_card(3,5,1)   #5 diamonds
add_card(3,14,2)   #ace hearts

add_card(3,6,1)   #6 diamonds
add_card(3,2,3)   #2 clubs


'''
#Initialise 2 cards for each player
add_card(1,random_value(), random_suit())
add_card(1,random_value(), random_suit())

add_card(2,random_value(), random_suit())
add_card(2,random_value(), random_suit())


flop()
turnorriver()
turnorriver()

print(player1cards)
print(player2cards)
print(tablecards)

check_highcard()
pair = check_set(2)
twopair = check_twopair()
threeOAK = check_set(3)
quads = check_set(4)
flush = check_flush()
straight = check_straight()
fullhouse = check_fullhouse()
straightflush = check_straightflush()
royalflush = check_royalflush()


if pair[0]:
    player1conditions[1] = 1
if pair[1]:
    player2conditions[1] = 1

if threeOAK[0]:
    player1conditions[3] = 1
if threeOAK[1]:
    player2conditions[3] = 1

if quads[0]:
    player1conditions[7] = 1
if quads[1]:
    player2conditions[7] = 1

if flush[0]:
    player1conditions[5] = 1
if flush[1]:
    player2conditions[5] = 1

if straight[0]:
    player1conditions[4] = 1
if straight[1]:
    player2conditions[4] = 1

if twopair[0]:
    player1conditions[2] = 1
if twopair[1]:
    player2conditions[2] = 1

if fullhouse[0]:
    player1conditions[6] = 1
if fullhouse[1]:
    player2conditions[6] = 1

if straightflush[0]:
    player1conditions[8] = 1
if straightflush[1]:
    player2conditions[8] = 1

if royalflush[0]:
    player1conditions[9] = 1
if royalflush[1]:
    player2conditions[9] = 1



def calc_winner():
    start_index = 9
    global winning_index
    global highcardrule
    while start_index >= 0:
        if player1conditions[start_index] == 1 and player2conditions[start_index] == 0:
            winning_index = start_index
            return 1
        if player1conditions[start_index] == 0 and player2conditions[start_index] == 1:
            winning_index = start_index
            return 2
        if player1conditions[start_index] == 1 and player2conditions[start_index] == 1:
            #assume that if both players have the same rank we go to high card
            winning_index = start_index
            highcardrule = True
            if player1conditions[0] == 1 and player2conditions[0] == 0:
                return 1
            elif player2conditions[0] == 1 and player1conditions[0] == 0:
                return 2
            else:
                return 3
        else:
            start_index -=1


def disp_method():
    if winning_index == 0:
        return "High Card"
    elif winning_index == 1:
        return "Pair"
    elif winning_index == 2:
        return "Two Pair"
    elif winning_index == 3:
        return "Three of a Kind"
    elif winning_index == 4:
        return "Straight"
    elif winning_index == 5:
        return "Flush"
    elif winning_index == 6:
        return "Full House"
    elif winning_index == 7:
        return "Four of a Kind"
    elif winning_index == 8:
        return "Straight Flush"
    elif winning_index == 9:
        return "Royal Flush"
#print(player1conditions)
#print(player2conditions)

winner = calc_winner()

method = disp_method()

if winner == 1:
    print("Player 1 Wins with a " + method)
elif winner == 2:
    print("Player 2 Wins with a " + method)
elif winner == 3:
    print("Its a draw with both players having a " + method)

if highcardrule == True:
    print("and the High Card")

input("press close to exit")















