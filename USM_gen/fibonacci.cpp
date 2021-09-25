// Create fibonaaci sequence
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <numeric>

using namespace std;

int main(){
    vector<int> fibonacci;
    fibonacci.push_back(1);
    fibonacci.push_back(1);

    while(fibonacci.size() < 10){
        fibonacci.push_back(fibonacci[fibonacci.size() - 1] + fibonacci[fibonacci.size() - 2]);
    }
    
    return 0;
}