def parseIntcode(code):
	parsed_code = map(int, code.split(","))
	return parsed_code

def getValue(index, key, default=None):
	try:
		return index[key]
	except:
		return default

def add(memory, data):
	a = getValue(memory, data[0], default=0)
	b = getValue(memory, data[1], default=0)
	memory[data[2]] = a + b

def multiply(memory, data):
	a = getValue(memory, data[0], default=0)
	b = getValue(memory, data[1], default=0)
	memory[data[2]] = a * b

instructions = {
	1: {
		"input_count": 3,
		"function": add
	},
	2: {
		"input_count": 3,
		"function": multiply
	}
}

def getInstruction(opcode):
	try:
		return instructions[opcode]
	except:
		return None

def executeIntcode(code):
	if type(code) == str:
		code = parseIntcode(code)
	memory = code

	code_length = len(memory)
	i = 0
	while i < code_length:
		opcode = memory[i]
		if opcode == 99:
			break
		instruction = getInstruction(opcode)
		if instruction == None:
			raise Exception(" => Couldn't find an instruction with the opcode '{0}'".format(opcode))
		
		input_count = instruction["input_count"]
		function = instruction["function"]

		instruction_input = memory[i + 1:i + 1 + input_count]
		function(memory, instruction_input)

		i += input_count + 1

	return memory