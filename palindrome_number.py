n=input();
k=n;
sum=0;
if(n<=1000):
    while(n>0):
        d=n%10;
        sum=(sum*10)+d;
        n=n//10;
    if(k==sum):
        print("yes");
    else:
        print("no");
else:
    print("value should not exceed 1000");
