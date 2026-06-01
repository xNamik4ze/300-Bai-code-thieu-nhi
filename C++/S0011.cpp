#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1;
        int res = 0;
        while (l < r) {
            int lengths = r - l;
            int cur_water = lengths * min(heights[l], heights[r]);
            res = max(res, cur_water);
            if (heights[l] < heights[r]) l++;
            else r--;
        }
        return res;
    }
};