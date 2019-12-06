import random
import os
import re
import collections
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

# GAME LOGIC
darklordDeck = []
blueeyesDeck = []
playerDeck=[]
aiDeck=[]
playerHand = []
aiHand = []
playerField = []
aiField = []
playerGrave = []
aiGrave = []
cardPlayed = []
dataList = []
resultList = []
threatList = 9999
predictDeck = ""
playStyle = ""
dataInput = {}
sum = 0
battle = 0
end = 0
stop = 0
spell = 0
numSum = 0
numMon = 0
maxAtk = 0
minAtk = 0
maxDef = 0
aiSum = 0
aiTribute = 0
aiSpell = 0
aiBattle = 0
aiEnd = 0
playerLife = 4000
aiLife = 4000
toSummon = ""
toTribute = ""
toActivate = ""
toPosition = ""
Attack = ""
toAttack = ""
aiChoice = ""

class Card(object):
    def __init__(self, name=None, type=None, archetype=None, effect=None, attack=None, defense=None, level=None, position=None):
        self.name = name
        self.type = type
        self.archetype = archetype
        self.effect = effect
        self.attack = attack
        self.defense = defense
        self.level = level
        self.position = position

def CreateDecks():
    darklordDeck.append(Card("Nasten", "monster", "DarkLord", None, 2600, 2600, 8, None))
    darklordDeck.append(Card("Nasten", "monster", "DarkLord", None, 2600, 2600, 8, None))
    darklordDeck.append(Card("Nasten", "monster", "DarkLord", None, 2600, 2600, 8, None))
    darklordDeck.append(Card("Desire", "monster", "DarkLord", None, 3000, 2000, 10, None))
    darklordDeck.append(Card("MorningStar", "monster", "DarkLord", None, 3100, 2800, 11, None))
    darklordDeck.append(Card("Superbia", "monster", "DarkLord", None, 2300, 2900, 8, None))
    darklordDeck.append(Card("Superbia", "monster", "DarkLord", None, 2300, 2900, 8, None))
    darklordDeck.append(Card("Superbia", "monster", "DarkLord", None, 2300, 2900, 8, None))
    darklordDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    darklordDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    darklordDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    darklordDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    darklordDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    darklordDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    darklordDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    darklordDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    darklordDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    darklordDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    darklordDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    darklordDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    #darklordDeck.append(Card("Reborn", "spell", "Monster", "Summon 1 Monster from Grave", None, None, None, None))
    #darklordDeck.append(Card("Reborn", "spell", "Monster", "Summon 1 Monster from Grave", None, None, None, None))
    #darklordDeck.append(Card("Reborn", "spell", "Monster", "Summon 1 Monster from Grave", None, None, None, None))
    #darklordDeck.append(Card("Offering", "spell", "Monster", "Destroy 1 Monster", None, None, None, None))
    #darklordDeck.append(Card("Offering", "spell", "Monster", "Destroy 1 Monster", None, None, None, None))
    #darklordDeck.append(Card("Offering", "spell", "Monster", "Destroy 1 Monster", None, None, None, None))
    #darklordDeck.append(Card("Power", "spell", "Monster", "Increase 1 Monster Attack by 500", None, None, None, None))
    #darklordDeck.append(Card("Power", "spell", "Monster", "Increase 1 Monster Attack by 500", None, None, None, None))
    #darklordDeck.append(Card("Power", "spell", "Monster", "Increase 1 Monster Attack by 500", None, None, None, None))

    blueeyesDeck.append(Card("White Dragon", "monster", "Blue-Eyes", None, 3000, 2500, 10, None))
    blueeyesDeck.append(Card("White Dragon", "monster", "Blue-Eyes", None, 3000, 2500, 10, None))
    blueeyesDeck.append(Card("White Dragon", "monster", "Blue-Eyes", None, 3000, 2500, 10, None))
    blueeyesDeck.append(Card("Spirit Dragon", "monster", "Blue-Eyes", None, 2500, 2000, 8, None))
    blueeyesDeck.append(Card("Spirit Dragon", "monster", "Blue-Eyes", None, 2500, 2000, 8, None))
    blueeyesDeck.append(Card("Spirit Dragon", "monster", "Blue-Eyes", None, 2500, 2000, 8, None))
    blueeyesDeck.append(Card("Cosmos", "monster", "Blue-Eyes", None, 3100, 1800, 11, None))
    blueeyesDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    blueeyesDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    blueeyesDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    blueeyesDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    blueeyesDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    blueeyesDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    blueeyesDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    blueeyesDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    blueeyesDeck.append(Card("Hunter", "monster", "Monster", None, 1500, 600, 4, None))
    blueeyesDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    blueeyesDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    blueeyesDeck.append(Card("Defender", "monster", "Monster", None, 1300, 1900, 4, None))
    #blueeyesDeck.append(Card("Reborn", "spell", "Monster", "Summon 1 Monster from Grave", None, None, None, None))
    #blueeyesDeck.append(Card("Reborn", "spell", "Monster", "Summon 1 Monster from Grave", None, None, None, None))
    #blueeyesDeck.append(Card("Reborn", "spell", "Monster", "Summon 1 Monster from Grave", None, None, None, None))
    #blueeyesDeck.append(Card("Offering", "spell", "Monster", "Destroy 1 Monster", None, None, None, None))
    #blueeyesDeck.append(Card("Offering", "spell", "Monster", "Destroy 1 Monster", None, None, None, None))
    #blueeyesDeck.append(Card("Offering", "spell", "Monster", "Destroy 1 Monster", None, None, None, None))
    #blueeyesDeck.append(Card("Power", "spell", "Monster", "Increase 1 Monster Attack by 500", None, None, None, None))
    #blueeyesDeck.append(Card("Power", "spell", "Monster", "Increase 1 Monster Attack by 500", None, None, None, None))
    #blueeyesDeck.append(Card("Power", "spell", "Monster", "Increase 1 Monster Attack by 500", None, None, None, None))



