#include <iostream>
using namespace std;

int main()
{
   long long int n1,n2,n3;
   cin>>n1>>n2>>n3;
   string s1,s2,s3;
   cin>>s1>>s2>>s3;
   bool flag=false;
   int arr[26];
   string subs="",temp="";
   int j=0,k=0;
   for(long int i=0;i<n2;i++)
   {
       if(!flag && s2[i]<=s3[0])
            flag=true;
   }
   int i=-1;
   bool flag_for_s3=false;
   while(i++<n3)
   {
     if(s3[i]!=s3[i+1])
        break;
   }
   (s3[i]<s3[i+1])?flag_for_s3=true:flag_for_s3=false;
   cout<<flag_for_s3<<i;
   if(flag)
   {
     char min_ch='z';
     for(int i=n2-1;i>=0;i--)
     {
       if(s2[i]<=min_ch)
          min_ch=s2[i];
       temp+=min_ch;
     }
     for(int i=0;i<n2;i++)
     {
       if(s2[i]>s3[0])
          break;
       if(temp[n2-i-1]==s2[i])
          subs+=s2[i];
      }
      cout<<"subs: "<<subs<<"\n";
      if(!flag_for_s3)
      {
        while(subs.back()==s3[0])
        {
            subs.pop_back();
        }
      }
       cout<<s1+subs+s3<<"\n";
   }
   else
   {
       cout<<s1+s3<<"\n";
   }
}
/*
#include <iostream>

using namespace std;

int main()
{
   long long int n1,n2,n3;
   cin>>n1>>n2>>n3;
   string s1,s2,s3;
   cin>>s1>>s2>>s3;
   bool flag=false;
   int arr[26];
   string subs="",temp="";
   int j=0,k=0;
   for(long int i=0;i<n2;i++)
   {
       if( s2[i]<=s3[0])
       {
            flag=true;break;
       }
   }
   if(flag)
   {
        string res = "";
        int cr = 0;
        while (cr < n2) {
        	char mx = s2[cr];
        	for (int i = cr + 1; i < n2; i++)
        		mx = min(mx, s2[i]);
        	int lst = cr;
        for (int i = cr; i < n2; i++)
        		if (s2[i] == mx) {
        			res += s2[i];
        			lst = i;
        		}
        	cr = lst + 1;
	    }
	    //cout<<res<<"\n";
	    int i=-1;
        bool flag_for_s3=false;
        while(i++<n3)
        {
            if(s3[i]!=s3[i+1])
                break;
        }
        (s3[i]<s3[i+1])?flag_for_s3=true:flag_for_s3=false;
        if(!flag_for_s3)
        {
            while(res.back()==s3[0])
            {
                res.pop_back();
            }
        }
        cout<<s1<<res<<s3<<"\n";
    }
	else
	{
	    cout<<s1+s3<<"\n";
	}
   return 0;
}
*/
