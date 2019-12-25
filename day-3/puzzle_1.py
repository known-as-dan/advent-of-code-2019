import sys
import os

def getFileContent(path):
	fi = open(path, "r")
	content = fi.read()
	fi.close()
	return content

def main():
	script_directory = sys.path[0]
	input_path = "input.txt" # path relative to the script directory
	full_path = os.path.join(script_directory, input_path)

	aoc_input = getFileContent(full_path)

if __name__ == "__main__":
	main()
