import os, sys

def main():
	contacts = {
			"Mary": {
				"address": "3603 Sheppard Ave", 
				"city": "Toronto", "state": "Ontario", "postalCode": "M1S 1T4", 
				"phone": "416-339-9531", "email": "z9vhdddrsh@temporary-mail.net"},
			"Charles": {"address": "478 Sixth Street", 
				"city": "Pincher Creek", "state": "Alberta", "postalCode": "T0K 1W0", 
				"phone": "403-627-0285", "email": "82h7ojcl3gj@temporary-mail.net"},
			"Gloria": {"address": "3773 Russell Avenue", 
				"city": "Langley", "state": "British Columbia", "postalCode": "V4X 1J7",  
				"phone": "604-825-3070"},
		}

	phone = contacts["Mary"]["phone"] 
	email = contacts["Mary"]["email"]
	print(phone, email)

	print("Enter your key value.")
	sub_key = input().lower()
	if sub_key in contacts["Charles"]:
		sub_key_value = contacts["Charles"][sub_key]
		print(sub_key_value)
	else:
		print("Sorry, This contact(Charles) does not have", sub_key)

	for key in contacts.keys():
		phone = contacts.get(key).get("phone")     #Print sub_key "Phone" for every values.
		print(phone)



if __name__ == "__main__":
	
	#Comment these two lines for user Input
	sys.stdin  = open('../input.txt', 'r')  
	sys.stdout = open('../output.txt', 'w')
	#Comment these two lines for user Input 
	main()
	