import string
from os import system

#Functions
def best_char(current_wordlist,tested):
        letter_val_dict = {}
        for i in range (len(string.ascii_lowercase)):
            char_letter = string.ascii_lowercase[i]
            # Skip if char is tested
            if tested.find(char_letter) != -1:
                continue
            sum_avg = 0
            for j in range(len(current_wordlist)):
                if current_wordlist[j].find(char_letter)!=-1:
                    sum_avg = sum_avg+1
            #dict["a"] = 100
            letter_val_dict[char_letter] = sum_avg
        #Sort dict
        letter_val_dict = sorted(letter_val_dict.items(),reverse=True,key=lambda x:x[1])
        # [(a,1232),(b,232)]
        return letter_val_dict[0][0]
        # a

def test_letter(current_wordlist,test_char):
        #User input instead
        wrong = False
        if input("Is the char < " + test_char + " > inside? y/n\n") == "y":
            positions = input("Enter position, indexed 0, separated by commas if there are more than one, (1,2,6,9)").split(",")
            #char is inside
            print(positions)
            n = 0
            for i in range(len(current_wordlist)):
                for j in range(len(positions)):
                    current_word = current_wordlist[i-n]
                    if current_word.find(test_char) != int(positions[j]):
                        current_wordlist.pop(i-n)
                        n = n+1
        else:
            #Char is not inside
            wrong = True
            n = 0
            for i in range(len(current_wordlist)):
                if current_wordlist[i-n].find(test_char) != -1:
                    current_wordlist.pop(i-n)
                    n = n+1
        return current_wordlist, wrong

#Variables
global_counter = 0
wordlist = open("../files/words.txt","r").read().splitlines()
length = int(input("Enter length of word \n")) #int(input("How long is the word?:\n"))
already_tested = ""
global_wrongs = 0
#Setup
temp_counter = 0

for i in range(len(wordlist)):
    if len(wordlist[i-temp_counter])!= length:
        wordlist.pop(i-temp_counter)
        temp_counter = temp_counter+1


#Play
while True:
    global_counter = global_counter+1
    
    current_char = best_char(wordlist, already_tested)
    already_tested = already_tested + current_char
    res = test_letter(wordlist, current_char)


    wordlist = res[0]
    if res[1]:
        global_wrongs = global_wrongs+1
    
    print("Round",global_counter,"\nWords:", len(wordlist))
    print("="*30)
    #print(wordlist)
    if len(wordlist) < 2:
        print(10*" ","Results:", already_tested)
        print("Total tests:", len(already_tested), "\nWrongs:",  global_wrongs)
        print("Word:", wordlist)
        break