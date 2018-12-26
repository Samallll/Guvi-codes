number=int(input())
digit=0
while(number!=0):
    rem=number%10
    digit=digit+1
    number=number/10
print(digit)    
