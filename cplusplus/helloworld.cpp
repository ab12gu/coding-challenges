// filename: helloworld.cpp
//
// by: Abhay Gupta
// date: 21-08-22
//
// description: sanity check script of C++ language by printing hello world

// include:     import libraries 
// include:     tells preprocessor to include the contents of a specified file at the point where the directive (instruction) appears
// directive:   specifies how a compiler should process its input
#include <iostream>

// using:       introduces all the names from std namespace into the global namespace (current scope)
// namespace:   declarative region that provides a scope to identifers
using namespace std;

int main()
{
    std::cout << "Hello World" << std::endl; // use regional namespace 
    cout << "Goodbye World" << endl; // use global namespace  
}