def Draw(times, deck, hand):
    i = 0
    while(i < times):
        draw = random.randint(0,len(deck) -1)
        hand.append(deck[draw])
        deck.pop(draw)
        i = i + 1

def MainPhase(playerHand,playerField,playerGrave,aiHand,aiField,aiGrave,turn):
    global aiEnd
    choice = ""
    actions = {"summon" : normalSummon,
               "tribute" : tributeSummon,
               "battle"  :BattlePhase,
               "end" : endTurn,
               "stop": stopGame,
               "effect" : checkEffect,
               "spell" : activateSpell,
               "hand" : checkHand,
               "field": checkField,
               "grave" : checkGrave}
    
    if (turn == "Player"):
        checkHand(playerHand,playerField,playerGrave,turn)
    if (turn == "AI"):
        checkHand(aiHand,aiField,aiGrave,turn)
        actionMaking(aiHand,aiGrave,aiField,"AI")
        DecisionTreeBattle(playStyle,threatList)
    while(end != 1):
        if (turn == "Player"):
            choice = input("Enter an action: ")
            for act in actions:
                if (choice == act):
                    if (choice == "battle"):
                        actions[choice](playerField,playerGrave,aiField,aiGrave,turn)
                    elif (choice == "spell"):
                        actions[choice](playerHand,playerField,playerGrave,aiHand,aiField,aiGrave,turn)
                    else:
                        actions[choice](playerHand,playerField,playerGrave,turn)
        if (turn == "AI"):
            if (aiChoice == "tribute"):
                choice = "tribute"
            elif(aiChoice == "summon"):
                choice = "summon"
            elif (aiBattle == 1):
                choice = "battle"
                DecisionTreeBattle(playStyle,threatList)
            elif(aiTribute == 0 and aiSum == 0 and aiBattle == 0):
                aiEnd = 1
            if (aiEnd == 1):
                choice = "end"
            if (choice == "battle"):
                actions[choice](aiField,aiGrave,playerField,playerGrave,turn)
            elif (choice == "spell"):
                actions[choice](aiHand,aiField,aiGrave,playerHand,playerField,playerGrave,turn)
            else:
                actions[choice](aiHand,aiField,aiGrave,turn)

