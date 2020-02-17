#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int n,k;
	cin>>n>>k;
	vector<int> v1;
	for(int i=0;i<n;i++)
	{
		int x;
		cin>>x;
		v1.push_back(x);
	}
	int cnt=0;
	for(int i=0;i<n;i++)
	{
		
		if((k-i-1>=0 && k+i-1<n)&&v1[k-1-i]==v1[k-1+i])
		{
			if(k-i-1==k+i-1)
				cnt+=v1[k-i-1];
			else
				cnt+=2*v1[k-i-1];
		}
		else if((k-i-1>=0 && k+i-1<n)&&v1[k-1-i]!=v1[k-1+i])
		{
			cnt+=0;
		}
		else if(k-i-1>=0)
		{
			cnt+=v1[k-i-1];
		}
		else if(k+i-1<n)
		{
			cnt+=v1[k+i-1];
		}
		
		
	}
	cout<< cnt;
}
