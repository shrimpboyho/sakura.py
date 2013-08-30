#include <iostream>
#include "sakura.h"

int main(int argc, char* argv[]){
	if(argv[1]){
		std::cout << "Reading from file " << argv[1] << std::endl;
	}
	return 0;
}
