import os, sys

def main():
	# County codes as keys and County name as values.
	countries = {"BE": "Belgium", "FR": "France", "CZ": "Czechia",
				"DK": "Denmark", "IT": "Italy", "PT": "Portugal",
				"RO": "Romania", "SE": "Sweden", "PL": "Poland"}

	country_name = countries["BE"]					#get value from dictionary for key "BE"
	print("Country name for Country code 'BE':", end=" ")
	print(country_name)

	print("Before chnaging value of country code 'CZ':", countries["CZ"])
	countries["CZ"] = "Czech Republic"				#change value for key "CZ"
	print("After chnaging value of country code 'CZ':", countries["CZ"])

	countries["RO"] = "Romania"						#add key change value for key "CZ"
	print("Added country code 'RO' in dictionarys:", countries["RO"])

	country_name = countries.get("RO")				# get the value fro key "RO"
	print("Value of country code 'RO':", country_name)

	country_name = countries.get("IE")				# if key not exist it returns "None" value.
	print("Value of country code 'IE':", country_name,"(It will return 'None' if coudn't found values 'IE')")

	country_name = countries.get("IE", "Unknown")	# we can set second parameter as "Unknown" which return it instead of "None"
	print("Value of country code 'IE':", country_name ,"(It will return 'Unknown' if coudn't found values 'IE')")

	
	print("Check key is exist in dcitionary or not & get value country_code: IN")
	country_code = "IN"
	if country_code in countries:
		country_name = countries[country_code]
		print(country_name)
	else:
		print("The code", country_code,"isn't in the dictionary(countries).")




if __name__ == "__main__":
	main()