def BattlePhase(attackField,attackGrave,defenseField,defenseGrave, turn):
    global playerLife, aiLife
    attack = ""
    defense = ""
    target = 0
    canAttack = 0
    global battle, aiBattle
    for card in attackField:
        if(card.position == "attack"):
            if (battle == 0):
                print(card.name + " can attack")
                canAttack = canAttack + 1
    if(canAttack > 0 and battle == 0):
        if(turn == "Player"):
            attack = input("Chose attack card: ")
        else:
            attack = Attack
        print("Available Target: ")
        for card in defenseField:
            print(card.name)
            target = target + 1
        if(target > 0):
            if (turn == "Player"):
                defense = input("Chose target card: ")
            else:
                defense = toAttack
            for attackcard in attackField:
                 if (attack.lower() == attackcard.name.lower()):
                     for defensecard in defenseField:
                         if (defense.lower() == defensecard.name.lower()):
                             if(defensecard.position == "attack"):
                                 if(attackcard.attack > defensecard.attack):
                                     print(attackcard.name + " has attacked and destroyed " + defensecard.name + " by battle")
                                     defenseGrave.append(defensecard)
                                     defenseField.remove(defensecard)
                                     if(turn == "Player"):
                                         aiLife = aiLife - (attackcard.attack - defensecard.attack)
                                         print("AI takes",(attackcard.attack - defensecard.attack),"to their LifePoint")
                                     else:
                                         playerLife = playerLife - (attackcard.attack - defensecard.attack)
                                         print("Player takes",(attackcard.attack - defensecard.attack),"to their LifePoint")
                                     checkWin()
                                     battle = 1
                                     aiBattle = 0
                                     break
                                 if(attackcard.attack == defensecard.attack):
                                     print(attackcard.name+ " and " + defensecard.name + " have detroyed eachother by battle")
                                     attackGrave.append(attackcard)
                                     attackField.remove(attackcard)
                                     defenseGrave.append(defensecard)
                                     defenseField.remove(defensecard)
                                     checkWin()
                                     battle = 1
                                     aiBattle = 0
                                     break
                                 if(attackcard.attack < defensecard.attack):
                                     print(attackcard.name + " has attacked " + defensecard.name + " and has been destroyed by battle")
                                     attackGrave.append(attackcard)
                                     attackField.remove(attackcard)
                                     if(turn == "Player"):
                                         playerLife = playerLife - (-attackcard.attack + defensecard.attack)
                                     else:
                                         aiLife = aiLife - (-attackcard.attack + defensecard.attack)
                                     battle = 1
                                     aiBattle = 0
                                     print(turn + " takes",(-attackcard.attack + defensecard.attack),"to their LifePoint")
                                     checkWin()
                                     break
                             if(defensecard.position == "defense"):
                                 if(attackcard.attack > defensecard.defense):
                                     print(attackcard.name + " has attacked and destroyed " + defensecard.name + " by battle")
                                     defenseGrave.append(defensecard)
                                     defenseField.remove(defensecard)
                                     battle = 1
                                     aiBattle = 0
                                     checkWin()
                                     break
                                 if(attackcard.attack == defensecard.attack):
                                     print(attackcard.name + " and " + defensecard.name + " battle but nothing happens")
                                     battle = 1
                                     aiBattle = 0
                                     checkWin()
                                     break
                                 if(attackcard.attack < defensecard.attack):
                                     print(attackcard.name + " has attacked " + defensecard.name + " and recieve recoil damage")
                                     if(turn == "Player"):
                                         playerLife = playerLife - (-attackcard.attack + defensecard.defense)
                                     else:
                                         aiLife = aiLife - (-attackcard.attack + defensecard.defense)
                                     print(turn + " takes",(-attackcard.attack + defensecard.defense),"to their LifePoint")
                                     aiBattle = 0
                                     battle = 1
                                     checkWin()
                                     break
        else:
            for attacker in attackField:
                if (attack.lower() == attacker.name.lower()):
                    if(turn == "Player"):
                        aiLife = aiLife - attacker.attack
                    else:
                        playerLife = playerLife - attacker.attack
                    print("None")
                    print(attack + " attacks directly for", attacker.attack,"damage")
                    aiBattle = 0
                    battle = 1
                    break
    else:
        print("Cannot conduct any attack")
        aiBattle = 0

