# Subject: AISC 1000_02 (Prof. Tim Nguyen)
# Assignment: Application Excercise 1s21
# Student Name & Number: Keval Padsala (500199506)


import os, sys, random

################# <------------- start main region -------------> #################
###### Author : Keval_78
###### Date   : 7th OCT 2021

class AppExc1s21():

    def question1(self):

        again = "y"
        while again in ["y","Y"]:
            print("\nSales Tax Calculator")
            print("ENTER ITEMS (ENTER 0 TO END)")
            print("Cost of item:", end=" ")

            total_cost = 0.0
            total_cost += float(si())
            
            print("Total:", total_cost)
            print("Sales tax:", total_cost*0.13)
            print("Total after tax:", total_cost*1.13)

            again = si()


        print(ae1[-1])                          #Access sublist.
        print(ae1[-1][1])                       #Access sublist elements.
        print(ae1[random.randint(0,len(ae1)-1)])  #Randomly select any element.

    def q2(self):
        print("\nQuestion 2")
        istr = "cvM achiNe,Lear ningKowithisPyt:Hon"    #Input String
        # output_str = "Machine learning with python"

        output_str = istr[2] + istr[4:10].lower() +" "+ istr[11].lower() +istr[12:15] + istr[16:20] +" "+ istr[22:-9] +" "+ istr[-7].lower() + istr[-6:-4] + istr[-3:].lower()
        print(output_str)

    def q3(self):
        print("\nQuestion 3")
        records = []
        records.append(("Student1", 85, 75, 72))
        records.append(("Student2", 67, 56, 88))
        records.append(("Student3", 90, 61, 84))

        for i in range(len(records)):
            
            avg = round((records[i][1] + records[i][2] + records[i][3])/3, 2)
            if i==0:
                records.append((records[i][0], avg))
                print(records[-1])
            else:
                records[-1] = list(records[-1])
                records[-1].append(records[i][0])
                records[-1].append(avg)
                records[-1] = tuple(records[-1])
        print(records)
    
    def q4(self):
        # Customer account number:			12345
        # Minutes used:					(you provide)
        # Charge for the first 250 minutes@ 0.35:		(you provide)
        # Charge for the remaining minutes@ 0.55:	(you provide)	
        # Taxes:						(you provide)
        # Credits:						(you provide)
        # Total bill:					(you provide)

        print("\nQuestion 4")

        print("Enter Customer account number:", end=" ")
        can = si()
        print("Customer account number:",can)
        
        print("Enter Minutes used:", end=" ")
        minutes = ii()
        print("Minutes used:", minutes)
        
        before_250 = min(minutes,250)*0.35
        after_250 = 0
        print("Charge for the first 250 minutes@ 0.35:", round(min(minutes,250)*0.35, 2))
        if minutes > 250:
            after_250 = (minutes-250)*0.55
            print("Charge for the remaining minutes@ 0.55:", round((minutes-250)*0.55, 2))

        total_charge = before_250 + after_250
        print("Total Charge for", minutes, "minutes", total_charge)

        taxes = round(total_charge*0.11, 2)
        print("Taxes:", taxes)

        print("Enter Your Credits:", end = " ")
        credit = float(si())
        print("Credits:", credit)

        total_bill = total_charge + taxes - credit
        print("Total Bills:", total_bill)



def main():
    print("Application Exercise 1s21")

    appExc1s21 = AppExc1s21()
    appExc1s21.q1()
    appExc1s21.q2()
    appExc1s21.q3()
    appExc1s21.q4()


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
    read()
    main()



