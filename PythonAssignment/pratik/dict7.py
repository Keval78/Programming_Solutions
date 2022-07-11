import os, sys

def main():
	students = {"John":[78, 89, 99],
            	"Rudolf":[96, 100, 81],
            	"Donald":[93, 70, 84, 79]} # list as value in dictionary
	
	print("List as value in dictionary:-")
	print(students)
	
	print("Get values for key 'John':-", end=" ")
	print(students["John"])				# get values from embedded list
	
	print("Get first score of value of key 'John':-", end=" ")
	john_scores_1 = students["John"][0]	# get values from embedded list
	print(john_scores_1)


if __name__ == "__main__":
	main()
