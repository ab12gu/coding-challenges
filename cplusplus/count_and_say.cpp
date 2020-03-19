// filename: count_and_say.cpp
//
// By: Abhay Gupta
// Desc: Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. 

#include <iostream>
using namespace std; 
#include <string>

class Solution {
public:
    string countAndSay(int n) {
        std::string str ("1");

        if (n == 1) {
            return str;
        };

        std::string new_str ("");
        int count, check;

        for (int a = 1; a <= n-1; a += 1) {
            count = 0;
            check = (int)str[0] - 48;

            for (std::string::size_type i = 0; i < str.size(); i++) {
                int j = (int)str[i] - 48;

                if (check == j) {
                    count += 1;
                } else {
                    new_str += std::to_string(count) + str[i-1];
                    count = 1;
                    check = j;
                }
            }
            new_str += std::to_string(count) + str.back();

            str = new_str;
            new_str =  "";
        }


        return str;

    };
};



int main() {
    Solution sol;
    int N = 4;
    cout << sol.countAndSay(N) << endl;
    return 0;
}