def normalSummon(hand, field, grave, turn):
    global numSum
    global aiSum
    global aiChoice
    summon = ""
    position = ""
    global sum
    i = 0;
    for checkcard in hand:
        if (isinstance(checkcard.level, int) and checkcard.level < 9 and sum == 0):
            print("Can Summon " + checkcard.name)
            i = i + 1
    if (sum == 1 or i == 0):
        print("No Normal Summon can be performed")
        aiSum = 0
        aiChoice = ""
    else:
        if (turn == "Player"):
            summon = input("Chose card to Summon: ")
        else:
            summon = toSummon
        for summoncard in hand:
            if (isinstance(summoncard.level, int) and summoncard.level < 9 and sum == 0):
                if (summon.lower() == summoncard.name.lower()):
                    if (turn == "Player"):
                        position = input("Chose summoned card position(attack or defense): ")
                    else:
                        position = toPosition
                    summoncard.position = position
                    field.append(summoncard)
                    hand.remove(summoncard)
                    if(turn == "Player"):
                        cardPlayed.append(summoncard)
                        numSum = numSum + 1
                    print("Normal Summon " + summoncard.archetype + " " + summoncard.name + " in " + summoncard.position + " position")
                    sum = 1
                    break

def activateSpell(ownHand,ownField,ownGrave,oppHand,oppField,oppGrave,turn):
    global spell
    global aiSpell
    i = 0
    activate = ""
    for card in ownHand:
        if (card.effect != None and spell == 0):
            print(card.name + " can be activate")
            i = i + 1
    if (spell == 0 and i > 0):
        if (turn == "Player"):
            activate = input("Chose spell to activate: ")
        else:
            activate = toActivate
        for spellcard in ownHand:
            if (spellcard.effect != None):
                if (activate.lower() == spellcard.name.lower()):
                    print("Activate " + spellcard.name)
                    if (spell == 0):
                        for match in re.finditer("Summon",spellcard.effect, re.IGNORECASE):
                            print("Summon from Grave")
                            ownGrave.append(spellcard)
                            ownHand.remove(spellcard)
                            if(turn == "Player"):
                                cardPlayed.append(spellcard)
                            spell = 1
                            break
                    if (spell == 0):
                        for match in re.finditer("Increase",spellcard.effect,re.IGNORECASE):
                            print("Increase Damage")
                            ownGrave.append(spellcard)
                            ownHand.remove(spellcard)
                            if(turn == "Player"):
                                cardPlayed.append(spellcard)
                            spell = 1
                            break
                    if (spell == 0):
                        for match in re.finditer("Destroy",spellcard.effect,re.IGNORECASE):
                            print("Destroy a Monster")
                            ownGrave.append(spellcard)
                            ownHand.remove(spellcard)
                            if(turn == "Player"):
                                cardPlayed.append(spellcard)
                            spell = 1
                            break
    else:
        print("No spell can be activated")
        aiSpell = 0
    


def tributeSummon(hand, field, grave, turn):
    global numSum
    global aiTribute
    global aiChoice
    summon = ""
    position = ""
    tribute = ""
    global sum
    i = 0;
    control = 0
    for fieldcard in field:
        control = control + 1
    for checkcard in hand:        
        if (isinstance(checkcard.level, int) and checkcard.level > 9 and sum == 0 and control > 0):
            print("Can Summon " + checkcard.name)
            i = i + 1
    if (sum == 1 or i == 0):
        print("No Tribute Summon can be performed")
        aiTribute = 0
        aiChoice = ""
    else:
        if (turn == "Player"):
            summon = input("Chose card to Summon: ")
        else:
            summon = toSummon
        for summoncard in hand:
            if (isinstance(summoncard.level, int) and summoncard.level > 9 and sum == 0 and control > 0):
                if (summon.lower() == summoncard.name.lower()):
                    for tributecard in field:
                        print(tributecard.name + " can be tribute")
                    if (turn == "Player"):
                        tribute = input("Chose card to tribute: ")
                    else:
                        tribute = toTribute
                    for tributecard in field:
                        if (tribute.lower() == tributecard.name.lower()):
                            field.remove(tributecard)
                            grave.append(tributecard)
                            break
                    if (turn == "Player"):
                        position = input("Chose summoned card position(attack or defense): ")
                    else:
                        position = toPosition
                    summoncard.position = position
                    field.append(summoncard)
                    hand.remove(summoncard)
                    if(turn == "Player"):
                        cardPlayed.append(summoncard)
                        numSum = numSum + 1
                    print("Normal Summon " + summoncard.archetype + " " + summoncard.name + " in " + summoncard.position + " position")
                    sum = 1
                    break
                else:
                    print("Card cannot be normal summon or name is incorrect")
                    print(toSummon)
                    break
