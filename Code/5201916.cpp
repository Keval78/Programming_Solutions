/*#include<bits/stdc++.h>
using namespace std;
vector<int> v;
#define ll long long
int main()
{
  ll q;
  v.push_back(0);
  cin>>q;
  while(q--)
  {
    int choice;
    cin>>choice;
    if(choice==1)
    {
      ll x;
      cin>>x;
      v.push_back(x);
    }
    else if(choice==2)
    {
      ll x;
      cin>>x;
      for(int i=0;i<v.size();i++)
      {
        ll y=v[i];
        v.at(i)=(y^x);
      }
    }
    else
    {
      std::vector<int>::iterator result = std::min_element(std::begin(v), std::end(v));
      cout<<*result<<endl;
    }
  }
}*/
#include<bits/stdc++.h>
#define ll long long int
using namespace std;

typedef struct nam
{
    nam * left;
    nam * right;
}nam;

nam* newnode()
{
    nam * er = new nam();
    er->left = NULL;
    er->right = NULL;
    return er;
}

void insert(ll val, nam *head)
{
    nam *temp = head;
    for(int i = 31 ; i>=0; i--)
    {
        if((1<<i) & val)
        {
            if(temp->right == NULL)
            {
                temp->right = newnode();
                temp = temp->right;
                cout<<"Create to The Right node"<<endl;
            }
            else
            {
                temp = temp->right;
                cout<<"go to The Right node"<<endl;
            }
        }
        else
        {
            if(temp->left == NULL)
            {
                temp->left = newnode();
                //cout<<"Create to The Left node"<<endl;
            }

            temp = temp->left;
            cout<<(1<<i)<<"go to The Left node"<<endl;
        }
    }
}


ll findmin(nam* head,ll next)
{
    ll value = 0;
    nam *temp = head;
    cout<<"finding Min Value:------"<<endl;
    for(int i = 31 ; i>=0 ; i--)
    {
        cout<<(1<<i)<<"   "<<next<<endl;
        if((1<<i) & next)
        {
            if(temp->right != NULL)
            {
                temp = temp->right;
                cout<<"go to The right node right is no NULL"<<endl;
            }
            else
            {
                value += (1<<i);
                temp = temp->left;
                cout<<value<<"   go to left node"<<endl;
            }
        }
        else
        {
            if(temp->left != NULL)
            {
                temp = temp->left;
                cout<<"go to The Left node left is no NULL"<<endl;
            }
            else
            {
                value += (1<<i);
                temp = temp->right;
                cout<<value<<"   go to right node"<<endl;
            }
        }
    }

    return value;
}

int main()
{
    int q;
    cin>>q;
    ll lop = 0;
    nam*  head = newnode();
    int in = 0;

    insert(0,head);
    while(q--)
    {
        int t;
        cin>>t;
        if(t == 1)
        {
            ll x;
            cin>>x;
            insert(x^lop,head);
        }
        else if(t == 2)
        {
            ll x;
            cin>>x;
            lop^=x;
        }
        else
        {
            cout<<findmin(head,lop)<<endl;
        }
        cout<<"lop is "<<lop<<endl;
    }
}

/*
10
3
1 7
3
2 4
2 8
2 3
1 10
1 3
3
2 1

*/
