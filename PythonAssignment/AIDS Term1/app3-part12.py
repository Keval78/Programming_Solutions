# Subject: AISC 1000_02 (Prof. Tim Nguyen)
# Assignment: Application Excercise 03W21 APP3PART2
# Student Name & Number: Keval Padsala (500199506)
# Student Name & Number: Alifiya Pipewala (500201710)
# Student Name & Number: Ria Sharma (500195363)
# Student Name & Number: Archit Verma (500195589)


import os, sys, random, re

################# <------------- start main region -------------> #################

class App3Part2():

    def __init__(self):
        print("******** Application 1 Part 2 ********")

    def create_eng_fre_dict(self):
        dict_eng_fre = {}
        print("Enter the inputs for English to French dictionary.")

        while True:                                         #Loop to get inputs for English/Spanish Dictionary.
            print("Enter the English word:", end=" ")
            eng_key = si()
            print("Enter the French word for {}:".format(eng_key), end=" ")
            fre_val = si()

            dict_eng_fre[eng_key] = fre_val

            print("Enter Y/y if you want to add more data into English/French dictionary.")
            if si() not in ["Y","y"]:
                return dict_eng_fre
    def create_fre_ger_dict(self):
        dict_fre_ger = {}
        print("Enter the inputs for French to German dictionary.")
        while True:                                         #Loop to get inputs for Spanish/Italian Dictionary.
            print("Enter the French word:", end=" ")
            fre_key = si()
            print("Enter the German word for {}:".format(fre_key), end=" ")
            ger_val = si()

            dict_fre_ger[fre_key] = ger_val

            print("Enter Y/y if you want to add more data into French/German dictionary.")
            if si() not in ["Y","y"]:
                return dict_fre_ger
    
    def check_word_in_dict(self, dict_eng_fre, dict_fre_ger):
        while True:                                         #Loop to get inputs from user and check it in both Dictionaries.
            print("Enter English word:", end=" ")
            eng_key = si()
            if eng_key not in dict_eng_fre.keys():
                print("{} is not avaialble English/French dictionary".format(eng_key))
            else:
                fre_key = dict_eng_fre[eng_key]
                if fre_key not in dict_fre_ger.keys():
                    print("{} is not avaialble French/German dictionary".format(eng_key))
                else:
                    ger_val = dict_fre_ger[fre_key]
                    print("German word for English word {} is: {}".format(eng_key, ger_val))
            
            print("Enter Y/y if you want to check more words into English/French & French/German dictionary.")
            if si() not in ["Y","y"]:
                return

    def main(self):
        run_more = True
        while run_more:                                         #Loop to run APP again...
            dict_eng_fre = self.create_eng_fre_dict()           #Function for craeting English to French dicationary.
            dict_fre_ger = self.create_fre_ger_dict()           #Function for craeting French to German dicationary.

            self.check_word_in_dict(dict_eng_fre, dict_fre_ger)                           #Function for check wrods in dicationaries.

            print("Enter Y/y if you want to execute it again.")
            if si() not in ["Y","y"]:
                print("Bye!")
                run_more = False


def main():

    app3_part2 = App3Part2()
    app3_part2.main()


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



