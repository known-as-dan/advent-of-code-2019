#include <iostream>
#include <string>
#include <fstream>
#include <math.h>

using namespace std;

float getFuel(float mass)
{
	float fuel = floor(mass / 3) - 2;
	return fuel;
}

int main()
{
	string file_path = "input.txt";

	string line;
	ifstream input_file(file_path);

	if (input_file.is_open())
	{
		int module_mass;
		float fuel_sum = 0;
		while(getline(input_file, line))
		{
			module_mass = stoi(line);
			fuel_sum += getFuel(module_mass);
		}
		input_file.close();

		cout << fixed << fuel_sum << endl;
	}

	return 0;
}