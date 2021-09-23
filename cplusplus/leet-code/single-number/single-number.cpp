// filename: single-number.cpp
//
// by: Abhay Gupta
//
// Description:
// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
// You must implement a solution with a linear runtime complexity and use only constant extra space.

#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution
{
    public:
        int singleNumber(vector<int>& nums) {

            set<int> sln;
            
            for (int num : nums) {
                if (sln.count(num)){
                    sln.erase(num);
                } else {
                    sln.insert(num);
                }
            }

            if (sln.size() == 1) {
                for (int num : sln) {
                    return num;
                }
            }
            return 1;
        }
    
    public:
        int doubleNumber(vector<int>& nums) {

        }

};

int main()
{
    std::cout << "hello\n";

    vector<int> nums = {2, 2, 3};
    vector<int> nums1 = {4, 1, 2, 1, 2};
    vector<int> nums2 = {1};

    Solution sln;
    int temp = sln.singleNumber(nums);
    temp = sln.doubleNumber(nums);

    cout << temp << endl;
}

