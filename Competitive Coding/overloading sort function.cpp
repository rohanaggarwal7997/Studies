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
#define S second
bool cmp(pll p1,pll p2)
{
    return p1.F<p2.F;
}
bool cmp2(pll p1,pll p2)
{
    return p1.S<p2.S;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    pll a[3];
    rep(i,0,2)cin>>a[i].F>>a[i].S;
    sort(a,a+3,cmp);
    cout<<"according to first value"<<endl;
    rep(i,0,2)cout<<a[i].F<<" "<<a[i].S<<endl;
    sort(a,a+3,cmp2);
    cout<<"according to second value"<<endl;
    rep(i,0,2)cout<<a[i].F<<" "<<a[i].S<<endl;


    return 0;
}
