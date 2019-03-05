n=input();
e=input();
for s in range(n,e):
    num=s;
    sum=0;
    while(s>0):
        digit=s%10;
        sum=sum+(digit*digit*digit);
        s=s//10;
    if(num==sum):
        print(num);
