n=input();
k=input();
for x in range(n,k + 1):
    if x > 1:
        for i in range(2,x):
           if (x % i) == 0:
               break;
        else:
            print(x);
