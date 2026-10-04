#include <string>
#include <vector>
class Solution {
public:
    std::string addSpaces(std::string s, std::vector<int>& spaces) {
        std::string result;
        result.reserve(s.size() + spaces.size());
        int spaceIdx = 0;
        for (int i = 0; i < s.size(); i++) {
            if (spaceIdx < spaces.size() && i == spaces[spaceIdx]) {
                result += ' ';
                spaceIdx++;
            }
            result += s[i];
        }
        return result;
    }
};
