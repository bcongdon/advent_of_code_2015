#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

string processString(string input){
	int count = 0;
	char chr = input[0];
	string output = "";
	for(int i = 0; i < input.length(); i++){
		if(chr == input[i]) count ++;
		else if(count > 0){
			output += to_string(count);
			output += chr;
			count = 1;
			chr = input[i];
		}
	}
	output += to_string(count);
	output += chr;
	return output;
}

void day10(string puzzleInput, int iterations){
	clock_t begin = clock();
	string input = "1113122113";
	for(int i = 0; i < 10000; i++) {//iterations; i++){
		input = processString(input);
		cout << i << endl;
	}
	cout << to_string(iterations) + " iterations: ";
	cout << to_string(input.length()) << endl;
	clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	cout << "Seconds to complete: " + to_string(elapsed_secs) << endl;
	cout << endl;
}

int main()
{
	day10("1113122113",40);
	day10("1113122113",50);
}