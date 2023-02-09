# Subject: AISC 1000_02 (Prof. Tim Nguyen)
# Assignment: Application Excercise 03
# Student Name & Number: Keval Padsala (500199506)
# Student Name & Number: Alifiya Pipewala (500201710)
# Student Name & Number: Ria Sharma (500195363)
# Student Name & Number: Archit Verma (500195589)


import os, sys, random, re

################# <------------- start main region -------------> #################

class AppExc3():

    def __init__(self):
        print("******** Application Exercise 3s21 ********")

    def q1(self):
        print("\n\nQUESTION 1:-")

        run_more = True             #Loop to run APP again...
        while run_more:
            print("Please enter the number of entries and passwords you want to save in the tuple.")
            passwords = tuple([si() for i in range(ii())])      #take number of passwords and passwords and store into tuple.
            print(passwords)

            print("Enter the password you want to check:", end=" ")
            input_pass = si()
            for i in passwords:                                 #FOR....ELSE
                if i == input_pass:
                    print(input_pass, "is found in Password entries.")
                    break
            else:
                print(input_pass, "isn't found in the password entries.")
            
            print("Enter Y/y if you want to execute it again.")
            if si() not in ["Y","y"]:
                print("Bye!")
                run_more = False


    def q2(self):
        print("\n\nQUESTION 2:-")

        run_more = True
        while run_more:                                         #Loop to run APP again...
            dict_eng_spa = {}
            dict_spa_itl = {}

            print("Enter the inputs for English to Spanish dictionary.")

            while True:                                         #Loop to get inputs for English/Spanish Dictionary.
                print("Enter the English word:", end=" ")
                eng_key = si()
                print("Enter the Spanish word for {}:".format(eng_key), end=" ")
                spa_val = si()

                dict_eng_spa[eng_key] = spa_val

                print("Enter Y/y if you want to add more data into English/Spanish dictionary.")
                if si() not in ["Y","y"]:
                    break

            while True:                                         #Loop to get inputs for Spanish/Italian Dictionary.
                print("Enter the Spanish word:", end=" ")
                spa_key = si()
                print("Enter the Italian word for {}:".format(eng_key), end=" ")
                itl_val = si()

                dict_spa_itl[spa_key] = itl_val

                print("Enter Y/y if you want to add more data into Spanish/Italian dictionary.")
                if si() not in ["Y","y"]:
                    break
            
            while True:                                         #Loop to get inputs from user and check it in both Dictionaries.
                print("Enter English word:", end=" ")
                eng_key = si()
                if eng_key not in dict_eng_spa.keys():
                    print("{} is not avaialble English/Spanish dictionary".format(eng_key))
                else:
                    spa_key = dict_eng_spa[eng_key]
                    if spa_key not in dict_spa_itl.keys():
                        print("{} is not avaialble Spanish/Italian dictionary".format(eng_key))
                    else:
                        itl_val = dict_spa_itl[spa_key]
                        print("Italian word for English word {} is: {}".format(eng_key, itl_val))
                
                print("Enter Y/y if you want to check more words into English/Spanish & Spanish/Italian dictionary.")
                if si() not in ["Y","y"]:
                    break
        
            print("Enter Y/y if you want to execute it again.")
            if si() not in ["Y","y"]:
                print("Bye!")
                run_more = False

    def q3(self):
        print("\n\nQUESTION 3:-")                       # QUESTION 3
        print("Enter inputs for countries names and capitals")
        dict_cc = {}
        while True:
            print("Enter First country name and then capital of that country.")
            dict_cc[si()] = si()                        # Input contry name and capitals and store into dictionary.
            print("Enter Y/y if you want to add more values into dictionary.")
            if si() not in ["Y","y"]:
                break
        
        # Check values using isalpha() which allows letters only.
        cleaned_countries = [country for country in list(dict_cc.values()) if country.replace(" ","").isalpha()]
        cleaned_capitals = [capital for capital in list(dict_cc.keys()) if capital.replace(" ","").isalpha()]

        print("valid Capitals: ",cleaned_capitals)
        print("valid Countries: ",cleaned_countries)

    def q4(self):
        print("\n\nGame Stats program:-")

        def stats():                # Generate stats for each player ranbdomly.
            return {'Wins':random.randint(0,50), 'Losses':random.randint(0,50), 'Ties':random.randint(0,50)}

        player_stats = {            # Player stats Dictionary
            'Keval': stats(),
            'Alifiya': stats(),
            'Ria': stats(),
            'Archit': stats(),
            'Player1': stats(),
            'Player2': stats(),
        }

        print("ALL PLAYERS:\n")
        for payer in sorted(dict.keys(player_stats)):   # loop through sorted dictionary.
            print(payer)

        while True:
            print("Enter a player Name:", end=" ")
            player = si()
            if player in player_stats.keys():
                for key,value in player_stats[player].items():
                    print("{}: {}".format(key,value))
            else:
                print("Sorry, Player with the name {} does not exists.".format(player))
            print("Continue? (y/n)")
            if si() not in ["Y","y"]:
                print("Bye!")
                break






def main():

    appExc3 = AppExc3()
    appExc3.q1()
    appExc3.q2()
    appExc3.q3()
    appExc3.q4()



################# <------------- end main region -------------> #################
###### normal io ######

def ii():  return int(input())
def si():  return input()
def mi(ss=" "):  return map(int,input().strip().split(ss))
def msi(ss=" "): return map(str,input().strip().split(ss))
def li(ss=" "):  return list(mi(ss))

def read():
    sys.stdin  = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')


if __name__ == "__main__":
    # read()
    main()



