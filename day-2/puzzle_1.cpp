#include <iostream>
#include <string>
#include <fstream>
#include <vector>

std::vector<int> intcode(std::vector<int> program)
{
	std::vector<int> memory = program;
	return memory;
}

std::vector<std::string> splitStr(char separator, std::string str)
{
	std::vector<std::string> split_string;
	char character;
	std::string buffer;
	for (int i = 0; i < str.length(); i++)
	{
		character = str[i];
		if (character == separator)
		{
			if (buffer.length() > 0) 
			{
				split_string.push_back(buffer);
				buffer = "";
			}
		}
		else
		{
			buffer += character;
		}
	}
	if (buffer.length() > 0) { split_string.push_back(buffer); }

	return split_string;
}

int main()
{
	std::string file_path = "input.txt";

	std::string line;
	std::ifstream input_file(file_path);

	if (input_file.is_open())
	{
		int number;
		std::vector<int> program;
		while(getline(input_file, line))
		{
			number = stoi(line);
			std::cout << number << std::endl;
			program.push_back(number);
		}
		input_file.close();

		std::cout << program[4] << std::endl;
	}

	std::string x = "Hello World";
	std::vector<std::string> words = splitStr(' ', x);
	std::cout << words[1] << std::endl;

	return 0;
}