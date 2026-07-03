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
        
        vector<int> result;
        for (int i = less_count; i < less_count + count; i++) {
            result.push_back(i);
        }
        
        return result;
    }
};
