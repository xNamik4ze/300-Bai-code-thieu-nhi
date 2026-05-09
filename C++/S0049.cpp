#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (string s : strs) {
            string key = string(26, 0);
            for (char c : s) key[c - 'a']++;
            groups[key].push_back(s);

        }
        vector<vector<string>> res;
        for (auto p : groups) res.push_back(p.second);
        return res;
    }
};