#include <cmath>
#include <iostream>

using namespace std;

int largestDiff(int input[], int length) {
    int highestLeft[length];
    int lowestLeft[length];
    int lowest[length];
    int highest[length];
    highest[0] = lowest[0] = input[0];
    highestLeft[0] = lowestLeft[0] = input[0];
    for (int i = 1; i < length; i++) {
        int current = input[i];
        highest[i] = (current > current + highest[i-1]) ?
                current : current + highest[i-1];
        highestLeft[i] = (highest[i] > highestLeft[i-1]) ?
                highest[i] : highestLeft[i-1];
        lowest[i] = (current < current + lowest[i-1]) ?
                current : current + lowest[i-1];
        lowestLeft[i] = (lowest[i] < lowestLeft[i-1]) ?
                lowest[i-1] : lowestLeft[i-1];
    }
    int highestRight[length];
    int lowestRight[length];
    highest[length-1] = lowest[length-1] = input[length-1];
    highestRight[length-1] = lowestRight[length-1] = input[length-1];
    for (int i = length-2; i >= 0; i--) {
        int current = input[i];
        highest[i] = (current > current + highest[i+1]) ?
                current : current + highest[i+1];
        highestRight[i] = (highest[i] > highestRight[i+1]) ?
                highest[i] : highestRight[i+1];
        lowest[i] = (current < current + lowest[i+1]) ?
                current : current + lowest[i+1];
        lowestRight[i] = (lowest[i] < lowestRight[i+1]) ?
                lowest[i] : lowestRight[i+1];
    }
    int maxDiff = 0;
    int maxDiffIndex = 0;
    for (int i = 0; i < length - 1; i++) {
        if (abs(highestLeft[i] - lowestRight[i+1]) > maxDiff) {
            maxDiff = abs(highestLeft[i] - highestRight[i+1]);
        } else if (abs(lowestLeft[i] - highestRight[i+1]) > maxDiff) {
            maxDiff = abs(highestLeft[i] - highestRight[i+1]);
        }
    }
    return maxDiff;
}

int main () {
    int input1[5] = {-1,-1,2,2,2};
    cout << largestDiff(input1, 5) << endl;
    int input2[5] = {7,-1,2,2,2};
    cout << largestDiff(input2, 5) << endl;
}
