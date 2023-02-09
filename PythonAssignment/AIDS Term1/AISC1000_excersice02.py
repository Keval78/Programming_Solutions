# Subject: AISC 1000_02 (Prof. Tim Nguyen)
# Assignment: Application Excercise 03
# Student Name & Number: Keval Padsala (500199506)
# Student Name & Number: Keval Padsala (500199506)
# Student Name & Number: Keval Padsala (500199506)


import os, sys, random, re

################# <------------- start main region -------------> #################

class AppExc2():

	def q1(self):
		print("\n\nQUESTION 1:-")
		l1, l2 = [1, 2, 3, 4, 5, ',', 7, 8, 9, 10], []				#List1 which contains 10 Elements & List2 emptylist
		print("List 1:", l1)
		print("List 2:", l2)
		l1 = list(filter(lambda a: (str(a)).isalnum() ,l1)) #Cleanup first list by removing special characters(using lambda).
		for i in range(len(l1)):
			l2.append(l1.pop())
		print("List 1:", l1)
		print("List 2:", l2)

	def q2(self):
		print("\n\nQUESTION 2:-")
		def take_and_validate_input():
			while True:
				inp = si()
				if inp.isdigit():
					inp = int(inp)
					return inp if inp >= 0 and inp <= 100 else print(inp, "Input must be between 0 and 100. Please enter valid input again.", end=": ")
				else:
					print("\""+inp+"\" Input is not Numeric. Please enter valid input again.", end=": ")

		add_more, count, details = True, 1, []
		while(add_more):									#Input loop to get values of students name & grades
			print("Enter new Student Name & grades for 3 subjects:".format(count))
			details.append(si())
			
			grades_temp = []
			for i in range(3):
				grades_temp.append(take_and_validate_input())

			details.append(grades_temp)

			details.append(sum(grades_temp)/len(grades_temp))
			
			print("Enter Y/y if you want to add more students details.")
			if si() not in ["Y","y"]:
				add_more = False
			count += 1

		print("Student details with name, grades & average grades:-\n",details)
	
	def q3(self):
		print("\n\nQUESTION 3:-")
		print("Please enter the number of entries and passwords you want to save in the tuple.")
		passwords = tuple([si() for i in range(ii())])
		print(passwords)

		print("Enter the password you want to check.")
		input_pass = si()
		for i in passwords:
			if i == input_pass:
				print(input_pass, "is found in Password entries.")
				break
		else:
			print(input_pass, "isn't found in the password entries.")





def main():
	print("**** Application Exercise 1s21 ****")

	appExc2 = AppExc2()
	appExc2.q1()
	appExc2.q2()
	appExc2.q3()



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



