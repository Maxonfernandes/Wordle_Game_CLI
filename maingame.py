import random

#list of words 
list_word = [
    "Apple", "Beach", "Crane", "Dream", "Eagle", "Flame", "Grasp", "House", "Index", "Jolly",
    "Knock", "Lemon", "Magic", "Noble", "Ocean", "Pearl", "Quiet", "River", "Stone", "Train",
    "Unity", "Vivid", "Wheat", "Xerox", "Yacht", "Zebra", "Blaze", "Chill", "Dwarf", "Every",
    "Frost", "Ghost", "Honey", "Ivory", "Jumpy", "Kiosk", "Light", "Maple", "Nerve", "Orbit",
    "Prism", "Quest", "Round", "Shine", "Trace", "Urged", "Valor", "Whirl", "Xylic", "Yield",
    "Zesty", "Alarm", "Brave", "Cloud", "Dance", "Elbow", "Flair", "Gloom", "Haste", "Ideal",
    "Joint", "Karma", "Latch", "Mirth", "Novel", "Opine", "Panic", "Quite", "Rally", "Scene",
    "Tower", "Urban", "Voice", "Witty", "Xerox", "Youth", "Zooms", "Agile", "Blend", "Craft",
    "Dough", "Ember", "Flute", "Gears", "Hinge", "Inlet", "Jolly", "Kneel", "Ledge", "Mocha",
    "Nurse", "Olive"
]

#converts everything to lowercase
list_words=[element.lower() for element in list_word]

size_words = len(list_words)

#selecting a random word from the list of words
word =list_words[random.randint(0,size_words)] 

#initiate output list
list_out = ['_']*5

#print(word)

for i in range(0,6):  #6 attempts
    count=0
    inp = input("Enter your word guess = ")
    inp=inp.lower() #converts the words letters to lowercase
    size_inp = len(inp)
    for i in range(0,size_inp):  #iterate and check for all letter match in the word
        if inp[i] == word[i]:
            list_out[i]=inp[i]  #if correct then add the correct letter to the right index in the output list
            count+=1  #counter used to keep a track of correct letter so that the game ends when the user gets all the letters right
        elif inp[i] not in word:
            print(inp[i]," doesnt exist.")
        else:
            print(inp[i]," exists but in other index.")
            
    list_out = [element.upper() for element in list_out]
    print('|',list_out[0],'|',list_out[1],'|',list_out[2],'|',list_out[3],'|',list_out[4],'|')
    print('----------------------------------------')
    if count == 5:
            break
    
