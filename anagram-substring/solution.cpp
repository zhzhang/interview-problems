#include <iostream>
#include <cstring>
#include <map>

using namespace std;

// Uses a map for convenience, but to avoid the worst case
// O(nm) time, an RBTree can be used for O(nlogm)
bool anagramSubstring(const char* x, const char* y) {
    map<char,int> xCounts;
    int xTotal = 0;
    for (int i = 0; i < strlen(x); i++) {
        xCounts[*(x+i)]++;
        xTotal++;
    }
    int startIndex = 0;
    for (int i = 0; i < strlen(y); i++) {
        char c = *(y+i);
        if (xCounts.find(c) == xCounts.end()) {
            while (startIndex < i) {
                xCounts[*(y + startIndex)]++;
                xTotal++;
                startIndex++;
            }
            startIndex++;
        } else if (xCounts[c] == 0) {
            while (xCounts[c] == 0 && startIndex < i) {
                xCounts[*(y + startIndex)]++;
                xTotal++;
                startIndex++;
            }
            xCounts[c]--;
            xTotal--;
        } else {
            xCounts[c]--;
            xTotal--;
        }
        if (xTotal == 0) {
            return true;
        }
    }
    return false;
}

int main() {
    cout << anagramSubstring("abc", "abc") << endl;
    cout << anagramSubstring("abc", "bca") << endl;
    cout << anagramSubstring("abc", "aabc") << endl;
    cout << anagramSubstring("abc", "aaaa") << endl;
    cout << anagramSubstring("abc", "a") << endl;
    cout << anagramSubstring("hello", "hehehello") << endl;
    cout << anagramSubstring("hello", "olololleh") << endl;
    cout << anagramSubstring("hello", "ololollehasd") << endl;
    cout << anagramSubstring("hello", "olololleasd") << endl;
}
