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
	for x in range (99):
			for y in range(99):
				parsed_code = intcode.parseIntcode(code)
				parsed_code[1] = x
				parsed_code[2] = y
				memory = intcode.executeIntcode(parsed_code)
				if memory[0] == 19690720:
					print("noun={} verb={}".format(x, y))
					break

if __name__ == "__main__":
	main()