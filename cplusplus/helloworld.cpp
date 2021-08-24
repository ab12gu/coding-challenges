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
#include <vector>
#include <string> 
#include <initializer_list>

// using:       introduces all the names from std namespace into the global namespace (current scope)
// namespace:   declarative region that provides a scope to identifers
// std:         C++ "standard" namespace
// "::" :       scope operator, tells compiler where what namespace to look for an identifier
// --> Take everything that is in the std namespace and dump it into the global namespace || may cause naming conflicts :(
using namespace std;

int main()
{
    std::cout << "Hello World" << std::endl; // use regional namespace 
    cout << "Goodbye World" << endl; // use global namespace  

    std::vector<std::string> myvector {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension"};

    // known exact amount of iterations
    // word type:   a reference to a string whose contents cannot be changed 
    for (const string& word : myvector) 
    {
        // console out command, prints to console
        std::cout << word << " "; // insertion operator "<<"
    }

    std::cout << std::endl;

    const int i = 1;
    int j = 2;
}

// Methods of passing variables through functions:
//
// Pass by value:       a copy of the original object is created and passed
// Pass by pointer:     only the memory address of the original object is passedA
// Pass by reference:   an alias for original object passed  
//      ++ no need for pointer notation when declaring actual object
//      ++ no need to check for NULL (cannot be allocated without allocated memory)





