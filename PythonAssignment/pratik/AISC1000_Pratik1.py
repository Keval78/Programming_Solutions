import os, sys

def main():
	print("Asynchronous class 07F21")
	countries = [["FR", "France"], ["DE", "Germany"], ["PT", "Portugal"]]
	countries = dict(countries)
	print(countries)

	print("COMAND MENU\nview - View country name\nadd - Add a country\ndel - Delete a country\nexit - Exit program")
	commands = ["view", "add", "del", "exit"]
	while True:
		while True:
			command = input()
			if command.lower() == "view":
				print("Command: view")
				print("Country codes:", countries.keys())
				print("Enter country code:", end=" ")
				print("Country name", countries[input().upper()])
			
			elif command.lower() == "add":
				print("Command: add")
				print("Country codes:", countries.keys())
				print("Enter country code:", end=" ")
				country_code = input().upper()
				print("Enter country name:", end=" ")
				country_name = input()
				print(country_name, "was added")
			
			elif command.lower() == "del":
				print("Command: del")
				print("Enter country code:", end=" ")
				print(countries.pop(input().upper()), "was deleted")
			
			elif command.lower() == "exit":
				print("Command: exit")
				print("Bye!")
				return
			
			else:
				continue
			break
		if (input() not in ["Y","y"]):
			break




if __name__ == "__main__":
	
	#Comment these two lines for user Input
	sys.stdin  = open('../input.txt', 'r')  
	sys.stdout = open('../output.txt', 'w')
	#Comment these two lines for user Input 
	main()
