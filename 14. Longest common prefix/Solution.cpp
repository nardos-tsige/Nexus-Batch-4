#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::string longestCommonPrefix(std::vector<std::string>& strs) {
        if (strs.empty()) return "";
        
        std::string shortest = *std::min_element(strs.begin(), strs.end(),
            [](const std::string& a, const std::string& b) {
                return a.size() < b.size();
            });
        
        for (int i = 0; i < shortest.size(); i++) {
            char c = shortest[i];
            
            for (const std::string& s : strs) {
                if (s[i] != c) {
                    return shortest.substr(0, i);
                }
            }
        }
        return shortest;
    }
};
