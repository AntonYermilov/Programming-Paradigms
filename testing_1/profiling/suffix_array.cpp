#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

vector<int> buildSuffixArray(const string &text) {
    size_t n = text.size();

    vector<int> array(n), position(n), helper(n);
    for (int i = 0; i < n; ++i) {
        array[i] = i;
        position[i] = text[i];
    }

    int bucketSize = 1;
    auto cmp = [&](int i, int j) noexcept {
        if (position[i] != position[j])
            return position[i] < position[j];
        i += bucketSize;
        j += bucketSize;
        return (i < n && j < n) ? position[i] < position[j] : i > j;
    };

    for (;;bucketSize <<= 1) {
        std::sort(array.begin(), array.end(), cmp);
        for (int i = 0; i != n - 1; ++i) {
            helper[i + 1] = helper[i] + cmp(array[i], array[i + 1]);
        }
        for (int i = 0; i < n; ++i) {
            position[array[i]] = helper[i];
        }
        if (helper[n - 1] == n - 1)
            break;
    }
    return array;
}

int main() {
    string text;
    cin >> text;
    auto sa = buildSuffixArray(text);
    // for (int i: sa) {
    //     cout << i << " ";
    // }
    cout << sa.size() << endl;
    return 0;
}
