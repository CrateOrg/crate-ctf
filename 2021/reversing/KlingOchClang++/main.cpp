#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
	volatile int changeme = 2;

	int original[41] = {90, 980, 52, 835, 60, 874, 985, 148, 236, 49, 35, 224, 134, 102, 15, 18, 919, 68, 922, 2, 975, 838, 139, 80, 15, 87, 128, 891, 978, 1012, 990, 16, 998, 1001, 988, 27, 875, 889, 48, 38, 479};
	vector<int> key{218, 225, 38, 71, 151, 157, 92, 9, 160, 177, 217, 167, 170, 23, 176, 184, 229, 42, 101, 222, 202, 108, 142, 232, 165, 181, 11, 152, 90, 6, 51, 35, 249, 94, 229, 94, 61, 143, 54, 13, 37};
	int last = 32;
	vector<int> middle;
	vector<int> final_flag(41);

	for(int i=40; i>=0; --i) {
		last = int(original[i]^last);
		middle.push_back(last);
	}

	for_each(middle.begin(), middle.end(), [](int &i){ i-= 423; });
	transform(middle.rbegin(), middle.rend(), key.begin(), back_inserter(final_flag), [](int &i1, int &i2){ return i1^i2; });

	if(changeme==1) {
		for(char c: final_flag) {
			cout << c;
		}
	} else {
		cout << "Almost there..." << endl;
	}
}
