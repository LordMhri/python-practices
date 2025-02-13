#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    int n;
    cin >> n;

    vector<int> nums;


    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        nums.push_back(num);
    }

    sort(nums.begin(),nums.end());

    int ans = 1; //forgot the first number we encounter is also a unique number

    for(int i = 0; i < n-1;i++) {
        if (nums[i+1] - nums[i] != 0)
        {
            ans += 1;
        }
        
    } 

    cout << ans << endl;
    

    return 0;
}