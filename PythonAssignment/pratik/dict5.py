import os, sys

def main():
	countries = {"BE": "Belgium", "FR": "France", "CZ": "Czechia",
				"DK": "Denmark", "IT": "Italy", "PT": "Portugal",
				"RO": "Romania", "SE": "Sweden", "PL": "Poland"}

	print("\n")
	print("get list of keys from dictinary and print it after sorting:-")
	country_codes = list(countries.keys())		# store all keys into list "country_codes"
	country_codes.sort()						# sort values of list "country_codes"
	for country_code in country_codes:			# print sorted country codes.
		print(country_code)

	
	print("\n")
	print("get list of values from dictinary and print it:-")
	for country_name in countries.values():		# values() returns list of values of dictionary.
		print(country_name)


	print("\n")
	print("convert 2D list into dictionary:-")
	countries_2d_list = [["BE", "Belgium"], ["FR", "France"], ["CZ", "Czechia"],
				["DK", "Denmark"], ["IT", "Italy"], ["PT", "Portugal"],
				["RO", "Romania"], ["SE", "Sweden"], ["PL", "Poland"]]
	countries = dict(countries)
	print(countries)

if __name__ == "__main__":
	main()
