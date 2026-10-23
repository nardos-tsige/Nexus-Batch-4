#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<int> minCounts(26, 100); //start with a high number
        for(const string& word : words){
            vector<int> currentCounts(26, 0);
            for (char c : word) {
                currentCounts[c - 'a']++;
            }
            for(int i = 0; i < 26; i++){
                minCounts[i] = min(minCounts[i], currentCounts[i]);
            }
        }
        vector<string> result;
        for(int i = 0; i < 26; i++){
            while (minCounts[i] > 0){
                result.push_back(string(1, i + 'a'));
                minCounts[i]--;
            }
        }
        return result;
    }
};
