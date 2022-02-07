#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(x) for(ll i=0; i<x;i++)
#define fr(k,x) for(ll i=k; i<x;i++)
#define arr(a,n) ll a[n];for(ll i=0;i<n;i++) cin>>a[i];
#define ff first
#define ss second
#define tc ll t;cin>>t;while(t--)
#define pb push_back
#define pob pop_back
#define ve vector
#define vll vector<ll>
#define mod 1000000007
#define pi 3.14159265
#define setbits(x) __builtin_popcountll(x)
#define fio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define sp(x) fixed<<setprecision(int x)

void solve(){
    ll i,j,k,l,p,q,n;
    cin>>n;
    string s;
    cin>>s;
    if(n%2==1){
        cout<<"NO\n";
        return;
    }
    map<char,int>m;
    vector<pair<int,char>>v;
    for(i=0;i<n;i++)
        m[s[i]]++;
    for(auto x: m){
        v.push_back(make_pair(x.second,x.first));
    }
    
    sort(v.begin(),v.end());
    string r="";
    for(i=0;i<v.size();i++){
        p=v[i].first;
        if(p>(n/2)){
            cout<<"NO\n";
            return;
        }
        
        for(j=0;j<p;j++){
            r+=v[i].second;
        }
    }
    j=n/2;
    i=0;
    j--;
    char c;
    while(i<j){
        c=r[i];
        r[i]=r[j];
        r[j]=c;
        i++;j--;
    }
    cout<<"YES\n"<<r<<"\n";
    
}

int main()
{
    fio
    ll t;
    cin>>t;
    while(t--){
        solve();
    }
    return 0;
}
