#include <vector>
#include <numeric>
using namespace std;
class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        int less_count = 0;
        int count = 0;
        
        for (int num : nums) {
            if (num < target) {
                less_count++;
            } else if (num == target) {
                count++;
            }
        }
        
        if (count == 0) return {};
        
        vector<int> result(count);
        iota(result.begin(), result.end(), less_count);
        
        return result;
    }
};
