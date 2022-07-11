# Subject: AISC 1000_02 (Prof. Tim Nguyen)
# Assignment: Application Excercise 03W21 APP3PART1
# Student Name & Number: Keval Padsala (500199506)
# Student Name & Number: Alifiya Pipewala (500201710)
# Student Name & Number: Ria Sharma (500195363)
# Student Name & Number: Archit Verma (500195589)


import os, sys, random, re

################# <------------- start main region -------------> #################

class App3Part1():

    def __init__(self):
        print("******** Application 1 Part 1 ********")

    def count_inputs(self):
        print("Please Enter, How many floating point numbers with 5 integer digits and two decimal digits the program should accept??")
        return ii()
    
    def take_and_validate_number(self):
        print("Please Enter again with 5 digits and two decimal digits.", end=" ")
        while True:
            str_number = si()
            digits = str_number.split(".")
            digit = digits[0] if len(digits) > 0 else None
            decimal_digit = digits[1] if len(digits) > 1 else None
            print(digit, decimal_digit)
            if (digit.isnumeric() and decimal_digit.isnumeric()):
                if len(digit) + len(decimal_digit) <= 5:
                    if len(decimal_digit) == 2:
                        return float(str_number)
                    else:
                        print("{} do not have 2 decimal digits".format(str_number))
                else:
                    print("{} do not have 5 digits".format(str_number))
            else:
                print("{} is not numeric".format(str_number))
            print("Please Enter number again with 5 digits and two decimal digits:", end=" ")

    def main(self):

        n = self.count_inputs()                  #Take number of inputs from user.

        total_inp = 0
        for _ in range(n):
            inp = self.take_and_validate_number()
            total_inp += inp

        print(total_inp)


def main():

    app3_part1 = App3Part1()
    app3_part1.main()


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



