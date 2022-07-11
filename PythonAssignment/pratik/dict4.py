import os, sys

def main():
	countries = {"BE": "Belgium", "FR": "France", "CZ": "Czechia",
				"DK": "Denmark", "IT": "Italy", "PT": "Portugal",
				"RO": "Romania", "SE": "Sweden", "PL": "Poland"}

	print("Loop through keys() and print key Value pair:-")
	print("Code" + "   " + "Country Name")
	for country_code in countries.keys():					# print every key value pair from dictionary
		print(country_code + "     " + countries[country_code])
	
	print("\n")
	print("Iterate over every items of dictinary using items():-")
	print("Code" + "   " + "Country Name")
	for country_code, country_name in countries.items():	# items() provides a tuple of key-value pairs over which we may iterate.
		print(country_code + "     " + country_name)

	print("\n")
	print("Loop through values() and print values:-")
	print("Country Names")
	for country_name in countries.values():					# values() returns list of values of dictionary.
		print(country_name)



if __name__ == "__main__":
	main()
