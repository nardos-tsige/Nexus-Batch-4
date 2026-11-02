class Solution {
public:
    int mySqrt(int x) {
        if(x < 2) return x;
        long long i = 1;
        while(i * i <= x) {
            i = i * 2; //double the guess
        }
        while(i * i > x) {
            i--; //step back until we hit the floor
        }
        return i;
    }
};
