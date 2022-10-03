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
    ll N;
    cin >> N;

    ll B = 1;
    ll b = 0;

    ll ans = INF;
    while (B <= N) {
        ll a = N / B;
        ll c = N % B;

        if (ans > a + b + c) ans = (a + b + c);

        b++;
        B *= 2;
    }

    cout << ans << endl;

}