def newTurn(playerHand,playerField,playerGrave,aiHand,aiField,aiGrave,turn):
    global aiSum
    global aiTribute
    global aiSpell
    global aiEnd
    global aiBattle
    global Attack
    global toAttack
    global maxAtk
    global minAtk
    global maxDef
    global toSummon
    global toTribute
    global toActivate
    global toPosition
    global sum
    global end
    global spell
    global battle
    global aiChoice
    sum = 0
    end = 0
    spell = 0
    if(stop != 1):
        battle = 0
    aiSum = 0
    aiSpell = 0
    aiTribute = 0
    aiBattle = 0
    aiEnd = 0
    maxAtk = 0
    minAtk = 0
    maxDef = 0
    toSummon = ""
    toTribute = ""
    toActivate = ""
    toPosition = ""
    Attack = ""
    toAttack = ""
    aiChoice = ""
    if(turn == "Player"):
        print("Player Life Points:",playerLife)
    else:
        print("AI Life Points:",aiLife)
    MainPhase(playerHand,playerField,playerGrave,aiHand,aiField,aiGrave,turn)

def checkHand(hand, field, grave, turn):
    for card in hand:
        if (card.type == "monster"):
            print(card.archetype + " " + card.name + "(",card.attack,"/",card.defense,")")
        if (card.type == "spell"):
            print(card.archetype + " " + card.name + "( "+card.type+" )")

def checkField(hand, field, grave, turn):
    global numMon
    global maxAtk
    if (turn == "Player"):
        print("Player Side: ")
        for card in playerField:
            if (card.position == "attack"):
                print(card.archetype + " " + card.name + " Attack:",card.attack)
            if (card.position == "defense"):
                print(card.archetype + " " + card.name + " Defense:",card.defense)
        print("AI Side: ")
        for card in aiField:
            if (card.position == "attack"):
                print(card.archetype + " " + card.name + " Attack:",card.attack)
            if (card.position == "defense"):
                print(card.archetype + " " + card.name + " Defense:",card.defense)
    else:
        numMon = 0
        maxAtk = 0
        for card in playerField:
            numMon = numMon + 1
            if maxAtk < card.attack:
                maxAtk = card.attack


def checkGrave(hand, field, grave, turn):
    print("Player Graveyard: ")
    for card in playerGrave:
        if (card.type == "monster"):
            print(card.archetype + " " + card.name + "(",card.attack,"/",card.defense,")")
        if (card.type == "spell"):
            print(card.archetype + " " + card.name + "( "+card.type+" )")
    print("AI Graveyard: ")
    for card in aiGrave:
        if (card.type == "monster"):
            print(card.archetype + " " + card.name + "(",card.attack,"/",card.defense,")")
        if (card.type == "spell"):
            print(card.archetype + " " + card.name + "( "+card.type+" )")

def checkEffect(hand, field, grave, turn):
    i = 0
    for card in playerHand:
        if (card.effect != None):
            print(card.name + " effect: " + card.effect)
            i = i + 1
def endTurn(hand, field, grave, turn):
    global end
    if(turn == "Player"):
        end = 1
    else:
        input("Press Enter to continue...")
        end = 1
    os.system("cls")

def stopGame(hand, field, grave, turn):
    global stop
    stop = -1
    endTurn(hand,field,grave,turn)



