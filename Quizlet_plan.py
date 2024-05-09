import random

class Item:
    
    def __init__(self, term, defin, level=0):
        self.term = term
        self.defin = defin
        self.level = level

    def __str__(self):
        return "(" + str(self.level) + ") " + self.term + ": " + self.defin # only aesthetic

    def print_to_file(self):
        return self.term + ":" + self.defin + "=" + str(self.level) # to save to file 


    def get_term(self):
        return self.term
    
    def get_defin(self):
        return self.defin

    def increase_level(self):
        self.level+=1


#def save
    
def learn(items):
    
    for item in item_set:
        if item.level == 0: # multiple choice
            
            random_list = items.copy()      # make copy of item list for manipulation
            
            rand_item1 = random.choice(random_list) # choosing random item from list 
            choice1 = rand_item1.get_defin() # getting definition from random item
            
            
            pos1 = random_list.index(rand_item1) # finding position of random item just chosen
            random_list.remove(rand_item1) # remove random item so there aren't duplicate choices

        # repeated for remaining 3 option
            rand_item2 = random.choice(random_list)
            choice2 = rand_item2.get_defin()
            
            pos2 = random_list.index(rand_item2)
            random_list.remove(rand_item2)

            rand_item3 = random.choice(random_list)
            choice3 = rand_item3.get_defin()
            if choice1 != item.get_defin() and choice2 != item.get_defin() and choice3 != item.get_defin():
                choice4 = item.get_defin() # if none are correct, make the 4th correct
            else:
                pos3 = random_list.index(rand_item3)
                random_list.remove(rand_item3)

                rand_item4 = random.choice(random_list)
                choice4 = rand_item4.get_defin()
                
            choice_list = [choice1,choice2,choice3,choice4]
            random.shuffle(choice_list) # randomize order that choices are shown
           

            print("\n" + item.get_term())

            for i in range(len(choice_list)):
                print(str(i+1) + ": "+ choice_list[i]) # print term and options for definition

            if choice_list[int(input())-1] == item.get_defin():
                
                print("Correct!\n")
                item.increase_level() # increases level when correct
            else:
                if input("False! Override as correct? (y/n)\n").lower()=="y":
                    item.increase_level()
                    print("\n\n")
                
        elif item.level == 1: # enter def given term
            defin_guess=input(item.get_term()+"\n\nEnter Definition: ")
            if defin_guess==item.get_defin():
                print("Correct!\n")
                item.increase_level()
            else:
                if input("\nFalse! Override as correct? (y/n)\n").lower()=="y":
                    item.increase_level()
                    print("\n")
        elif item.level == 2 or item.level == 3:  # enter term given def
            term_guess=input(item.get_defin()+"\n\nEnter Term: ")
            if term_guess==item.get_term():
                print("\nCorrect!\n")
                item.increase_level()
            else:
                if input("\nFalse! Override as correct? (y/n)\n").lower()=="y":
                    item.increase_level()
                    print("\n")
    #if input("reset progress? (y/n)\n")==y:
        #none
   # else:
      #  save

            
def learn_def_first(items):
    for item in items:  # Loops through cards and print each card's definition, interprets results (need to add term first, multiple choice and 
        term_guess=input(item.defin+"\n\n")
        if term_guess==item.term:
            print("\nCorrect!\n")
            if int(item.level)==1: # Adds level if correct, but need way to not advance all terms to term-first, jave to base it on levels
                item.level=int(item.level)+1
        else:
            if input("\nFalse! Override as correct?\n\n").lower()=="y":
                if int(item.level)==1:
                    item.level=int(item.level)+1
                print("\n")
def learn_term_first(items):
    for item in items:
        defin_guess=input(item.get_term()+"\n\n")
        if defin_guess==item.get_defin():
            print("\nCorrect!\n")
            item.increase_level()
        else:
            if input("\nFalse! Override as correct? (y/n)").lower()=="y":
                item.increase_level()
                print("\n")







while True:
    master=open("/Users/tomseifert/Desktop/Python/quizlet_index.txt")
    set_list=[]
    for line in master: # getting rid of indent character at the end of each line when looping through for set names
        set_list.append(line[:-1])

    for i in range(1,len(set_list)+1): # presenting sets as options to proceed with, accompanied by integers
        print(str(i) + ":" + set_list[i-1])
    set_chosen=int(input("\nChoose a set\n"))
    
    try:
        if set_chosen in range(1,len(set_list)+1):
            active_set=open("/Users/tomseifert/Desktop/Python/"+str(set_list[int(set_chosen)])+".txt","r") # reading set file 
            item_set=[]
            
            for line in active_set: # reads file by line, splits each into term and definition, adds it to a list as the Item class
                
                term=line[:line.index(":")]
                
                defin=line[line.index(":")+1:line.index("\n")]
                
                #level=int(line[line.index("=")+1:line.index("\n")])
                
                item_set.append(Item(term,defin))
                
                    # close file since parsing through file is done
        else:
            print('Please select a valid set number')
    except:
        None
        #print(set_list)
        #continue
        
    # load master file of all set names
    # make list of set names extracted from file
    # index each set and ask for input
    # set_name = int(input("which set?"))


    # load specified set here using set_name (files will be named set_name.txt)
    # create list of Items here, then operate on them in the next loop


    while True: # Try to add new features like definitions of certain groups of terms, or how certain terms relate to one another, find ways to test that knowledge

        
        try:
            opt = int(input("select option: 0: Choose new set, 1: Learn, 2: Flashcards, 3: Edit set, 4: Print set\n"))
        except:
            print("what")

        if opt == 0:
            break
        elif opt == 1:
            learn(item_set)
            while True:
                try:
                    learn_opt = int(input("Learn options: 0: Exit learn, 1: Continue"))
                except:
                    print("Please Enter an Integer")
                    continue
                if learn_opt == 0:
                    learn_save = input("Save Progress? (y/n)")
                    if learn_save == "n":
                        break
                    else:
                        pre_save_set = open("/Users/tomseifert/Desktop/Python/"+str(set_list[int(set_chosen)-1])+".txt","w")
                        
                elif learn_opt == 1:
                    learn(item_set)
               



                    
            #learn_def_first(item_set)
            #learn_term_first(item_set)
            #for item in item_set:  # Loops through cards and print each card's definition, interprets results (need to add term first, multiple choice and 
                #term_guess=input(item.defin+item.level+"\n\n")
                #if term_guess==item.term:
                    #print("\nCorrect!\n")
                #else:
                    #if input("\nFalse! Override as correct?\n\n").lower()=="yes":
                        #print("\n")
            
                    
        elif opt == 2:
            random.shuffle(item_set)
            print("you have selected Flashcards, which has not been made yet")
            for item in item_set:
                input(item.term)
                input(item.defin + "\n")
            
        elif opt == 3: # Change this to a numbered list of items in the file plus an extra option to add a new item, can edit or add
            term = str(input("Term:")) 
            defin = str(input("Definition:"))
            item_set.append(Item(term, defin))

        elif opt == 4:
            for i in item_set:
                print(i)
            print()

        elif opt == -1:
            # remember to load new data *back* into the *samefile, in the same format
            break

        else:
            print("what")
