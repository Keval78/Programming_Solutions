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
        print("******** Application 1 Part 3 ********")

    def create_country_capitals_lists(self):
        list_cc = [[],[]]
        while True:
            print("Enter country name & then capital of that country.")
            list_cc[0].append(si())                   # Input contry name and capitals and store into dictionary.
            list_cc[1].append(si())                   # Input contry name and capitals and store into dictionary.
            print("Enter Y/y if you want to add more values into dictionary.")
            if si() not in ["Y","y"]:
                return list_cc

    def get_capital_from_country(self, list_cc):
        while True:                                         #Loop to get capital of country
            print("Enter country name to find its capital:", end=" ")
            country_name = si()
            print(list_cc)
            capital = [list_cc[1][i] for i in range(len(list_cc[0])) if list_cc[0][i].lower() == country_name.lower()]
            if len(capital) > 0:
                print("Capital for country: {} is {}".format(country_name, capital[0]))
            else:
                print("Couldn't find capital for country: {}".format(country_name))
            
            print("Enter Y/y if you want to check more capitals.")
            if si() not in ["Y","y"]:
                break


    def main(self):
        run_more = True
        while run_more:                                         #Loop to run APP again...

            list_cc = self.create_country_capitals_lists()              #Function for craeting lists of country and capitals.
            self.get_capital_from_country(list_cc)                      #Function for check wrods in list of lists.

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



