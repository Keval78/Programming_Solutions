# Subject: AISC 1000_02 (Prof. Tim Nguyen)
# Assignment: Case Study 01 S21
# Student Name & Number: Keval Padsala (500199506)

import os, sys, math


################# <------------- start main region -------------> #################

class EnergyBills:
    def __init__(self, years, prior_to_greens):
        self.years = years                                          #Array of years.
        self.energy_bills = [12*[0] for i in range(len(years))]     #Arrays of energy billd for all years.
        self.energy_bills_saving = 12*[0]                           #Energy saving for every month.
        self.prior_to_greens = prior_to_greens                      #Year is prior to green or not.
        self.months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    
    def take_and_validate_input(self):                              #################Get Input & Validate it. (Task 7)#################
        while True:
            inp = si()
            if inp.isdigit():
                inp = int(inp)
                if inp >= 0:
                    return inp
                else:
                    print(inp, "Input must be greater than 0. Please enter valid input again.", end=": ")
            else:
                print(inp,"Input is not Numeric. Please enter valid input again.", end=": ")
    
    def get_energy_bills(self):
        for i in range(len(self.years)):
            print(self.years[i])
            print("Enter Energy bills for every month for a year "+("prior to" if (self.prior_to_greens[i]) else "after going")+" green")
            for j in range(len(self.months)):
                print("Enter energy bills for "+self.months[j%12],end=": ")
                self.energy_bills[i][j] = self.take_and_validate_input()
        
        
        #################Take input and validate it. (Task 3)#################
        self.X = 12*[0]
        print("Enter X value for 12 months.")
        for i in range(len(self.months)):
            print("Enter X value for "+self.months[i],end=": ")
            inp = si()
            if inp.isdigit():
                inp = int(inp)
                if inp >= 0:
                    self.X[i] = inp
                else:
                    print(inp, "Input must be greater than 0. assuming it's a average of last inputs.")
                    self.X[i] = sum(self.X[0:i])//i
            else:
                print(inp,"Input is not Numeric. assuming it's a average of last inputs.")
                self.X[i] = sum(self.X[0:i])//i
    
    def calculate_savings(self):
        print("%-12s %-8d %-8d %-8s %-8s %-15s %-15s %-15s"%("Month", self.years[0], self.years[1], "X", "Saving", "Max. Saving", "Min. Saving", "Avg. Saving"))
        print("%-12s %-8s %-8s %-8s %-8s %-15s %-15s %-15s"%("*****", "****",        "****",        "*", "******", "***********", "***********", "***********"))
        for i in range(len(self.months)):
            self.energy_bills_saving[i] = self.energy_bills[0][i] - self.energy_bills[1][i]
            if i==0:
                print("%-12s %-8d %-8d %-8s %-8s %-15s %-15s %-15s"%(self.months[i], self.energy_bills[0][i], self.energy_bills[1][i], "?", str(self.energy_bills_saving[i]), str(max(self.energy_bills_saving)), str(min(self.energy_bills_saving)), str(self.energy_saving_avg)))
                #################Format Output. (Task 6)#################
            else:
                print("%-12s %-8d %-8d %-8s %-8s"%(self.months[i], self.energy_bills[0][i], self.energy_bills[1][i], "?", str(self.energy_bills_saving[i])))

    def calculate_diff_saving(self):                                        #################Calculate diffrence of energy. (Task 1)#################
        for i in range(len(self.months)):
            self.energy_bills_saving[i] = self.energy_bills[0][i] - self.energy_bills[1][i]
        
        max_index = self.energy_bills_saving.index(max(self.energy_bills_saving))   #################Max. and Min. saving months. (Task 4)#################
        min_index = self.energy_bills_saving.index(min(self.energy_bills_saving))
        print("Maximum Saving Month:",self.months[max_index])
        print("Minimum Saving Month:",self.months[min_index])

    def calculate_avg_saving(self):
        self.energy_bills_avg = []
        for i in range(len(self.years)):
            self.energy_bills_avg.append(sum(self.energy_bills[i])/len(self.energy_bills[i]))
            print("Avg bill for year:", self.years[i], "=", round(self.energy_bills_avg[i],2)) 
        
        self.energy_saving_avg = 0
        self.energy_saving_avg = round(sum(self.energy_bills_saving)/len(self.energy_bills_saving), 2)
        print("Avg saving:", round(self.energy_saving_avg,2))               #################Avg. of savings. (Task 5)#################


    def calculate_pearson_correlation_coefficients(self):
        print(self.X)

        #################Pearson Correlation Coefficients (Task 2)#################
        self.X_mean = sum(self.X)/len(self.X)
        self.Y_mean = sum(self.energy_bills_saving)/len(self.energy_bills_saving)

        self.numerator = 0
        self.denominator_1 = 0
        self.denominator_2 = 0
        for i in range(12):
            self.numerator += ((self.X[i] - self.X_mean) * (self.energy_bills_saving[i] - self.Y_mean))
            self.denominator_1 += ((self.X[i] - self.X_mean) * (self.X[i] - self.X_mean))
            self.denominator_2 += ((self.energy_bills_saving[i] - self.Y_mean) * (self.energy_bills_saving[i] - self.Y_mean))

        corrcoef = self.numerator/math.sqrt(self.denominator_1*self.denominator_2)

        print(corrcoef)
        print("Type of correlation between X and Saving is:","POSITIVE." if corrcoef > 0 else "NEGATIVE." if corrcoef < 0 else "NO CORRELATION")


        


def main():
    print("Sample Run:")
    eb = EnergyBills([2019, 2020], [True,False])
    eb.get_energy_bills()                                       #Get Input & Validate it. (Task 7)# & #Calculate Pearson Correlation. (Task 3)#
    eb.calculate_diff_saving()                                  #Calculate diffrence of energy. (Task 1)#  &  #Max. and Min. saving months. (Task 4)#
    eb.calculate_avg_saving()                                   #Avg. of savings. (Task 5)#
    eb.calculate_savings()                                      #Format Output. (Task 6)#
    eb.calculate_pearson_correlation_coefficients()             #Accept Only valid input and Data Cleaning. (Task 2)#



################# <------------- end main region -------------> #################


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
    # dmain()
