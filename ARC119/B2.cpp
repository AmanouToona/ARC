#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll pow_ll(ll x, ll y) {
    ll ret = 1;
    while (y > 0) {
        if (y & 1) ret *= x;
        x *= x;
        y >>= 1;
    }
    return ret;
}

int const INF = INT_MAX;


int main() {
    int N;
    string S, T;
    cin >> N;
    cin >> S >> T;

    int zero=0;
    for (auto s: S) {
        if (s == '0') zero++;
    }
    int zero2 = 0;
    for (auto t: T) {
        if (t == '0') zero2++;
    }

    if (zero != zero2) {
        cout << -1 << endl;
        return 0;
    }

    int act1 = 0, act2 = 0;
    for (int i = 0; i < N; i++) {
        if (i < zero && S[i] == '1')
    }


}

// 15
// 101011101111111
// 111111111111000
