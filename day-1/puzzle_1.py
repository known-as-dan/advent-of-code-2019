import sys
import os
import math

def getFileContent(path):
	fi = open(path, "r")
	content = fi.read()
	fi.close()
	return content

def calcFuel(mass):
	"calculate the amount of fuel necessary for any mass"
	fuel = math.floor(mass / 3) - 2
	return fuel

def main():
	script_directory = sys.path[0]
	input_path = "input.txt" # path relative to the script directory
	full_path = os.path.join(script_directory, input_path)

	aoc_input = getFileContent(full_path)
	mass_list = map(int, aoc_input.split("\n")) # parsing the string for the masses of the modules
	
	fuel_sum = 0
	for mass in mass_list:
		fuel_sum += calcFuel(mass)
	
	print(fuel_sum)
	

if __name__ == "__main__":
	main()