# AI LOGIC LEARNING

#Player's Deck Prediction using NGRAMS

def deckPrediction(deckList):
    #initialize variables
    probList = []
    matchList = []
    prob = 0
    match = 0
    deckName = []
    name = ""
    for deck in deckList:                           #loop to go through all the prebuilt decks
        for cardplayed in cardPlayed:               #loop to go through all the cards that the players played
            for card in deck:                       #if cards that player played exist in one of prebuilt deck, 
                if (card.archetype != "Monster"):   #the chance of that one exact prebuilt is using by the Player is higher
                    name = card.archetype
                if (cardplayed.archetype == card.archetype and cardplayed.archetype != "Monster"):
                    match = match + 2
                    matchList.append(match)
                elif (cardplayed.name == card.name):
                    match = match + 1
                    matchList.append(match)
        prob = match / 20                          #calculate the probability of guessing the deck that the player is using
        probList.append(prob)
        deckName.append(name)
        match = 0
        prob = 0
    predictDeck = deckName[probList.index(max(probList))]     #output prediction
    if (0.4 <= max(probList) < 0.6):
        print("Player might be using " + predictDeck)     
    elif (0.6 <= max(probList) < 1):
        print("Player is probably using "+ predictDeck)
    elif (max(probList) >= 1):
        print("Player is using "+ predictDeck)
    else:
        print("Doesnt have enough data to predict")
 
def createData(deckName, summon, onField, maxAtk):
    global dataInput                            #function to create a dataframe for all input needed
    deckno = 0
    if (deckName == "DarkLord"):
        deckno = 0
    elif (deckName == "Blue-Eyes"):
        deckno = 1                              #convert the predicted input from ngrams learning to integer to train
    dataInput = pd.DataFrame({'Deck Used' : deckno, 
                      'Number of Summons' : summon, 
                      'Number of Opponent Monsters on Field' : onField, 
                      'Highest Opponent Monster Attack' : maxAtk}, index=[0])

def playStyleLearning(input):
    global playStyle                            #this function will take input from the game, 
    data = pd.read_csv("playstyle.csv")         #load the training data from csv file and predict the result for the input
    dataList = data[['Deck Used', 'Number of Summons', 'Number of Opponent Monsters on Field', 'Highest Opponent Monster Attack']]
    resultList = data['Play Style']
    classifierTree = DecisionTreeClassifier(criterion ='entropy', random_state = 100)   
    classifierTree = classifierTree.fit(dataList,resultList)      #using decision tree classifier to train the model to predict
    prediction = classifierTree.predict(input)      
    if (prediction == 1):                                         #output the predicted playstyle to help in decision making process
        playStyle = "Aggressive"
        print("Player Field is weak, time to play Aggressive!")
    else:                                                                               
        playStyle = "Passive"
        print("Player Field is strong, time to play Passive!")

#learning potential threat the opponent might have
def BayesianLearning(playStyle):                #this function will go through what the AI have on the field
    global maxAtk                               #then figure out what are the potential threats that the Player can have and its probability
    global maxDef                           
    maxAtk = 0
    maxDef = 0
    probDeck = 0
    probField = 0
    name = ""
    countDeck = 0
    countField = 0
    threatList = {}

    for checkmax in aiField:                #getting the max attack and max def monster the AI have
        if (maxAtk < checkmax.attack):
            maxAtk = checkmax.attack
    for checkdef in aiField:
        if (maxDef < checkdef.defense):
            maxDef = checkdef.defense
    if (playStyle == "Aggressive"):         #if the playstyle is aggressive, 
        for monster in aiField:             #check the predicted player deck for any monster 
            if (monster.attack >= maxAtk):  #that have higher attack than what the AI currently have
                for card in playerDeck:     
                    if (card.attack > monster.attack):
                        name = card.name       #store its name
                        print("Found Threat: " + name)  
                        for cards in playerDeck:         #look at how many copy of the card is in the deck and store the count
                            if(cards.name == name):      
                                countDeck = countDeck + 1
                        probDeck = countDeck / len(playerDeck) #calculate probablity that the player draw into the threat
                        threatList.update({name : probDeck}) #save the card and its probability into the threat list
                for card in playerField:                #doing the same thing but to learn the threats on the field instead
                    if (card.attack > monster.attack):
                        countField = countField + 1
                        name = monster.name                 
                        print("Found Threat: " + name)
                        probField = 1 / countField      #threats on the field probability will be calculated with higher weight
                        threatList.update({name : probField})
    else:                                           #this part is for passive play style
        for monster in aiField:                     #the logic is the same but use defense instead of attack to compare
            if (monster.attack >= maxDef):
                for card in playerDeck:
                    if (card.attack > monster.defense):
                        name = card.name
                        print("Found Threat: " + name)
                for cards in playerDeck:
                    if(cards.name == name):
                        countDeck = countDeck + 1
                probDeck = countDeck / len(playerDeck)
                threatList.update({name : probDeck})
                for card in playerField:
                    if (card.attack > monster.defense):
                        countField = countField + 1
                        name = monster.name
                        print("Found Threat: " + name)
                        probField = 1 / countField
                        threatList.update({name : probField})

    print("Threats List:",threatList)

