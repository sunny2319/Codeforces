#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main() {
	// your code goes here
	ll n,p,q,r;
	cin>>n>>p>>q>>r;
 
	ll arr[n];
	for(ll i=0;i<n;i++)
		cin>>arr[i];
	ll mp1[n],mr1[n];
	mp1[0]=p*arr[0];
	for(ll i=1;i<n;i++)
	{
		mp1[i]=max(mp1[i-1],p*arr[i]);
	}
	mr1[n-1]=r*arr[n-1];
	for(ll i=n-2;i>=0;i--)
	{
		mr1[i]=max(mr1[i+1],r*arr[i]);
	}
	ll max1=-9223372036854775808;
	for(ll i=0;i<n;i++)
	{
		ll x=mp1[i]+q*arr[i]+mr1[i];
		if(x>max1)
		max1=x;
	}
	cout<<max1<<endl;
	return 0;
}
