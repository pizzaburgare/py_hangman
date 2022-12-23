import string
from os import system
from random import randint
#Functions
#Solving
def find_nth(string, substring, n):
   if (n == 1):
       return string.find(substring)
   else:
       return string.find(substring, find_nth(string, substring, n - 1) + 1)

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

def test_letter(current_wordlist,test_char, word):
        #User input instead
        wrong = False
        if word.find(test_char)!=-1:
            #char is inside
            positions = []
            
            for i in range(len(word)):
                pos = find_nth(word, test_char, i+1)
                if(pos==-1):
                    break
                else:
                    positions.append(pos)

            for j in range (len(positions)):
                n = 0
                for i in range(len(current_wordlist)):
                    # Find word
                    current_word = current_wordlist[i-n]

                    # [s]assy = 0; sas[s]y = 3
                    if find_nth(current_word, test_char, j+1) != int(positions[j]):
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

def remove_wrong_length(wordlist,length):
    temp_counter = 0
    for i in range(len(wordlist)):
        if len(wordlist[i-temp_counter])!= length:
            wordlist.pop(i-temp_counter)
            temp_counter = temp_counter+1
    return wordlist

def smart_solve(word):
    #Vars
    already_tested = ""
    local_wordlist = open("../files/words.txt","r").read().splitlines()
    wrongs = 0
    length = len(word)
    local_wordlist = remove_wrong_length(local_wordlist, length)

    while True:
        current_char = best_char(local_wordlist, already_tested)
        already_tested = already_tested + current_char
        res = test_letter(local_wordlist, current_char, word)
        local_wordlist = res[0]
        if res[1]:
            wrongs = wrongs + 1
        if len(local_wordlist)<2:
            return wrongs
            break
#Save to file
def write_arr_to_file(file, arr_in):
    file.write(" ".join([str(elm) for elm in arr_in]))

#Variables
#Setup

#Play
f = open("../files/words.txt","r").read().splitlines()

#Random list==========
my_list = []
for i in range(len(f)):
    my_list.append(i)
#=====================
#Data collection======
length_arr = []
wrong_arr = []
over_six_arr = []


for i in range(len(f)):
    r = randint(0, len(my_list)-1)
    wrong_attempts = smart_solve(f[r])
    word_length = len(f[r])
    over_six = wrong_attempts>6

    #Push to arr
    length_arr.append(word_length)
    wrong_arr.append(wrong_attempts)
    over_six_arr.append(over_six)

    #system("clear")
    print(i)
    if i%100 == 99:
        print(length_arr,"\n",wrong_arr,"\n",over_six_arr)
        with open("saved.txt", "w") as outfile:
            write_arr_to_file(outfile, length_arr)
            outfile.write("\n")
            write_arr_to_file(outfile, wrong_arr)
            outfile.write("\n")

            write_arr_to_file(outfile, over_six_arr)


    '''  print("\n")
    print(f[r])
    print("Wrongs", wrong_attempts) 
    print("Length", word_length) 
    print("Over 7:", over_six)'''
    
