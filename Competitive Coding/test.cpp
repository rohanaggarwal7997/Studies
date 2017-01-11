#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef long double ld;
#define rep(i,a,b) for(ll i=a;i<=b;++i)
#define rev(i,a,b) for(ll i=a;i>=b;i--)
#define pll pair<ll,ll>
#define vll vector<ll>
#define sll set<ll>
#define vpll vector<pll>
#define F first
struct compare {
    bool operator()(pll p1,
                    pll p2) const {
        return p1.F < p2.F;
    }
};

int main()
{
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    pll (3,4);
    cout<<pll(3,4).first;
    multiset<pll,compare> mult;
    mult.insert(pll(5,10));
    mult.insert(pll(3,11));
    multiset<pll,compare>::iterator it=mult.end();
    it--;
    it--;
    cout<<endl;
    cout<<(*it).first<<" "<<(*it).second;


    return 0;
}
