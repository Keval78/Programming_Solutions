# Subject: AISC 1000_02 (Prof. Tim Nguyen)
# Assignment: Application Excercise 02 s21
# Student Name & Number: Keval Padsala (500199506)
# Student Name & Number: Ria Sharma (500199506)
# Student Name & Number: Archit Verma (500199506)


import os, sys, random

################# <------------- start main region -------------> #################

class AppExc2s21():

    def q1(self):
        print("\nSales Tax Calculator")         ####SALES TAX CALCULATOR####

        def take_and_validate_input():          # Validate Input is greater than zero and float or not.
            while True:
                inp = si()
                try:
                    inp = float(inp)
                    return inp if inp >= 0 else print(inp, "Input must be greater than 0. Please enter valid input again.", end=": ")
                except:
                    print("\""+inp+"\" Input is not Numeric. Please enter valid input again.", end=": ")

        def count_tax_and_sales_tax(taxes):     # Print total and sales tax.
            print("Total:", round(sum(taxes),2))
            print("Sales tax:", round(sum(taxes)*0.13, 2))

        def count_total_after_tax(taxes):       # Print total after tax.
            print("Total after tax:", round(sum(taxes) + sum(taxes)*0.13, 2))

        count_more, taxes= True, []
        while(count_more):                      # Loop with Y/y.
            print("ENTER ITEMS (ENTER 0 TO END)")
            while True:                         # Loop to take input unitl zero.
                print("Cost of item:", end=" ")
                inp = take_and_validate_input()
                
                if(inp == 0):
                    break
                
                taxes.append(inp)
            count_tax_and_sales_tax(taxes)
            count_tax_and_sales_tax(taxes)

            print("Again? (y/n):")
            if si() not in ["Y","y"]:
                print("Thanks, bye!")
                count_more = False


    def q2(self):
        print("\nDice Roller")                  ####DICE ROLLER####

        def take_and_validate_input():          # Validate Input is betweeen 1 to 6.
            while True:
                inp = si()
                if inp.isdigit():
                    inp = int(inp)
                    return inp if inp >= 1 and inp <= 6 else print(inp, "Input must be between 1 and 6. Please enter valid input again.", end=": ")
                else:
                    print("\""+inp+"\" Input is not Numeric. Please enter valid input again.", end=": ")
        
        def roll_names(die1, die2):            # Roll dice names(reference: "https://en.wikipedia.org/wiki/Craps").
            rolls = {
                (1,1): "Snake Eyes", 
                (1,2): "Ace Deuce", (2,2):"Hard Four", 
                (1,3): "Easy Four", (2,3): "Five (Fever Five)", (3,3): "Hard Six",
                (1,4): "Five (Fever Five)", (2,4): "Easy Six", (3,4): "Natural/Seven Out", (4,4): "Hard Eight",
                (1,5): "Easy Six", (2,5): "Natural/Seven Out", (3,5): "Easy Eight", (4,5): "Nine (Nina)", (5,5): "Hard Ten",
                (1,6): "Natural/Seven Out", (2,6): "Easy Eight", (3,6): "Nine (Nina)", (4,6): "Easy Ten", (5,6): "Yo (Yo-leven)", (6,6): "Boxcars/Midnight"
            }
            return(rolls[min(die1, die2), max(die1, die2)])

        def print_output(die1, die2):          # Print Total & Output name.
            print("Total:", die1 + die2)
            print(roll_names(die1, die2))


        roll_more, taxes= True, []
        
        print("Roll the dice? (y/n):")
        if si() not in ["Y","y"]:
            roll_more = False

        while(roll_more):                       # Loop if user wants roll more dice.
            die1 = random.randint(1,7)
            print("Die 1:", die1)
            die2 = random.randint(1,7)
            print("Die 1:", die2)

            print_output(die1, die2)

            print("Roll the dice? (y/n):")
            if si() not in ["Y","y"]:
                roll_more = False

    def q3(self):
        print("\nQuestion 3")                  ####QUESTION 3####
        list1 = ['Python', 'Maths Data Science', 'Machine Learning', 'Step Presentation', 'Statistical Modelling and Inference', 1000, 1002, 1003, 1004, 1005]
        list2, list3 = [None]*5, [None]*5

        print(len(list1), len(list1)//2, -1)
        for i in range(len(list1), len(list1)//2, -1):                                      # Loop in list1 from Length to (length/2).
            rand_choice = random.choice([i for i in range(len(list2)) if list2[i]==None])   #randomly select one from indices which has value None
            list2[rand_choice] = list1.pop()                                                #pop() the value and add into list at radom position
        
        for i in range(len(list1), 0, -1):                                                  # Loop in list1 from (length/2) to 0.
            rand_choice = random.choice([i for i in range(len(list3)) if list3[i]==None])   #randomly select one from indices which has value None
            list3[rand_choice] = list1.pop()                                                #pop() the value and add into list at radom position

        print(list2)                                                #Print randomly create list2.
        print(list3)                                                #Print randomly create list3.
        dict_l2_l3 = dict(zip(list2, list3))
        print(dict_l2_l3)                                           #Print Dictionary from two lists.




def main():
    print("****Application Exercise 2s21****")

    appExc2s21 = AppExc2s21()
    appExc2s21.q1()
    appExc2s21.q2()
    appExc2s21.q3()


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
    # read()                        # uncomment to access an FILE IO.
    main()



