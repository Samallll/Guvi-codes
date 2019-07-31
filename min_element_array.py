n=int(input());
if((n>=1)&(n<=100000)):
    a=[];
    for i in range(n):
        m=int(input());
        a.append(m);
    min=a[0];
    for i in range(n):
        if(a[i]<min):
            min=a[i];
    print(min);
else:
    print("Invalid Input");
    
