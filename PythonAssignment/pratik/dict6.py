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
		} # dictionary of dictionaries

	
	print("Get values from embedded dictionary of 'Mary'")
	print("Phone:", contacts["Mary"]["phone"])
	print("Email:", contacts["Mary"]["email"])

	# get values from embedded dictionary of "Charles"
	sub_key = "phone"
	if sub_key in contacts["Charles"]:
		sub_key_value = contacts["Charles"][sub_key]
		print("value from embedded dictionary of 'Charles' for key 'phone'",sub_key_value)
	else:
		print("Sorry, This contact(Charles) does not have", sub_key)

	print("Print List of contact of every values:-")
	for key in contacts.keys():
		phone = contacts.get(key).get("phone")     #Print sub_key "Phone" for every values.
		print(phone)



if __name__ == "__main__":
	main()
	