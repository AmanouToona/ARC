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

    ll ans = 0;
    ll stack = 0;
    bool todo = false;
    int waiting;
    for (int i = 0; i < N; i++) {
        if (S[i] != T[i]) {
            if (!todo) {
                todo = true;
                waiting = S[i];
                continue;
            } else {
                todo = false;
                ans ++;
                ans += stack;
                stack = 0;
                S[i] = S[i] == '0' ? '1': '0';
                if (S[i] != T[i]) {
                    todo = true;
                    waiting = S[i];
                    continue;
                }
            }
        }

        if (todo && S[i] != waiting) stack++;

    }

    cout << ans << endl;

}

// 15
// 101011101111111
// 111111111111000
