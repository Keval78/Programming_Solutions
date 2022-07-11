#################### I/O SECTION ####################

import sys

fastio = sys.stdin.readline


def inp():
    return(int(fastio()))
def flp():
    return(float(fastio()))
def inlt():
    return(list(map(int,fastio().split())))
def insr():
    s = fastio()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,fastio().split()))
def stvr():
    return(fastio().split())


#################### MAIN SECTION ####################

def main(args):
	print("Enter your first name, last name and user ID:")
	firstName, lastName, userId = stvr()

	print('''Enter the pay rate, hours per day and days you worked during this week''')
	
	hpRate = flp()
	whours = flp()
	wDays = flp()
	
	print("Name:", firstName, lastName)
	print("User ID:", userId)

	print("Pay Rate:", hpRate)
	print("Hours:", whours)
	print("Days:", wDays)

	print('Weekly Pay: $',(hpRate * whours * wDays))

	print("Process finished with exit code 0")
	return 0



if __name__ == '__main__':
    sys.exit(main(sys.argv))

#################### OUTPUT ####################
'''

$ python3 AISC1000_excersice01_Keval_500199506.py 
Enter your first name, last name and user ID:
Keval Padsala 500199506
Enter the pay rate, hours per day and days you worked during this week
15.75
8.5
5
Name: Keval Padsala
User ID: 500199506
Pay Rate: 15.75
Hours: 8.5
Days: 5.0
Weekly Pay: $ 669.375
Process finished with exit code 0

'''