def checkWin():
    global stop
    if (playerLife <= 0):
        print("AI wins!")
        input("Press Enter to exit...")
        stop = 0
    if (aiLife <= 0):
        print("Player wins!")
        input("Press Enter to exit...")
        stop = 0
    if (len(playerDeck) == 0 or len(aiDeck) == 0):
        print("No card left in the deck!")
        print("Draw!")
        input("Press Enter to exit...")
        stop = 0

def actionMaking(hand,grave,field,turn):
    global aiSum
    global aiTribute
    global aiSpell
    global aiEnd
    global aiChoice
    control = 0
    for fieldcard in field:             #Summon boss monster when ever possible
        control = control + 1
    for checkcard in hand:
        if (isinstance(checkcard.level, int) and checkcard.level > 9 and control > 0):
            aiTribute = 1
            aiSum = 0
            aiChoice = "tribute"
            rulebasedSystem(hand,field,grave,playStyle)
            break
        if (isinstance(checkcard.level, int) and checkcard.level < 9 and aiTribute == 0):
            aiSum = 1
            aiChoice = "summon"
            rulebasedSystem(hand,field,grave,playStyle)
        if (checkcard.effect != None):
            aiSpell = 1
            rulebasedSystem(hand,field,grave,playStyle)

def rulebasedSystem(hand, field, grave, playStyle):
    global aiSum
    global aiTribute
    global aiSpell
    global aiEnd
    global maxAtk
    global minAtk
    global maxDef
    global toSummon
    global toTribute
    global toActivate
    global toPosition
    global aiChoice
    minAtk = 5000
    maxAtk = 0
    maxDef = 0
    #check for max ATK
    for checkmax in hand:
        if (isinstance(checkmax.level, int) and checkmax.level < 9):
            if (maxAtk < checkmax.attack):
                maxAtk = checkmax.attack
    #check for min ATK
    for checkmin in field:
        if (isinstance(checkmin.level, int) and checkmin.level < 9):
            if (checkmin.attack < minAtk):
                minAtk = checkmin.attack
    #check for max DEF
    for checkdef in hand:
        if (isinstance(checkdef.level, int) and checkdef.level < 9):
            if (maxDef < checkdef.defense):
                maxDef = checkdef.defense
    #rule based system:
    #if play style is Agreesive
    #Summon highest attack monster in attack position
    #Prioritize tribute for boss monster with lowest attack monster whenever possible
    
    if(playStyle == "Aggressive"):
        if(aiChoice == "tribute"):                 
            control = 0
            for fieldcard in field:             #Summon boss monster when ever possible
                control = control + 1
            for checkcard1 in hand:
                if (isinstance(checkcard1.level, int) and checkcard1.level > 9 and control > 0):
                    toSummon = checkcard1.name
                    for checkfield in field:
                        if (checkfield.attack <= minAtk):
                            toTribute = checkfield.name
            toPosition = "attack"
            
        if(aiChoice == "summon"):
            for checkcard2 in hand:                 #Summon the highest attack monster in attack position
                if (isinstance(checkcard2.level, int) and checkcard2.level < 9):
                    if (checkcard2.attack >= maxAtk):
                        toSummon = checkcard2.name
            toPosition = "attack"
        if(aiSpell == 1):
            for checkcard3 in hand:
                if (checkcard3.effect != None):
                     toActivate = checkcard3.name
    #if play style is passive
    #Summon highest defense position monster in defense
    #Prioritize flooding the field with defense position monsters and wait for boss monster to tribute

    elif(playStyle == "Passive"):
        if(aiChoice == "tribute"):
            control = 0
            for fieldcard in field:
                control = control + 1                #Summon boss monster when having 2 or more monster
            for checkcard1 in hand:
                if (isinstance(checkcard1.level, int) and checkcard1.level > 9 and control > 0):
                    toSummon = checkcard1.name
                    for checkfield in field:
                        if (checkfield.attack <= minAtk):
                            toTribute = checkfield.name
            toPosition = "attack"
        if(aiChoice == "summon"):
            for checkcard2 in hand:                    #Summon the highest defense monster in defense position
                if (isinstance(checkcard2.level, int) and checkcard2.level < 9):
                    if (checkcard2.defense >= maxDef):
                        toSummon = checkcard2.name
            toPosition = "defense"
        if(aiSpell == 1):
            for checkcard3 in hand:
                if (checkcard3.effect != None):
                 toActivate = checkcard3.name

