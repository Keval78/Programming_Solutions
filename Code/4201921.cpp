#include<bits/stdc++.h>
using namespace std;
bool isSafe(int i,int j,int n, int m)
{
  if(i<0||j<0||i>n-1||j>m-1)
  {
    return false;
  }
  return true;
}
int main()
{
  int n,m;
  cin>>n>>m;
  string s[n];
  for(int i=0;i<n;i++)
    cin>>s[i];
  int count=0;
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      if(s[i][j]=='s'){
        //DownCross
        if(isSafe(i+1,j+1,n,m)){
          if(s[i+1][j+1]=='a'){
            if(isSafe(i+2,j+2,n,m)){
              if(s[i+2][j+2]=='b'){
                if(isSafe(i+3,j+3,n,m)){
                  if(s[i+3][j+3]=='a'){
                    count++;
                  }
                }
              }
            }
          }
        }
        //UpCross
        if(isSafe(i-1,j+1,n,m)){
          if(s[i-1][j+1]=='a'){
            if(isSafe(i-2,j+2,n,m)){
              if(s[i-2][j+2]=='b'){
                if(isSafe(i-3,j+3,n,m)){
                  if(s[i-3][j+3]=='a'){
                    count++;
                  }
                }
              }
            }
          }
        }
        //Down
        if(isSafe(i+1,j,n,m)){
          if(s[i+1][j]=='a'){
            if(isSafe(i+2,j,n,m)){
              if(s[i+2][j]=='b'){
                if(isSafe(i+3,j,n,m)){
                  if(s[i+3][j]=='a'){
                    count++;
                  }
                }
              }
            }
          }
        }
        //Right
        if(isSafe(i,j+1,n,m)){
          if(s[i][j+1]=='a'){
            if(isSafe(i,j+2,n,m)){
              if(s[i][j+2]=='b'){
                if(isSafe(i,j+3,n,m)){
                  if(s[i][j+3]=='a'){
                    cout<<"bhjbf"<<endl;
                    count++;
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  cout<<count<<endl;
}
