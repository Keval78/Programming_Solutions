# Subject: AISC 1000_02 (Prof. Tim Nguyen)
# Assignment: Application Excercise 03W21 APP3PART2
# Student Name & Number: Keval Padsala (500199506)
# Student Name & Number: Alifiya Pipewala (500201710)
# Student Name & Number: Ria Sharma (500195363)
# Student Name & Number: Archit Verma (500195589)


import os, sys, random, re, math

################# <------------- start main region -------------> #################

class App3Part2():

    def __init__(self):
        print("******** Application 3 Part 2 ********")

    def q1(self):
        print("\n\nQUESTION 1:-")                       # QUESTION 1
        
        company_name = "The ABC company"
        position = "Software Engineer"
        gross_income = 85000

        print(company_name, '\n', position, '\n', gross_income)

    def q2(self):
        print("\n\nQUESTION 2:-")                       # QUESTION 2

        def print_value(company_name, position, gross_income):
            print(company_name, '\n', position, '\n', gross_income)
        
        company_name = "The ABC company"
        position = "Software Engineer"
        gross_income = 85000

        print_value(company_name, position, gross_income)

    def q3(self):
        print("\n\nQUESTION 3:-")                       # QUESTION 3

        def calc(a, b):
            return math.sqrt(a*b)
        
        print("Please, Enter the first number:", end=" ")
        self.a = ii()
        
        print("Please, Enter the second number:", end=" ")
        self.b = ii()

        print("The result of the square root is {}".format(calc(self.a, self.b)))

    def q4(self):
        print("\n\nQUESTION 4:-")                       # QUESTION 4

        def power(a):
            return a**5
        
        def mod(a,b):
            return a%b

        print("The Power({}^5) is: {}".format(self.a, power(self.a)))
        print("The value of modf({}%{}) is: {}".format(self.a, self.b, mod(self.a, self.b)))



def main():

    app3_part2 = App3Part2()
    app3_part2.q1()
    app3_part2.q2()
    app3_part2.q3()
    app3_part2.q4()


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



