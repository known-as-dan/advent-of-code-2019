import sys
import os
import intcode

def getFileContent(path):
	fi = open(path, "r")
	content = fi.read()
	fi.close()
	return content

def main():
	script_directory = sys.path[0]
	input_path = "input.txt" # path relative to the script directory
	full_path = os.path.join(script_directory, input_path)

	code = getFileContent(full_path)
	parsed_code = intcode.parseIntcode(code)
	parsed_code[1] = 12
	parsed_code[2] = 2
	memory = intcode.executeIntcode(parsed_code)
	
	print(memory[0])

if __name__ == "__main__":
	main()