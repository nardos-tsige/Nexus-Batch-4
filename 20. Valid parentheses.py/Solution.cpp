class Solution {
public:
    bool isValid(string s) {
        std::stack<char> st;
        std::unordered_map<char, char> dictt = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for (char i : s) {
            if (i == '(' || i == '[' || i == '{') {
                st.push(i);
            } else {
                if (st.empty()) return false;
                
                char top = st.top();
                st.pop();
                
                if (top != dictt[i]) return false;
            }
        }
        
        return st.empty();
    }
};
