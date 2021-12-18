// filename: maximum_subarray.cpp
//
// by: Abhay Gupta
// date: 03-18-20
// desc: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.



#include <iostream>
using namespace std; 
#include <string>
#include <bits/stdc++.h> 

class Solution {
public:
    int maxSubArray(vector<int>& nums, int low, int high) {
        if (low == high) {
            return 
        }
        return high;
        
    }
};
struct output { 
    int low, high, sum; 
}; 
  
typedef struct output Struct; 
 
int main() {
    Solution sol;
    vector<int> vect{ -2,1,-3,4,-1,2,1,-5,4 };
    low = sol.maxSubArray(vect, 0, vect.size()-1) 
    cout << << endl;

    return 0;

}