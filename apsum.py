n=int(input());
a=int(input());
d=int(input());
sum=0;
for i in range(n,0,-1):
    sum=sum+a+(i-1)*d;
print(sum);
