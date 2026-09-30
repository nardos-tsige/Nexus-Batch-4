class Solution {
public:
    string interpret(string command) {
        string goalparser = "";
        int i = 0;
        while (i < command.size()){
            if (command[i]=='G') {
                goalparser += "G";
                i++;
            }
            else if (command.substr(i, 2) == "()"){
                goalparser += "o";
                i += 2;
            }
            else{
                goalparser += "al";
                i += 4;
            }
        }
        return goalparser;
    }
};