def DecisionTreeBattle(playStyle,threatList):
    global aiBattle 
    global maxAtk
    global Attack
    global toAttack
    count = 0
    maxAtk = 0
    for checkmax in aiField:                
        if (maxAtk < checkmax.attack):
            maxAtk = checkmax.attack
    if (playStyle == "Aggressive"):
        for defense in playerField:
            count = count + 1
            for attackcard in aiField:
                if(attackcard.position == "attack"):          
                    if(attackcard.attack > defense.attack):
                        aiBattle = 1
                    elif(attackcard.attack > defense.defense):
                        aiBattle = 1
    else:
        for defense in playerField:
            count = count + 1
            for attackcard in aiField:
                if(attackcard.position == "attack"):          
                    if(attackcard.attack > defense.attack):
                        aiBattle = 1
                    elif(attackcard.attack > defense.defense):
                        aiBattle = 1
    if(count == 0):
        for direct in aiField:
            if(direct.attack >= maxAtk):
                 Attack = direct.name
        aiBattle = 1
    if(aiBattle == 1):
        for attacker in aiField:
            if(attacker.attack > threatList):
                Attack = attacker.name
                toAttack = threatList.name
                break
            elif(attacker.attack >= maxAtk):
                for enemy in playerField:
                    if(enemy.position == "attack"):
                        if (attacker.attack > enemy.attack):
                            Attack = attacker.name
                            toAttack = enemy.name
                            break
                    else:
                        if (attacker.attack > enemy.defense):
                            Attack = attacker.name
                            toAttack = enemy.name
                            break
            
# GAME LOOP
CreateDecks()
deckNameList = {"DarkLord" : darklordDeck,
                "Blue-Eyes" : blueeyesDeck}
deckList = [darklordDeck, blueeyesDeck]
playerDeck = darklordDeck
aiDeck = blueeyesDeck
Draw(5, playerDeck, playerHand)
Draw(5, aiDeck, aiHand)
stop = stop + 1
while(stop != 0):
    if(stop != 1):
        Draw(1, playerDeck, playerHand)
        Draw(1, aiDeck, aiHand)
    else:
        battle = 1
    print("Player Turn:",stop)
    newTurn(playerHand,playerField,playerGrave,aiHand,aiField,aiGrave,"Player")
    print("AI Turn:",stop)
    deckPrediction(deckList)
    checkField(aiHand,aiField,aiGrave,"AI")
    createData(predictDeck,numSum,numMon,maxAtk)
    playStyleLearning(dataInput)
    BayesianLearning(playStyle)
    newTurn(playerHand,playerField,playerGrave,aiHand,aiField,aiGrave,"AI")
    stop = stop + 1
    checkWin()

