import os, sys

def main():
	countries = {"BE": "Belgium", "FR": "France", "CZ": "Czechia",
				"DK": "Denmark", "IT": "Italy", "PT": "Portugal",
				"RO": "Romania", "SE": "Sweden", "PL": "Poland"}

	del countries["PL"]								# delete key-value pair from dictionary
	print("Key 'PL' was deleted from dictionary(countries).")
	del countries["PT"]
	print("Key 'PT' was deleted from dictionary(countries).")



	country_code = "PL"
	if country_code in countries:
		country_name = countries[country_code]
		del countries[country_code]
		print(country_name, "was deleted from dictionary(countries).")
	else:
		print("The code", country_code,"isn't in the dictionary(countries).")

	country_name = countries.pop("FR")								# pop() which deletes key-value pair and returns deleted value.
	print("Using pop(), get the country name for key 'FR':", country_name)

	try:
		country_name = countries.pop("IN")							# if country code doesn't exist it shows error
	except Exception as e:
		print("KeyError:", end=" ")
		print(str(e))
	
	country_name = countries.pop("IN", "Unknown")					# We may avoid errors by providing the second argument.
	print("Value of country code 'IN':", country_name ,"(It will return 'Unknown' if coudn't found values 'IN')")

	country_code = "SE"
	country_name = countries.pop(country_code, "Unknown country") # Avoids the occurrence of a KeyError
	print(country_name + " was deleted.")

	countries.clear()											# delete every items from dictionary.
	print(countries, "<-- emprty dictionary after deleteing every item using clear() method.")



if __name__ == "__main__":
	main()
