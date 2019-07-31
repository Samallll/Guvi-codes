n=int(input());
if((n>=1)&(n<=100000)):
    a=[];
    for i in range(n):
        m=int(input());
        a.append(m);
    max=a[0];
    for i in range(n):
        if(a[i]>max):
            max=a[i];
    print(max);
else:
    print("Invalid Input");
    
