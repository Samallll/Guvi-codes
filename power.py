n=input();
k=input();
ans=1;
ans=pow(n,k);
def pow(n,k):
    ans=n*pow(n,k-1);
print(ans);
    
